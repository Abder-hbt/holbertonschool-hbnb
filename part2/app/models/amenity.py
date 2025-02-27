from models.base_model import BaseModel
import datetime

class Amenity(BaseModel):

    def __init__(self, name):
        super().__init__()
        self.name = self.valide_name(name)

    def valide_name(self, name):
        name = name.strip()
        if not name or len(name) > 50:
            raise ValueError("Veuillez entrer un nom obligatoire de maximum 50 caractères")
        return name

    def update_name(self, new_name=None):
        # Met à jour le nom
        try:
            if new_name:
                self.name = self.valide_name(new_name)  # Valide et met à jour le nom
            self.updated_at = datetime.datetime.now()  # Met à jour la date de modification
        except ValueError as e:
            print(f"Erreur lors de la mise à jour du nom : {e}")  # Gère les erreurs de validation