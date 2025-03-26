import re
from  app.models.base_model import BaseModel
from app import db, bcrypt



class User(BaseModel):
    # Représente un utilisateur de l'application
    __tablename__ = 'user'

    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    
    used_emails = set()  # Ensemble pour stocker les emails déjà utilisés 

    def __init__(self, first_name, last_name, email, password, is_admin=False):
        # Initialise un nouvel utilisateur avec des validations
        super().__init__()  # Appelle le constructeur de la classe parente 
        self.first_name = self.valide_name(first_name)  # Valide et assigne le prénom 
        self.last_name = self.valide_name(last_name)  # Valide et assigne le nom de famille 
        self.email = self.valide_email(email)  # Valide et assigne l'email 
        self.is_admin = is_admin  # Indique si l'utilisateur est un administrateur 
        self.places = []
        self.hash_password(password)

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
    
    def hash_password(self, password):
        """Hashes the password before storing it."""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """Verifies if the provided password matches the hashed password."""
        return bcrypt.check_password_hash(self.password, password)