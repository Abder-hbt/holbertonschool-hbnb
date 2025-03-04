from unittest.mock import patch
import uuid
import unittest
from app.models.user import User
from app.models.place import Place

class TestUser(unittest.TestCase):

    @patch('app.models.place.Place.geocode_address')  # Mock de la méthode geocode_address
    def test_add_place(self, mocked_geocode):
        print("Test de l'ajout d'un lieu par un utilisateur")
        # Test l'ajout d'un lieu valide
        user = User(first_name="John", last_name="Doe", email=f"john.doe.{uuid.uuid4()}@example.com")
        mocked_geocode.return_value = (48.8566, 2.3522)  # Coordonnées fictives

        # Création d'un lieu avec amenities simulées via une liste vide
        place = Place(title="Lovely Place", description="A nice place to visit, very beautiful and comfortable", 
                      price=100, address="123 Street", owner=user)

        # Ajout de l'attribut amenities après la création du lieu
        place.amenities = []  # On assigne l'amenity après création du lieu

        user.add_place(place)  # Ajout d'un lieu
        self.assertIn(place, user.places)  # Vérifie que le lieu est bien ajouté
        print("Lieu ajouté avec succès")

        # Test l'ajout d'un lieu invalide
        with self.assertRaises(ValueError):
            user.add_place("Not a Place object")  # Ce n'est pas une instance de Place
            print("Erreur correctement levée pour un objet non valide")
