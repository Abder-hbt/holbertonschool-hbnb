# Ce module importe les classes nécessaires pour définir les modèles de données de l'application.
# Les classes importées incluent :
# - BaseModel : Classe de base pour les modèles, fournissant des attributs communs et des méthodes.
# - User : Classe représentant un utilisateur dans l'application.
# - Place : Classe représentant un lieu dans l'application.
# - Review : Classe représentant un avis sur un lieu.
# - Amenity : Classe représentant une commodité associée à un lieu.

from app.models.base_model import BaseModel
from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity
