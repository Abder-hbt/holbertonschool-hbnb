# Ce module importe les classes nécessaires pour définir les modèles de données de l'application.
# Les classes importées incluent :
# - BaseModel : Classe de base pour les modèles, fournissant des attributs communs et des méthodes.
# - User : Classe représentant un utilisateur dans l'application.
# - Place : Classe représentant un lieu dans l'application.
# - Review : Classe représentant un avis sur un lieu.
# - Amenity : Classe représentant une commodité associée à un lieu.

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
