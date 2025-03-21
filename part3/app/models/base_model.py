# Définition de la classe BaseModel

# Ce module définit la classe `BaseModel`, qui sert de classe de base 
# pour d'autres modèles en fournissant des fonctionnalités communes.

# Classes :
# - BaseModel : Fournit un identifiant unique, des timestamps de création 
#   et de mise à jour, ainsi que des méthodes pour enregistrer et modifier l'objet.

# Attributs :
# - id : Identifiant unique généré automatiquement (UUID).
# - created_at : Date et heure de création de l'objet.
# - updated_at : Date et heure de la dernière modification de l'objet.

# Méthodes :
# - save() : Met à jour l'attribut `updated_at` pour enregistrer la dernière modification.
# - update(data) : Met à jour les attributs de l'objet à partir d'un dictionnaire fourni.

import uuid
from datetime import datetime

class BaseModel:
    # Classe de base fournissant un identifiant unique et des timestamps
    
    def __init__(self):
        # Initialise un nouvel objet avec un ID unique et des timestamps
        self.id = str(uuid.uuid4())  # Génère un identifiant unique
        self.created_at = datetime.now()  # Stocke la date et l'heure de création
        self.updated_at = datetime.now()  # Stocke la date et l'heure de la dernière mise à jour

    def save(self):
        # Met à jour le timestamp updated_at lors de chaque modification
        self.updated_at = datetime.now()

    def update(self, data):
        # Met à jour les attributs de l'objet à partir d'un dictionnaire fourni
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()  # Met à jour le timestamp updated_at après modification
