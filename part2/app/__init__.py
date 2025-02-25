""" 
Initialisation de l'application Flask avec Flask-RESTx

Ce script définit une fonction pour créer une application Flask avec une API RESTx.

Fonctions :
- create_app() : Initialise et configure l'application Flask avec Flask-RESTx.

L'API est accessible avec la documentation Swagger à l'URL '/api/v1/'.
"""
from flask import Flask
from flask_restx import Api

def create_app():
    """ Crée et configure l'application Flask avec Flask-RESTx """
    app = Flask(__name__)  
    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API', doc='/api/v1/')
    
    return app
