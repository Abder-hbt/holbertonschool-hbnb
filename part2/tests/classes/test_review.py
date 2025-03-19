import unittest
from app.models.review import Review
from app.models.user import User
from app.models.place import Place
import uuid  # Pour générer un email unique à chaque test

class TestReview(unittest.TestCase):
    
    def setUp(self):
        """Initialisation avant chaque test."""
        # Création d'un utilisateur fictif avec un email unique
        self.user = User(first_name="John", last_name="Doe", email=f"johndoe{uuid.uuid4().hex}@test.com")
        # Création d'un lieu fictif
        self.place = Place(title="Test Place", description="A test place", price=100.0, address="Nice", owner=self.user, amenities="WiFi")
    
    def test_review_creation_valid(self):
        """Test la création d'un avis valide."""
        review = Review(text="Excellent place!", rating=5, place=self.place, user=self.user)
        self.assertEqual(review.text, "Excellent place!")
        self.assertEqual(review.rating, 5)
        self.assertEqual(review.place, self.place)
        self.assertEqual(review.user, self.user)
    
    def test_review_rating_invalid_too_low(self):
        """Test un avis avec une note trop basse."""
        with self.assertRaises(ValueError) as context:
            Review(text="Bad place", rating=0, place=self.place, user=self.user)
        self.assertEqual(str(context.exception), "La note doit être comprise entre 1 et 5")
    
    def test_review_rating_invalid_too_high(self):
        """Test un avis avec une note trop haute."""
        with self.assertRaises(ValueError) as context:
            Review(text="Amazing place", rating=6, place=self.place, user=self.user)
        self.assertEqual(str(context.exception), "La note doit être comprise entre 1 et 5")
    
    def test_review_text_empty(self):
        """Test un avis avec un texte vide."""
        with self.assertRaises(ValueError) as context:
            Review(text="", rating=3, place=self.place, user=self.user)
        self.assertEqual(str(context.exception), "Veuillez écrire un commentaire")
    
    def test_review_place_invalid(self):
        """Test un avis avec un lieu invalide."""
        with self.assertRaises(ValueError) as context:
            Review(text="Nice place", rating=4, place="Invalid Place", user=self.user)
        self.assertEqual(str(context.exception), "Le lieu doit être une instance de Place")
    
    def test_review_user_invalid(self):
        """Test un avis avec un utilisateur invalide."""
        with self.assertRaises(ValueError) as context:
            Review(text="Nice place", rating=4, place=self.place, user="Invalid User")
        self.assertEqual(str(context.exception), "L'utilisateur doit être une instance de User")

if __name__ == "__main__":
    unittest.main()
