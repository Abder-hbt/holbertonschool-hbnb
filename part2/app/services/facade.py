""" 
Facade pour la gestion des données de l'application HBnB

Cette classe `HBnBFacade` centralise l'accès aux repositories en mémoire pour gérer 
les utilisateurs, les lieux, les avis et les commodités.

Classes :
- HBnBFacade : Fournit une interface unifiée pour interagir avec les repositories.

Attributs :
- user_repo : Repository pour la gestion des utilisateurs.
- place_repo : Repository pour la gestion des lieux.
- review_repo : Repository pour la gestion des avis.
- amenity_repo : Repository pour la gestion des commodités.

Méthodes :
- create_user(user_data) : Méthode à implémenter pour créer un utilisateur.
- get_place(place_id) : Méthode à implémenter pour récupérer un lieu par son ID.
"""

from app.persistence.repository import InMemoryRepository

class HBnBFacade:
    """ Facade pour gérer les repositories de l'application HBnB """
    
    def __init__(self):
        """ Initialise les repositories en mémoire pour chaque entité """
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    def create_user(self, user_data):
        """ Placeholder : Créer un utilisateur (à implémenter) """
        pass

    def get_place(self, place_id):
        """ Placeholder : Récupérer un lieu par son identifiant (à implémenter) """
        pass
