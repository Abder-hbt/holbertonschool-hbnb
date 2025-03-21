""" 
Initialisation et exécution de l'application Flask

Ce script crée une instance de l'application Flask et la démarre en mode debug 
si le script est exécuté directement.

Fonctions :
- create_app() : Fonction qui initialise et configure l'application Flask.

Objet :
- app : Instance de l'application Flask.

Exécution :
- Si le script est exécuté directement, l'application est démarrée en mode debug.
"""

from app import create_app

app = create_app()  #Crée une instance de l'application Flask

if __name__ == '__main__':
    app.run(debug=True)   #Démarre l'application en mode debug
