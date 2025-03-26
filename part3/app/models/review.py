from app.models.base_model import BaseModel
import datetime
from app import db
from typing import TYPE_CHECKING

class Review(BaseModel):
    # Représente un avis sur un lieu

    __tablename__ = 'review'

    text = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    place_id = db.Column(db.Integer, db.ForeignKey('place.id'), nullable=False)

    def __init__(self, text, rating, place, user):
        # Initialise un nouvel objet Review avec des validations
        super().__init__()  # Appelle le constructeur de la classe parente
        self.text = self.valide_text(text)  # Valide et assigne le texte de l'avis
        self.rating = self.valide_rating(rating)  # Valide et assigne la note
        self.place = self.correct_place(place)  # Valide et assigne le lieu
        self.user = self.is_user(user)  # Valide et assigne l'utilisateur

    def valide_text(self, text):
        # Valide que le texte de l'avis n'est pas vide
        if len(text) == 0:
            raise ValueError("Veuillez écrire un commentaire")
        return text
    
    def valide_rating(self, rating):
        # Valide que la note est comprise entre 1 et 5
        rating = float(rating)
        if rating < 1 or rating > 5:
            raise ValueError("La note doit être comprise entre 1 et 5")
        return rating
    
    def correct_place(self, place_id):
        # Fait le lien entre l'entités Review et Place 
        from app.models.place import Place
        if not isinstance(place_id, Place):
            raise ValueError("Le lieu doit être une instance de Place")
        return place_id
    
    def is_user(self, user_id):
        # Fait le lien entre l'entités Review et User
        from app.models.user import User
        if not isinstance(user_id, User):
            raise ValueError("L'utilisateur doit être une instance de User")
        return user_id

    def update_review(self, new_text=None, new_rating=None):
        # Met à jour le texte et/ou la note de l'avis
        try:
            if new_text is not None:
                self.text = self.valide_text(new_text)  # Valide et met à jour le texte
            if new_rating is not None:
                self.rating = self.valide_rating(new_rating)  # Valide et met à jour la note
            self.updated_at = datetime.datetime.now()  # Met à jour la date de modification
        except ValueError as e:
            print(f"Erreur lors de la mise à jour de l'avis : {e}")  # Gère les erreurs de validation
