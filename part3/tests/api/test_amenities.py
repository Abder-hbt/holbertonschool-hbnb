import unittest
from app import create_app
from app.models.amenity import Amenity  # Si nécessaire pour la création d'objets amenity dans tes tests

class TestAmenityEndpoints(unittest.TestCase):

    def setUp(self):
        # Créer une instance de l'application Flask et un client pour les tests
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_amenity(self):
        # Test la création d'une amenity valide
        response = self.client.post('/api/v1/amenities/', json={
            "name": "Swimming Pool"
        })
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertIn('id', data)
        self.assertEqual(data['name'], "Swimming Pool")

    def test_create_amenity_invalid_data(self):
        # Test la création d'une amenity avec des données invalides (nom vide)
        response = self.client.post('/api/v1/amenities/', json={
            "name": ""
        })
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertIn('error', data)
        self.assertEqual(data['error'], 'Veuillez entrer un nom obligatoire de maximum 50 caractères')

    def test_create_amenity_duplicate(self):
        # Test la création d'une amenity avec un nom déjà existant
        # Créons d'abord une amenity valide
        self.client.post('/api/v1/amenities/', json={
            "name": "Gym"
        })

        # Tentons de créer la même amenity
        response = self.client.post('/api/v1/amenities/', json={
            "name": "Gym"
        })
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertIn('error', data)
        self.assertEqual(data['error'], 'Amenity already registered')

    def test_get_amenities(self):
        # Test la récupération de la liste des amenities
        response = self.client.get('/api/v1/amenities/')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIsInstance(data, list)  # La réponse doit être une liste
        if len(data) > 0:
            self.assertIn('id', data[0])
            self.assertIn('name', data[0])

    def test_get_amenity_by_id(self):
        # Test la récupération d'une amenity par ID
        # Créons une amenity d'abord
        response = self.client.post('/api/v1/amenities/', json={
            "name": "Sauna"
        })
        amenity_id = response.get_json()['id']

        # Récupérons l'amenity par son ID
        response = self.client.get(f'/api/v1/amenities/{amenity_id}')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['id'], amenity_id)
        self.assertEqual(data['name'], "Sauna")

    def test_get_amenity_not_found(self):
        # Test la récupération d'une amenity avec un ID inexistant
        response = self.client.get('/api/v1/amenities/9999')
        self.assertEqual(response.status_code, 404)
        data = response.get_json()
        self.assertIn('error', data)
        self.assertEqual(data['error'], 'Amenity not found')

    def test_update_amenity(self):
        # Test la mise à jour d'une amenity existante
        response = self.client.post('/api/v1/amenities/', json={
            "name": "Tennis Court"
        })
        amenity_id = response.get_json()['id']

        # Mettons à jour cette amenity
        response = self.client.put(f'/api/v1/amenities/{amenity_id}', json={
            "name": "Updated Tennis Court"
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['name'], "Updated Tennis Court")

    def test_update_amenity_not_found(self):
        # Test la mise à jour d'une amenity inexistante
        response = self.client.put('/api/v1/amenities/9999', json={
            "name": "Non-existent Amenity"
        })
        self.assertEqual(response.status_code, 404)
        data = response.get_json()
        self.assertIn('error', data)
        self.assertEqual(data['error'], 'Amenity not found')

if __name__ == '__main__':
    unittest.main()
