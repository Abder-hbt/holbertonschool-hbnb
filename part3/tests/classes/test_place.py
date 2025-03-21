import unittest
from unittest.mock import patch
from app.models.place import Place
from app.models.user import User

class TestPlace(unittest.TestCase):

    @patch("app.models.place.Place.geocode_address", return_value=(48.8566, 2.3522))  # Simule une localisation à Paris
    def test_initialization_valid(self, mock_geocode):
        owner = User("John", "Doe", "john2@example.com")
        place = Place("Appartement cosy", "Un joli appartement au centre-ville", 100.0, "Paris, France", owner, "WiFi, Parking")

        self.assertEqual(place.title, "Appartement cosy")
        self.assertEqual(place.price, 100.0)
        self.assertEqual(place.address, "Paris, France")
        self.assertEqual(place.owner, owner)
        self.assertEqual(place.amenities, "WiFi, Parking")
        self.assertEqual(place.latitude, 48.8566)
        self.assertEqual(place.longitude, 2.3522)

    def test_invalid_title_too_long(self):
        owner = User("John", "Doe", "john3@example.com")
        with self.assertRaises(ValueError):
            Place("A" * 101, "Description", 50.0, "Paris", owner, "WiFi")

    def test_invalid_price_negative(self):
        owner = User("John", "Doe", "john4@example.com")
        with self.assertRaises(ValueError):
            Place("Studio", "Petit studio", -10.0, "Lyon", owner, "WiFi")

    def test_invalid_owner_type(self):
        with self.assertRaises(ValueError):
            Place("Maison", "Grande maison", 200.0, "Marseille", "not_a_user", "WiFi")

    def test_add_review(self):
        owner = User("John", "Doe", "john5@example.com")
        place = Place("Villa", "Belle villa", 500.0, "Nice", owner, "Piscine")
        place.add_review("Super séjour !")

        self.assertIn("Super séjour !", place.reviews)

    @patch("app.models.place.Place.geocode_address", side_effect=RuntimeError("Erreur API"))
    def test_geocode_error(self, mock_geocode):
        owner = User("John", "Doe", "john6@example.com")
        place = Place("Cabane", "Charmante cabane", 80.0, "Inconnue", owner, "Chauffage")
        
        self.assertEqual(place.latitude, 0.0)  # Valeur par défaut en cas d'erreur
        self.assertEqual(place.longitude, 0.0)

if __name__ == "__main__":
    unittest.main()
