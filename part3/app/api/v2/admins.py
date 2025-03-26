from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.facade import HBnBFacade
facade = HBnBFacade()
from flask import request

api = Namespace('admin', description='Admin operations')

user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user'),
    'is_admin': fields.Boolean(required=True, description='Whether the user is an admin'),
    'password': fields.String(required=True, description='Password of the user')
})

amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Name of the amenity')
})

@api.route('/users/')
class AdminUserCreate(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Email already registered')
    @api.response(400, 'Invalid input data')
    @jwt_required()
    def post(self):
        user_data = api.payload
        current_user = get_jwt_identity()
        
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403
        
        existing_user = facade.get_user_by_email(user_data['email'])        
        if existing_user:
            return {'error': 'Email already registered'}, 400

        new_user = facade.create_user(user_data)
        return {'id': new_user.id, 'first_name': new_user.first_name, 'last_name': new_user.last_name, 'email': new_user.email}, 201

@api.route('/users/<user_id>')
class AdminUserResource(Resource):    
    @api.expect(user_model, validate=True)
    @api.response(200, 'User updated successfully')
    @api.response(404, 'User not found')
    @jwt_required()
    def put(self, user_id):
        user_data = api.payload
        current_user = get_jwt_identity()

        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403
        
        existing_user = facade.get_user_by_email(user_data['email'])        
        if existing_user:
            return {'error': 'Email is already in use'}, 400
        
        updated_user = facade.update_user(user_id, user_data)

        if not updated_user:
            return {'error': 'Unable to update user'}, 404

        return {
            'id': updated_user.id,
            'first_name': updated_user.first_name,
            'last_name': updated_user.last_name,
            'email': updated_user.email
        }, 200

@api.route('/amenities/')
class AdminAmenityCreate(Resource):
    @jwt_required()
    @api.response(201, 'Amenity successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        current_user = get_jwt_identity()
        amenity_data = api.payload
        
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403

        existing_amenity = facade.get_amenity_by_name(amenity_data['name'])
        if existing_amenity:
            return {'error': 'Amenity already registered'}, 400
        
        new_amenity = facade.create_amenity(amenity_data)
        return {'id': new_amenity.id, 'name': new_amenity.name}, 201
    

@api.route('/amenities/<amenity_id>')
class AdminAmenityModify(Resource):
    @jwt_required()
    @api.response(200, 'Amenity details retrieved successfully')
    @api.response(404, 'Amenity not found')
    def put(self, amenity_id):
        amenity_data = api.payload
        amenity = facade.get_amenity(amenity_id)
        current_user = get_jwt_identity()

        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403
        
        if not amenity:
            return {'error': 'Amenity not found'}, 404
        
        updated_amenity = facade.update_amenity(amenity_id, amenity_data)

        if not updated_amenity:
            return {'error': 'Unable to update amenity'}, 400
        return{
            'id': updated_amenity.id,
            'name': updated_amenity.name
        }, 200
    
@api.route('/places/<place_id>')
class AdminPlaceModify(Resource):
    @jwt_required()
    def put(self, place_id):
        current_user = get_jwt_identity()
        data = api.payload
        
        # Set is_admin default to False if not exists
        is_admin = current_user.get('is_admin', False)
        user_id = current_user.get('id')

        place = facade.get_place(place_id)
        if not is_admin and place.owner_id != user_id:
            return {'error': 'Unauthorized action'}, 403
        
        place = facade.update_place(place_id, data)

        if place is None:
            return {"error": "Place not found"}, 404

        # Convertir l'objet Place en dictionnaire pour la sérialisation JSON
        place_data = {
            'id': place.id,
            'title': place.title,
            'description': place.description,
            'price': place.price,
            'address': place.address,
            'latitude': place.latitude,
            'longitude': place.longitude,
            'owner': {
                'id': place.owner.id,
                'first_name': place.owner.first_name,
                'last_name': place.owner.last_name
            },
            'amenities': place.amenities
        }

        return place_data, 200
