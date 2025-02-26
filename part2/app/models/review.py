# Définition de la classe Review

# Ce module définit la classe `Review`, qui représente un avis sur un lieu dans l'application.
# Elle hérite de `BaseModel` et inclut des validations pour les attributs de l'avis.

# Classes :
# - Review : Représente un avis avec des attributs tels que le texte, la note, 
#   le lieu et l'utilisateur, ainsi que des méthodes pour la validation et la mise à jour.

# Attributs :
# - text : Contenu de l'avis, validé pour ne pas être vide.
# - rating : Note de l'avis, validée pour être comprise entre 1 et 5.
# - place : Lieu associé à l'avis, validé pour être une instance de `Place`.
# - user : Utilisateur ayant laissé l'avis, validé pour être une instance de `User`.

# Méthodes :
# - __init__(text, rating, place, user) : Constructeur qui initialise les attributs de l'avis
#   et effectue des validations.
# - valide_text(text) : Valide que le texte de l'avis n'est pas vide.
# - valide_rating(rating) : Valide que la note est comprise entre 1 et 5.
# - correct_place(place) : Valide que le lieu est une instance de `Place`.
# - is_user(user) : Valide que l'utilisateur est une instance de `User`.
# - update_review(new_text, new_rating) : Met à jour le texte et/ou la note de l'avis 
#   et enregistre la date de mise à jour.

from models.base_model import BaseModel
from models.user import User
from models.place import Place
import datetime

class Review(BaseModel):
    # Représente un avis sur un lieu

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
    
    def correct_place(self, place):
        # Valide que le lieu est une instance de Place
        if not isinstance(place, Place):
            raise ValueError("Le lieu doit être une instance de Place")
        return place
    
    def is_user(self, user):
        # Valide que l'utilisateur est une instance de User
        if not isinstance(user, User):
            raise ValueError("L'utilisateur doit être une instance de User")
        return user

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
