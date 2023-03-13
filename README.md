# OC Lettings

Ce projet a été réalisé dans le cadre de la formation OpenClassrooms *Développeur d'application - Python*.

→ Mise à l'échelle d'une application Django :
- Refonte de l'architecture modulaire
- Implémentation de tests unitaires
- Création d'un pipeline CI/CD

## Présentation de l'application
*L'application requiert un interpréteur Python, version 3.6 ou supérieure.*

Le projet initial a été cloné depuis le dépôt suivant : https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR

*Orange County Lettings* est une start-up fictive dans le secteur de la location de biens immobiliers.
L'application permet de lister et d'afficher le détail de profils utilisateurs et de biens immobiliers.

## Installation
- créer un environnement virtuel : python -m venv [nom]
- activer l'environnement virtuel : [nom]\Scripts\activate
- installer les packages : pip install -r requirements.txt

## Lancement de l'application
- activer l'environnement virtuel : [nom]\Scripts\activate
- lancer le serveur de développement : python manage.py runserver
- se rendre à l'adresse : http://127.0.0.1:8000/

## Accès au site d'administration
- URL : http://localhost:8000/admin
- utilisateur : "admin"
- mot de passe : "Abc1234!"

## Linting & Tests unitaires
- activer l'environnement virtuel : [nom]\Scripts\activate
- scanner le code : flake8
- exécuter les tests : pytest
