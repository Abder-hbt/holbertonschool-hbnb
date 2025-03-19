import requests
from app.models.base_model import BaseModel
from app.models.user import User

class Place(BaseModel):
    """Représente un lieu dans l'application."""

    def __init__(self, title: str, description: str, price: float, address: str, owner: User, amenities: str):
        """Initialise un nouvel objet Place avec des validations et du géocodage."""
        super().__init__()
        self.title = self.validate_title(title)
        self.description = description
        self.price = self.validate_price(price)
        self.address = address
        self.owner = self.validate_owner(owner)
        self.amenities = amenities
        self.reviews = []

        # Géocodage de l'adresse
        try:
            self.latitude, self.longitude = self.geocode_address(address)
        except Exception as e:
            print(f"⚠️ Géocodage échoué : {e}")
            self.latitude, self.longitude = 0.0, 0.0  # Valeurs par défaut

        self.latitude = self.validate_latitude(self.latitude)
        self.longitude = self.validate_longitude(self.longitude)

    def validate_title(self, title: str) -> str:
        """Valide que le titre ne dépasse pas 100 caractères."""
        if len(title.strip()) > 100:
            raise ValueError("Le titre ne peut pas dépasser 100 caractères.")
        return title.strip()

    def validate_price(self, price: float) -> float:
        """Valide que le prix est un nombre positif."""
        price = float(price)
        if price < 0:
            raise ValueError("Le prix doit être supérieur ou égal à 0.")
        return price

    def validate_owner(self, owner):
        """Valide que le propriétaire est bien une instance de User."""
        if not isinstance(owner, User):
            raise ValueError("Le propriétaire doit être une instance de User.")
        return owner
    
    def add_review(self, review):
        """Ajoute une review à la liste des reviews du lieu."""
        self.reviews.append(review)

    def geocode_address(self, address: str) -> tuple[float, float]:
        """Utilise l'API Nominatim pour obtenir la latitude et la longitude d'une adresse."""
        try:
            response = requests.get(
                "https://nominatim.openstreetmap.org/search",
                params={"q": address, "format": "json"},
                headers={"User-Agent": "hbnb-app"}
            )
            response.raise_for_status()  # Lève une erreur si le statut HTTP n'est pas 200

            data = response.json()
            if not data:
                raise ValueError(f"Aucune donnée trouvée pour l'adresse : {address}")

            return float(data[0]["lat"]), float(data[0]["lon"])
        
        except requests.RequestException as e:
            raise RuntimeError(f"Erreur de connexion à l'API de géocodage : {e}")

    def validate_latitude(self, latitude: float) -> float:
        """Valide et corrige la latitude si nécessaire."""
        latitude = float(latitude)
        if latitude < -90 or latitude > 90:
            raise ValueError(f"Latitude invalide : {latitude}. Elle doit être entre -90 et 90.")
        return latitude

    def validate_longitude(self, longitude: float) -> float:
        """Valide et corrige la longitude si nécessaire."""
        longitude = float(longitude)
        if longitude < -180 or longitude > 180:
            raise ValueError(f"Longitude invalide : {longitude}. Elle doit être entre -180 et 180.")
        return longitude
    
