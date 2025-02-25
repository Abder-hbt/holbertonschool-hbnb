""" 
Initialisation de la facade HBnB

Ce script crée une instance de la facade HBnB, qui centralise l'accès aux services 
de gestion des données de l'application HBnB.

Classes :
- HBnBFacade : Classe qui gère les interactions avec les repositories.

Objet :
- facade : Instance de la facade HBnB pour gérer les utilisateurs, les lieux, 
  les avis et les commodités.
"""

from app.services.facade import HBnBFacade

facade = HBnBFacade()  """ Crée une instance de la facade HBnB """
