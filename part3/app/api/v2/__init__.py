from flask import Blueprint
from flask_restx import Api
from app.api.v1.users import api as users_ns

# Création du Blueprint
blueprint = Blueprint('api', __name__, url_prefix='/api/v1')

# Initialisation de l'API Flask-RESTx
api = Api(
    blueprint,
    title="HBnB API",
    version="1.0",
    description="Documentation de l'API HBnB",
    doc="/"  # Swagger UI sera accessible à /api/v1/
)

# Ajout des namespaces
api.add_namespace(users_ns, path='/users')
