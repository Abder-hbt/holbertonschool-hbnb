# Définition de la classe Place

# Ce module définit la classe `Place`, qui représente un lieu dans l'application.
# Elle hérite de `BaseModel` et inclut des validations pour les attributs du lieu 
# ainsi que la géocodification de l'adresse fournie.

# Classes :
# - Place : Représente un lieu avec des attributs tels que le titre, la description, 
#   le prix, l'adresse et le propriétaire, ainsi que des validations et des méthodes 
#   pour la géocodification.

# Attributs :
# - title : Titre du lieu, validé à une longueur maximale de 100 caractères.
# - description : Description du lieu.
# - price : Prix du lieu, validé pour être supérieur ou égal à 0.
# - address : Adresse du lieu, utilisée pour la géocodification.
# - owner : Propriétaire du lieu, validé pour être une instance de `User`.
# - latitude : Latitude du lieu, obtenue par géocodification de l'adresse.
# - longitude : Longitude du lieu, obtenue par géocodification de l'adresse.

# Méthodes :
# - __init__(title, description, price, address, owner) : Constructeur qui initialise
#   les attributs du lieu et effectue des validations.
# - valide_title(title) : Valide que le titre n'excède pas 100 caractères.
# - valide_price(price) : Valide que le prix est supérieur ou égal à 0.
# - is_owner(owner) : Valide que le propriétaire est une instance de `User`.
# - geocode_address(address) : Obtient la latitude et la longitude de l'adresse
#   en effectuant une requête à l'API de géocodage.
# - valide_latitude(latitude) : Valide et corrige la latitude dans les limites acceptables.
# - valide_longitude(longitude) : Valide et corrige la longitude dans les limites acceptables.

import requests
from models.base_model import BaseModel
from models.user import User

class Place(BaseModel):
    # Représente un lieu dans l'application

    def __init__(self, title, description, price, address, owner):
        # Initialise un nouvel objet Place avec des validations
        super().__init__()  # Appelle le constructeur de la classe parente
        self.title = self.valide_title(title)  # Valide et assigne le titre
        self.description = description  # Assigne la description
        self.price = self.valide_price(price)  # Valide et assigne le prix
        self.address = address  # Assigne l'adresse
        self.owner = self.is_owner(owner)  # Valide et assigne le propriétaire

        # Effectue la géocodification de l'adresse pour obtenir la latitude et la longitude
        self.latitude, self.longitude = self.geocode_address(address)
        self.latitude = self.valide_latitude(self.latitude)  # Valide la latitude
        self.longitude = self.valide_longitude(self.longitude)  # Valide la longitude

    def valide_title(self, title):
        # Valide que le titre ne dépasse pas 100 caractères
        if len(title) > 100:
            raise ValueError("Seulement 100 caractères sont autorisés")
        return title

    def valide_price(self, price):
        # Valide que le prix est supérieur ou égal à 0
        if float(price) < 0:
            raise ValueError("Veuillez saisir une valeur égale ou supérieure à 0")
        return price
    
    def is_owner(self, owner):
        # Valide que le propriétaire est une instance de User
        if not isinstance(owner, User):
            raise ValueError("Le propriétaire doit être une instance de User")
        return owner

    def geocode_address(self, address):
        # Effectue une requête pour obtenir les coordonnées de l'adresse
        url = "https://nominatim.openstreetmap.org/search"
        params = {
            "q": address,
            "format": "json"
        }
        response = requests.get(url, params=params)

        # Vérifie la réponse et retourne la latitude et la longitude
        if response.status_code == 200:
            data = response.json()
            if data:
                latitude = float(data[0]["lat"])
                longitude = float(data[0]["lon"])
                return latitude, longitude
            else:
                raise ValueError("Aucune coordonnée trouvée pour l'adresse donnée")
        else:
            raise ValueError("Erreur lors de la requête à Nominatim")

    def valide_latitude(self, latitude):
        # Valide et corrige la latitude
        corrected_latitude = max(-90, min(90, float(latitude)))
        if corrected_latitude != float(latitude):
            print("Attention : La latitude saisie était hors limites", corrected_latitude)
        return corrected_latitude

    def valide_longitude(self, longitude):
        # Valide et corrige la longitude
        corrected_longitude = max(-180, min(180, float(longitude)))
        if corrected_longitude != float(longitude):
            print("Attention : La longitude saisie était hors limites", corrected_longitude)
        return corrected_longitude
