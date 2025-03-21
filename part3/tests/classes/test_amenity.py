import unittest
import datetime
from app.models.amenity import Amenity

class TestAmenity(unittest.TestCase):

    def test_initialization_valid_name(self):
        amenity = Amenity("Piscine")
        self.assertEqual(amenity.name, "Piscine")
        self.assertIsNotNone(amenity.id)
        self.assertIsInstance(amenity.created_at, datetime.datetime)

    def test_initialization_invalid_name_empty(self):
        with self.assertRaises(ValueError):
            Amenity("")

    def test_initialization_invalid_name_long(self):
        with self.assertRaises(ValueError):
            Amenity("A" * 51)  # 51 caractères

    def test_update_name_valid(self):
        amenity = Amenity("Salle de sport")
        old_updated_at = amenity.updated_at
        amenity.update_name("Gymnase")
        self.assertEqual(amenity.name, "Gymnase")
        self.assertNotEqual(amenity.updated_at, old_updated_at)  # Vérifie que la date a changé

    def test_update_name_invalid(self):
        amenity = Amenity("Sauna")
        old_updated_at = amenity.updated_at
        amenity.update_name("")  # Erreur prévue, le nom ne doit pas changer
        self.assertEqual(amenity.name, "Sauna")
        self.assertNotEqual(amenity.updated_at, old_updated_at)  # La date doit être mise à jour

if __name__ == "__main__":
    unittest.main()
