# Définition de la classe User

# Ce module définit la classe `User`, qui représente un utilisateur de l'application. 
# Elle hérite de `BaseModel` et inclut des validations pour les attributs de l'utilisateur.

# Classes :
# - User : Représente un utilisateur avec des attributs et des validations.

# Attributs :
# - used_emails : Ensemble pour stocker les emails utilisés, afin d'éviter les doublons.
# - first_name : Prénom de l'utilisateur, validé à une longueur maximale de 50 caractères.
# - last_name : Nom de famille de l'utilisateur, validé à une longueur maximale de 50 caractères.
# - email : Adresse email de l'utilisateur, validée pour respecter un format correct et l'unicité.
# - is_admin : Indicateur si l'utilisateur est un administrateur (valeur par défaut : False).

# Méthodes :
# - __init__(first_name, last_name, email, is_admin=False) : Constructeur qui initialise les attributs de l'utilisateur.
# - valide_name(name) : Valide que le nom n'excède pas 50 caractères et lève une exception si c'est le cas.
# - valide_email(email) : Valide le format de l'email, vérifie son unicité, et lève une exception si l'email est invalide ou déjà utilisé.

import re
from models.base_model import BaseModel

class User(BaseModel):
    # Représente un utilisateur de l'application
    
    used_emails = set()  # Ensemble pour stocker les emails déjà utilisés 

    def __init__(self, first_name, last_name, email, is_admin=False):
        # Initialise un nouvel utilisateur avec des validations
        super().__init__()  # Appelle le constructeur de la classe parente 
        self.first_name = self.valide_name(first_name)  # Valide et assigne le prénom 
        self.last_name = self.valide_name(last_name)  # Valide et assigne le nom de famille 
        self.email = self.valide_email(email)  # Valide et assigne l'email 
        self.is_admin = is_admin  # Indique si l'utilisateur est un administrateur 

    def valide_name(self, name):
        # Valide que le nom ne dépasse pas 50 caractères
        if len(name) > 50:
            raise ValueError("Seulement 50 caractères sont autorisés")
        return name

    def valide_email(self, email):
        # Valide le format de l'email et assure son unicité
        if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
            raise ValueError("Email invalide")
        if email in User.used_emails:
            raise ValueError("Cet Email est déjà utilisé")
        User.used_emails.add(email)  # Ajoute l'email à l'ensemble des emails utilisés 
        return email
