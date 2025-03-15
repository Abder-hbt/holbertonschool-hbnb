from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review

class HBnBFacade:
    def __init__(self):
        # Initialisation des repositories
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # User
    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)
    
    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    def update_user(self, user_id, user_data):
        user = self.user_repo.get(user_id)  # Récupère l'utilisateur à mettre à jour
        if not user:
            return None
        updated_user_data = {key: value for key, value in user_data.items()}
        self.user_repo.update(user.id, updated_user_data)
        return self.user_repo.get(user.id)

    # Amenity
    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity
    
    def get_amenity_by_name(self, name):
        return self.amenity_repo.get_by_attribute('name', name)

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.amenity_repo.get(amenity_id)
        if not amenity:
            return None
        updated_amenity_data = {key: value for key, value in amenity_data.items()}
        self.amenity_repo.update(amenity.id, updated_amenity_data)
        return self.amenity_repo.get(amenity.id)


    # Place
    def create_place(self, data):
        # Assure-toi que l'utilisateur avec owner_id existe
        owner_id = data.get("owner_id")
        owner = self.user_repo.get(owner_id)  # Utilisation de self.user_repo ici
        
        if not owner:
            raise ValueError(f"Utilisateur avec l'ID {owner_id} non trouvé.")
        
        # Ensuite, crée la place
        place = Place(
            title=data['title'],
            description=data.get('description', ''),  # Utilisation d'une valeur par défaut pour la description
            price=data['price'],
            address=data['address'],
            owner=owner,
            amenities=data['amenities']
        )
        
        # Ajout de la place dans le repository des places
        self.place_repo.add(place)
        
        return place

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        place = self.get_place(place_id)
        if not place:
            return None
        for key, value in place_data.items():
            setattr(place, key, value)
        return place

    def delete_place(self, place_id):
        place = self.get_place(place_id)
        if not place:
            return False
        self.place_repo.delete(place_id)
        return True

    # Review
    def create_review(self, review_data):
        review = Review(**review_data)
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        return [review for review in self.get_all_reviews() if review.place_id == place_id]

    def update_review(self, review_id, review_data):
        review = self.get_review(review_id)
        if not review:
            return None
        for key, value in review_data.items():
            setattr(review, key, value)
        self.review_repo.update(review)
        return review

    def delete_review(self, review_id):
        review = self.get_review(review_id)
        if not review:
            return False
        self.review_repo.delete(review_id)
        return True
