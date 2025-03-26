from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

bcrypt = Bcrypt()
db = SQLAlchemy()
jwt = JWTManager()

def create_app(config_class="config.DevelopmentConfig"):
    """Factory function to create the Flask application"""
    app = Flask(__name__)
    app.config.from_object(config_class)
    jwt.init_app(app)
    bcrypt.init_app(app)
    
    # Initialisation de SQLAlchemy
    db.init_app(app)

    # Création de l'API avec la route pour Swagger
    api = Api(
        app,
        version='1.0',
        title='HBnB API',
        description='HBnB Application API',
    )

    # Enregistrement des namespaces (routes) pour les différentes parties de l'API
    from app.api.v2.users import api as users_ns
    from app.api.v2.amenities import api as amenities_ns
    from app.api.v2.places import api as places_ns
    from app.api.v2.reviews import api as reviews_ns

    api.add_namespace(users_ns, path='/api/v1/users')
    api.add_namespace(amenities_ns, path='/api/v1/amenities')
    api.add_namespace(places_ns, path='/api/v1/places')
    api.add_namespace(reviews_ns, path='/api/v1/reviews')

    return app
