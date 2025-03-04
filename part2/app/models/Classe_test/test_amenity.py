import unittest
from app.models.amenity import Amenity  # Assure-toi que le chemin d'importation est correct

class TestAmenity(unittest.TestCase):

    def test_create_valid_amenity(self):
        # Test de création d'une amenity avec un nom valide
        try:
            amenity = Amenity("WiFi")
            print(f"Amenity '{amenity.name}' créée avec succès")
        except ValueError as e:
            print(f"Erreur lors de la création de l'amenity : {e}")

    def test_create_invalid_amenity_empty_name(self):
        # Test de création d'une amenity avec un nom vide
        try:
            amenity = Amenity("")
            print("Erreur attendue lors de la création d'une amenity avec un nom vide")
        except ValueError as e:
            print(f"Erreur lors de la création de l'amenity : {e}")

    def test_create_invalid_amenity_long_name(self):
        # Test de création d'une amenity avec un nom trop long
        try:
            amenity = Amenity("A" * 51)
            print("Erreur attendue lors de la création d'une amenity avec un nom trop long")
        except ValueError as e:
            print(f"Erreur lors de la création de l'amenity : {e}")

    def test_update_valid_name(self):
        # Test de mise à jour d'une amenity avec un nom valide
        amenity = Amenity("WiFi")
        try:
            amenity.update_name("Spa")
            print(f"Nom mis à jour avec succès : {amenity.name}")
        except ValueError as e:
            print(f"Erreur lors de la mise à jour du nom : {e}")

    def test_update_invalid_name_empty(self):
        # Test de mise à jour avec un nom vide
        amenity = Amenity("WiFi")
        try:
            amenity.update_name("")
            print("Erreur attendue lors de la mise à jour avec un nom vide")
        except ValueError as e:
            print(f"Erreur lors de la mise à jour du nom : {e}")

    def test_update_invalid_name_long(self):
        # Test de mise à jour avec un nom trop long
        amenity = Amenity("WiFi")
        try:
            amenity.update_name("A" * 51)
            print("Erreur attendue lors de la mise à jour avec un nom trop long")
        except ValueError as e:
            print(f"Erreur lors de la mise à jour du nom : {e}")

if __name__ == "__main__":
    unittest.main()
