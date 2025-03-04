import unittest
from app.models.user import User
from app.models.place import Place
import uuid

class TestUser(unittest.TestCase):

    def test_create_user_valid(self):
        print("Test de la création d'un utilisateur valide")
        user = User(first_name="John", last_name="Doe", email="john.doe1@example.com")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")
        self.assertEqual(user.email, "john.doe1@example.com")
        self.assertFalse(user.is_admin)  # Par défaut, is_admin doit être False
        self.assertEqual(len(user.places), 0)  # L'utilisateur ne doit avoir aucune place au départ
        print("Utilisateur valide créé avec succès")
    
    def test_valide_name(self):
        print("Test de la validation du nom de l'utilisateur")
        # Test un nom trop long
        with self.assertRaises(ValueError):
            User(first_name="A" * 51, last_name="Doe", email="valid.email@example.com")
            print("Erreur correctement levée pour un nom trop long")

        # Test un nom valide
        user = User(first_name="John", last_name="Doe", email="valid.email@example.com")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")
        print("Nom valide testé avec succès")

    def test_valide_email(self):
        print("Test de la validation de l'email de l'utilisateur")
        # Utilisation d'un UUID pour générer un email unique
        unique_email = f"john.doe.{uuid.uuid4()}@example.com"
        
        # Test un email invalide
        with self.assertRaises(ValueError):
            User(first_name="John", last_name="Doe", email="invalid-email")
            print("Erreur correctement levée pour un email invalide")

        # Test un email déjà utilisé avec un email unique pour chaque utilisateur
        User(first_name="John", last_name="Doe", email=unique_email)  # Créer un utilisateur valide
        with self.assertRaises(ValueError):
            User(first_name="Jane", last_name="Smith", email=unique_email)  # Email déjà utilisé
            print("Erreur correctement levée pour un email déjà utilisé")
    
    def test_add_place(self):
        print("Test de l'ajout d'un lieu par un utilisateur")
        # Test l'ajout d'un lieu valide
        user = User(first_name="John", last_name="Doe", email=f"john.doe.{uuid.uuid4()}@example.com")

    def test_is_admin(self):
        print("Test de la validation du rôle administrateur")
        # Test utilisateur administrateur
        admin_user = User(first_name="Admin", last_name="User", email="admin@example.com", is_admin=True)
        self.assertTrue(admin_user.is_admin)  # Vérifie que l'utilisateur est bien administrateur
        print("Utilisateur administrateur validé")

        # Test utilisateur non administrateur (par défaut)
        user = User(first_name="John", last_name="Doe", email=f"john.doe.{uuid.uuid4()}@example.com")
        self.assertFalse(user.is_admin)  # Vérifie que l'utilisateur n'est pas administrateur par défaut
        print("Utilisateur non administrateur validé")

if __name__ == "__main__":
    unittest.main()
