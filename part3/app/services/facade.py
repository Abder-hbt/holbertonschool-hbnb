from app.persistence.repository import SQLAlchemyRepository
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review

class HBnBFacade:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(HBnBFacade, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, ):
        # Initialisation des repositories
        if not hasattr(self, 'initialized'):
            # Initialisation des dépôts distincts
            self.user_repo = SQLAlchemyRepository(User)  # Switched to SQLAlchemyRepository
            self.place_repos = SQLAlchemyRepository(Place)
            self.review_repo = SQLAlchemyRepository(Review)
            self.amenity_repo = SQLAlchemyRepository(Amenity)

    # User
    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        print(f"Utilisateur ajouté : {user.id}, {user.first_name} {user.last_name}")
        return user

    def get_user(self, user_id):
        print(f"Recherche de l'utilisateur avec l'ID : {user_id}")
        user = self.user_repo.get(user_id)
        if user is None:
            # Vérifie les utilisateurs dans le dépôt pour déboguer
            all_users = self.user_repo.get_all()
            print("Utilisateurs dans le dépôt :", [u.id for u in all_users])
            raise ValueError(f"Objet avec l'ID {user_id} non trouvé.")
        return user
    
    def get_all_users(self):
        """Retrieve all users from the repository"""
        users = self.user_repo.get_all()
        return users
    
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
    def create_place(self, place_data):
        # Récupérer l'objet User à partir de l'ID
        owner_id = place_data['owner_id']
        owner = self.get_user(owner_id)  # Utilise get_user pour accéder à user_repo

        # Vérification et log
        if not isinstance(owner, User):
            print(f"Type de owner: {type(owner)}")  # Ajoute un log pour vérifier le type
            raise ValueError("Le propriétaire doit être une instance de User.")

        print(f"Propriétaire récupéré: {owner.id}, {owner.first_name} {owner.last_name}")

        # Créer une instance de Place avec l'objet User
        place = Place(
            title=place_data['title'],
            description=place_data['description'],
            price=place_data['price'],
            address=place_data['address'],
            owner=owner,  # Passe l'objet User ici
            amenities=place_data['amenities']
        )
        # Sauvegarder le lieu dans le dépôt des lieux
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        print(f"Recherche de la place avec l'ID : {place_id}")
        place = self.place_repo.get(place_id)
        if place is None:
            # Vérifie les places dans le dépôt pour déboguer
            all_places = self.place_repo.get_all()
            print("Places dans le dépôt :", [p.id for p in all_places])
            raise ValueError(f"Objet avec l'ID {place_id} non trouvé.")

        # Convertir l'objet Place en dictionnaire pour la sérialisation JSON
        place_data = {
            "id": place.id,
            "title": place.title,
            "description": place.description,
            "price": place.price,
            "address": place.address,
            "latitude": getattr(place, 'latitude', None),  # Utilise getattr pour éviter les erreurs si l'attribut n'existe pas
            "longitude": getattr(place, 'longitude', None),  # Utilise getattr pour éviter les erreurs si l'attribut n'existe pas
            "owner": {
                "id": place.owner.id,
                "first_name": place.owner.first_name,
                "last_name": place.owner.last_name
            },
            "amenities": place.amenities,
            "reviews": [{"id": r.id, "text": r.text, "rating": r.rating, "user_id": r.user.id} for r in place.reviews]
        }
        return place_data

    def get_all_places(self):
        places = self.place_repo.get_all()  # Récupère la liste de tous les lieux
        place_data_list = []

        for place in places:
            place_data = {
                "id": place.id,
                "title": place.title,
                "description": place.description,
                "price": place.price,
                "address": place.address,
                "latitude": place.latitude,
                "longitude": place.longitude,
                "owner": {
                    "id": place.owner.id,
                    "first_name": place.owner.first_name,
                    "last_name": place.owner.last_name
                },
                "amenities": place.amenities
            }
            place_data_list.append(place_data)

        return place_data_list

    def update_place(self, place_id, place_data):
        place = self.place_repo.get(place_id)
        if not place:
            return None
        updated_place_data = {key: value for key, value in place_data.items()}
        self.place_repo.update(place.id, updated_place_data)
        return self.place_repo.get(place.id)
    
    def get_place_object(self, place_id):
        print(f"Recherche de la place avec l'ID : {place_id}")
        place = self.place_repo.get(place_id)
        if place is None:
            # Vérifie les places dans le dépôt pour déboguer
            all_places = self.place_repo.get_all()
            print("Places dans le dépôt :", [p.id for p in all_places])
            raise ValueError(f"Objet avec l'ID {place_id} non trouvé.")
        return place  # Retourne l'objet Place



    # Review
    def create_review(self, review_data):
        user_id = review_data['user_id']
        user = self.get_user(user_id)

        place_id = review_data['place_id']
        place = self.get_place_object(place_id)  # Utilise get_place_object pour obtenir un objet Place

        if not isinstance(user, User):
            print(f"Type de user: {type(user)}")
            raise ValueError("L'utilisateur doit être une instance de User.")

        print(f"User récupéré: {user.id}, {user.first_name} {user.last_name}")

        if not isinstance(place, Place):
            print(f"Type de place: {type(place)}")
            raise ValueError("Le lieu doit être une instance de Place.")

        print(f"Place récupéré: {place.id}, {place.address}")

        review = Review(
            text=review_data['text'],
            rating=review_data['rating'],
            user=user,
            place=place
        )

        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        # Récupérer toutes les reviews
        all_reviews = self.get_all_reviews()

        # Filtrer les reviews par l'ID du lieu
        return [review for review in all_reviews if review.place.id == place_id]

    def update_review(self, review_id, review_data):
        review = self.review_repo.get(review_id)
        if not review:
            raise ValueError("Review non trouvé.")

        # Mettre à jour les attributs de la review avec les nouvelles données
        for key, value in review_data.items():
            setattr(review, key, value)

        # Appeler la méthode update du dépôt avec l'ID et les données mises à jour
        self.review_repo.update(review, review_data)
        return review

    def delete_review(self, review_id):
        review = self.get_review(review_id)
        if not review:
            return False
        self.review_repo.delete(review_id)
        return True
