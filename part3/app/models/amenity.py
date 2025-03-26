# Classe Amenity représentant une commodité associée à un lieu.
# Hérite de BaseModel et ajoute un attribut spécifique : name.

from app.models.base_model import BaseModel
import datetime
from app import db, bcrypt
import uuid

class Amenity(BaseModel):

    __tablename__ = 'amenitie' 

    name = db.Column(db.String(50), nullable=False)

    def __init__(self, name):
        # Initialise l'instance avec un nom validé
        super().__init__()
        self.name = self.valide_name(name)

    def valide_name(self, name):
        # Valide que le nom n'est pas vide et ne dépasse pas 50 caractères
        name = name.strip()
        if not name or len(name) > 50:
            raise ValueError("Veuillez entrer un nom obligatoire de maximum 50 caractères")
        return name

    def update_name(self, new_name=None):
        # Met à jour le nom avec validation et ajuste la date de modification
        try:
            if new_name:
                self.name = self.valide_name(new_name)  # Valide et met à jour le nom
            self.updated_at = datetime.datetime.now()  # Met à jour la date de modification
        except ValueError as e:
            print(f"Erreur lors de la mise à jour du nom : {e}")  # Gère les erreurs de validation
