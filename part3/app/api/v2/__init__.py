from flask import Blueprint
from flask_restx import Api
from app.api.v2.users import api as users_ns  # Corrigez l'importation pour pointer vers v2

# Création du Blueprint
blueprint = Blueprint('api', __name__, url_prefix='/api/v2')  # Mettez à jour le préfixe pour v2

# Initialisation de l'API Flask-RESTx
api = Api(
    blueprint,
    title="HBnB API",
    version="1.0",
    description="Documentation de l'API HBnB",
    doc="/"  # Swagger UI sera accessible à /api/v2/
)

# Ajout des namespaces
api.add_namespace(users_ns, path='/users')
