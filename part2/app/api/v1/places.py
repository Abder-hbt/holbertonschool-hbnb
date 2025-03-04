from flask_restx import Namespace, Resource, fields
from flask import request
from app.services.facade import HBnBFacade

facade = HBnBFacade()

def validate_place_data(data):
    """Validate the place data."""
    required_fields = ['title', 'price', 'latitude', 'longitude', 'owner_id', 'amenities']
    for field in required_fields:
        if field not in data or data[field] is None:
            return False
    return True

api = Namespace('places', description='Place operations')

amenity_model = api.model('PlaceAmenity', {
    'id': fields.String(description='Amenity ID'),
    'name': fields.String(description='Name of the amenity')
})

user_model = api.model('PlaceUser', {
    'id': fields.String(description='User ID'),
    'first_name': fields.String(description='First name of the owner'),
    'last_name': fields.String(description='Last name of the owner'),
    'email': fields.String(description='Email of the owner')
})

place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'address': fields.String(required=True, description='Address of the place'),  # Address field
    'owner_id': fields.String(required=True, description='ID of the owner'),
    'amenities': fields.List(fields.String, required=True, description="List of amenities ID's"),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place')
})

@api.route('/')
class PlaceList(Resource):
    @api.expect(place_model)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new place"""
        place_data = api.payload
        if not place_data:
            return {'error': 'No data received'}, 400

        if not validate_place_data(place_data):
            return {'error': 'Invalid input data', 'details': place_data}, 400
        
        try:
            new_place = facade.create_place(place_data)
        except ValueError as e:
            return {'error': str(e)}, 400
        except Exception as e:
            return {'error': 'Unexpected error', 'details': str(e)}, 500
        
        return {'message': 'Place successfully created', 'id': new_place.id}, 201

    @api.response(200, 'List of places retrieved successfully')
    def get(self):
        """Retrieve a list of all places"""
        data = facade.get_all_places()
        return [{'id': place.id, 'latitude': place.latitude, 'longitude': place.longitude, 'owner_id': place.owner.id, 'amenities': place.amenities} for place in data], 200

@api.route('/<place_id>')
class PlaceResource(Resource):
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get place details by ID"""
        place = facade.get_place_by_id(place_id)
        if not place:
            return {'error': 'Place not found'}, 404
        return place, 200

    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')
    def put(self, place_id):
        """Update a place's information"""
        data = request.json
        place = facade.get_place_by_id(place_id)

        if place is None:
            return {'error': 'Place not found'}, 404
        if not validate_place_data(data):
            return {'error': 'Invalid input data'}, 400
        
        updated_place = facade.update_place(place_id, data)
        return {'message': 'Place updated successfully'}, 200

    @api.response(200, 'Place deleted successfully')
    @api.response(404, 'Place not found')
    def delete(self, place_id):
        """Delete a place by ID"""
        place = facade.get_place(place_id)
        if not place:
            return {'error': 'Place not found'}, 404
        
        facade.delete_place(place_id)
        return {'message': 'Place successfully deleted'}, 200
