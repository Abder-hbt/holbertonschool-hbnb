""" 
Définition d'un modèle de repository avec une implémentation en mémoire

Ce module définit une classe abstraite `Repository` qui impose des méthodes pour la gestion d'objets.
Il inclut également `InMemoryRepository`, une implémentation stockant les objets en mémoire.

Classes :
- Repository (ABC) : Interface pour définir un repository avec des méthodes abstraites.
- InMemoryRepository : Implémentation en mémoire du repository.

Méthodes principales :
- add(obj) : Ajoute un objet au repository.
- get(obj_id) : Récupère un objet par son identifiant.
- get_all() : Retourne tous les objets stockés.
- update(obj_id, data) : Met à jour un objet existant.
- delete(obj_id) : Supprime un objet par son identifiant.
- get_by_attribute(attr_name, attr_value) : Recherche un objet par un attribut donné.
"""
from abc import ABC, abstractmethod

class Repository(ABC):
    """ Interface abstraite pour un repository générique """
    
    @abstractmethod
    def add(self, obj):
        """ Ajoute un objet au repository """
        pass

    @abstractmethod
    def get(self, obj_id):
        """ Récupère un objet par son identifiant """
        pass

    @abstractmethod
    def get_all(self):
        """ Retourne la liste de tous les objets stockés """
        pass

    @abstractmethod
    def update(self, obj_id, data):
        """ Met à jour un objet existant avec de nouvelles données """
        pass

    @abstractmethod
    def delete(self, obj_id):
        """ Supprime un objet du repository par son identifiant """
        pass

    @abstractmethod
    def get_by_attribute(self, attr_name, attr_value):
        """ Recherche un objet en fonction d'un attribut spécifique """
        pass


class InMemoryRepository(Repository):
    """ Implémentation du repository en mémoire avec un dictionnaire """
    
    def __init__(self):
        """ Initialise un dictionnaire pour stocker les objets """
        self._storage = {}

    def add(self, obj):
        """ Ajoute un objet en utilisant son identifiant comme clé """
        self._storage[obj.id] = obj

    def get(self, obj_id):
        """ Récupère un objet en fonction de son identifiant """
        return self._storage.get(obj_id)

    def get_all(self):
        """ Retourne tous les objets stockés sous forme de liste """
        return list(self._storage.values())

    def update(self, obj_id, data):
        """ Met à jour un objet existant s'il est trouvé """
        obj = self.get(obj_id)
        if obj:
            obj.update(data)

    def delete(self, obj_id):
        """ Supprime un objet du stockage s'il existe """
        if obj_id in self._storage:
            del self._storage[obj_id]

    def get_by_attribute(self, attr_name, attr_value):
        """ Recherche un objet par un attribut et retourne le premier correspondant """
        return next((obj for obj in self._storage.values() if getattr(obj, attr_name) == attr_value), None)
