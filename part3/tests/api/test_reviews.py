import unittest
from unittest.mock import patch, MagicMock
from app import create_app
from app.models.review import Review
from app.models.user import User
from app.models.place import Place

class TestReviewAPI(unittest.TestCase):
    
    @patch('app.api.v1.reviews.HBnBFacade.create_review')
    def test_create_review(self, mock_create_review):
        # Données de la revue à tester
        review_data = {
            'text': 'Great place to stay!',
            'rating': 5,
            'user_id': '12345',
            'place_id': '67890'
        }
        
        # Création des objets simulés pour l'utilisateur et le lieu
        mock_user = MagicMock(spec=User)
        mock_user.id = '12345'
        mock_user.first_name = 'John'
        mock_user.last_name = 'Doe'
        
        mock_place = MagicMock(spec=Place)
        mock_place.id = '67890'
        mock_place.name = 'Test Place'
        
        # Simuler la création de la revue
        mock_review = MagicMock(spec=Review)
        mock_review.id = '1'
        mock_review.text = 'Great place to stay!'
        mock_review.rating = 5
        mock_review.user = mock_user
        mock_review.place = mock_place

        # Retourner la revue simulée à la méthode `create_review`
        mock_create_review.return_value = mock_review

        # Test de la route POST pour créer une revue
        with create_app().test_client() as client:
            response = client.post('/api/v1/reviews/', json=review_data)

            # Vérification du code de statut et des données retournées
            self.assertEqual(response.status_code, 201)
            response_json = response.get_json()
            self.assertEqual(response_json['message'], 'Review successfully created')
            self.assertEqual(response_json['text'], review_data['text'])
            self.assertEqual(response_json['rating'], review_data['rating'])
            self.assertEqual(response_json['user_id'], review_data['user_id'])
            self.assertEqual(response_json['place_id'], review_data['place_id'])

if __name__ == '__main__':
    unittest.main()
