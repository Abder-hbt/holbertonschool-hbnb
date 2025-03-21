import unittest
from unittest.mock import patch, MagicMock
from app import create_app
from app.services.facade import HBnBFacade
from app.models.place import Place
from app.models.user import User

class TestPlaceAPI(unittest.TestCase):
    
    @patch.object(HBnBFacade, 'get_user')
    @patch.object(HBnBFacade, 'create_place')
    def test_create_place(self, mock_create_place, mock_get_user):
        # Création d'un utilisateur avec les arguments requis
        mock_user = User(first_name='John', last_name='Doe', email='john.doe@example.com')
        mock_user.id = '12345'  # Attribuer l'ID manuellement (puisque User est déjà créé)

        # Simuler que la fonction `get_user` retourne cet utilisateur
        mock_get_user.return_value = mock_user

        # Données de la place à tester
        place_data = {
            'title': 'Test Place',
            'description': 'A nice test place',
            'price': 100.0,
            'address': '123 Test St',
            'owner_id': '12345',
            'latitude': 40.7128,  # Ajouter latitude ici
            'longitude': -74.0060,  # Ajouter longitude ici
            'amenities': ['wifi', 'ac']
        }

        # Utilisation de MagicMock pour simuler l'instance de Place
        mock_place = MagicMock(spec=Place)
        mock_place.id = '1'
        mock_place.title = 'Test Place'
        mock_place.description = 'A nice test place'
        mock_place.price = 100.0
        mock_place.address = '123 Test St'
        mock_place.owner = mock_user
        mock_place.latitude = 40.7128  # Ajout de latitude
        mock_place.longitude = -74.0060  # Ajout de longitude
        mock_place.amenities = ['wifi', 'ac']

        # Simuler la création de la place
        mock_create_place.return_value = mock_place  # Simule la création de la place

        # Test de la route POST (on va tester que la place est bien créée)
        with create_app().test_client() as client:
            response = client.post('/api/v1/places/', json=place_data)

            # Vérification du code de statut et des données retournées
            self.assertEqual(response.status_code, 201)
            response_json = response.get_json()
            self.assertEqual(response_json['title'], place_data['title'])
            self.assertEqual(response_json['address'], place_data['address'])
            self.assertEqual(response_json['owner_id'], place_data['owner_id'])
            self.assertEqual(response_json['latitude'], place_data['latitude'])  # Vérification de latitude
            self.assertEqual(response_json['longitude'], place_data['longitude'])  # Vérification de longitude
            self.assertIn('amenities', response_json)
            self.assertIn('wifi', response_json['amenities'])
            self.assertIn('ac', response_json['amenities'])

if __name__ == '__main__':
    unittest.main()
