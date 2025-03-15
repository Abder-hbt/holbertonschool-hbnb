from abc import ABC, abstractmethod


class Repository(ABC):
    @abstractmethod
    def add(self, obj):
        pass

    @abstractmethod
    def get(self, obj_id):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def update(self, obj_id, data):
        pass

    @abstractmethod
    def delete(self, obj_id):
        pass

    @abstractmethod
    def get_by_attribute(self, attr_name, attr_value):
        pass


class InMemoryRepository(Repository):
    def __init__(self):
        self._storage = {}
        self._next_id = 1  # ID de départ pour générer un ID unique

    def add(self, obj):
        # Si l'objet n'a pas d'id, on lui en assigne un automatiquement
        if not hasattr(obj, 'id') or obj.id is None:
            obj.id = self._next_id
            self._next_id += 1
        print(f"📥 Ajout dans le repository : {obj.id}")
        self._storage[obj.id] = obj  # Stocke l'objet
        print(f"📦 Contenu du repository après ajout : {self._storage}")

    def get(self, obj_id):
        obj = self._storage.get(obj_id)
        if obj is None:
            raise ValueError(f"Objet avec l'ID {obj_id} non trouvé.")
        return obj

    def get_all(self):
        return list(self._storage.values())

    def update(self, obj_id, data):
        obj = self.get(obj_id)  # Récupère l'objet avec vérification
        for key, value in data.items():
            if hasattr(obj, key):  # Vérifie que l'attribut existe sur l'objet
                setattr(obj, key, value)
            else:
                raise AttributeError(f"L'attribut '{key}' n'existe pas sur l'objet.")
        print(f"📦 Objet avec ID {obj_id} mis à jour : {obj}")

    def delete(self, obj_id):
        if obj_id in self._storage:
            del self._storage[obj_id]
            print(f"🗑️ Objet avec ID {obj_id} supprimé.")
        else:
            raise ValueError(f"Objet avec l'ID {obj_id} non trouvé.")

    def get_by_attribute(self, attr_name, attr_value):
        for obj in self._storage.values():
            if hasattr(obj, attr_name) and getattr(obj, attr_name) == attr_value:
                return obj
        return None
