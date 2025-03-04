import unittest
from app.models.review import Review


# Classes fictives pour simuler Place et User
class MockPlace:
    def __init__(self):
        self.title = "Place Test"
        self.description = "Description de la place"
        self.price = 100
        self.address = "123 Rue"


class MockUser:
    def __init__(self):
        self.first_name = "John"
        self.last_name = "Doe"
        self.email = "john.doe@example.com"


class TestReview(unittest.TestCase):

    def setUp(self):
        # Créer des instances simulées de Place et User
        self.place = MockPlace()
        self.user = MockUser()

    def test_create_invalid_review_empty_text(self):
        # Tester la création d'un avis avec un texte vide
        with self.assertRaises(ValueError) as context:
            Review(text="", rating=4, place=self.place, user=self.user)
        self.assertEqual(str(context.exception), "Veuillez écrire un commentaire")
        print("test_create_invalid_review_empty_text a réussi.")

    def test_create_invalid_review_invalid_rating(self):
        # Tester la création d'un avis avec une note invalide
        with self.assertRaises(ValueError) as context:
            Review(text="Super endroit", rating=6, place=self.place, user=self.user)
        self.assertEqual(str(context.exception), "La note doit être comprise entre 1 et 5")
        print("test_create_invalid_review_invalid_rating a réussi.")

    def test_create_invalid_review_invalid_place(self):
        # Tester la création d'un avis avec un mauvais type de lieu
        invalid_place = object()  # Utilisation d'un objet générique qui n'est pas une instance de Place
        with self.assertRaises(ValueError) as context:
            Review(text="Super endroit", rating=4, place=invalid_place, user=self.user)
        self.assertEqual(str(context.exception), "Le lieu doit être une instance de Place")
        print("test_create_invalid_review_invalid_place a réussi.")


if __name__ == "__main__":
    unittest.main()
