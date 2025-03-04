""" 
Configuration de l'application

Ce module définit les classes de configuration pour l'application, 
y compris la gestion de la clé secrète et le mode debug.

Classes :
- Config : Classe de configuration de base pour l'application.
- DevelopmentConfig : Classe de configuration pour l'environnement de développement.

Attributs de Config :
- SECRET_KEY : Clé secrète pour sécuriser les sessions, récupérée depuis les variables d'environnement 
  ou définie par défaut.
- DEBUG : Indicateur de mode debug, initialisé à False.

Dictionnaire :
- config : Dictionnaire qui mappe les environnements de configuration aux classes de configuration 
  correspondantes.
"""

import os

class Config:
    """ Classe de configuration de base pour l'application """
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')   #Clé secrète pour l'application """
    DEBUG = False # Indicateur de mode debug, par défaut désactivé """

class DevelopmentConfig(Config):
    """ Classe de configuration pour l'environnement de développement """
    DEBUG = True #Active le mode debug """

config = {
    'development': DevelopmentConfig,  """ Configuration pour l'environnement de développement """
    'default': DevelopmentConfig  # Configuration par défaut, utilisée en développement """
}
