from flask import Flask
from flask_restx import Api
from app.api.v1.users import api as users_ns
from app.api.v1.amenities import api as amenities_ns
from app.api.v1.places import api as places_ns
from app.api.v1.reviews import api as reviews_ns

def create_app():
    """Factory function to create the Flask application"""
    app = Flask(__name__)

    # Création de l'API avec la route pour Swagger
    api = Api(
        app, 
        version='1.0', 
        title='HBnB API', 
        description='HBnB Application API',
    )

    # Enregistrement des namespaces (routes) pour les différentes parties de l'API
    api.add_namespace(users_ns, path='/api/v1/users')
    api.add_namespace(amenities_ns, path='/api/v1/amenities')
    api.add_namespace(places_ns, path='/api/v1/places')
    api.add_namespace(reviews_ns, path='/api/v1/reviews')

    return app
