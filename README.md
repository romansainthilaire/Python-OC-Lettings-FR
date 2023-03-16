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

## Linting et tests
- vérification de la qualité du code : flake8
- exécution des tests : pytest

## Lancement de l'application
- activer l'environnement virtuel : [nom]\Scripts\activate
- lancer le serveur de développement : python manage.py runserver
- se rendre à l'adresse : http://127.0.0.1:8000/

## Accès au site d'administration
- URL : http://localhost:8000/admin
- utilisateur : "admin"
- mot de passe : "Abc1234!"

## Lancement de l'application avec Docker
- création de l'image docker : docker-compose build
- lancer l'application : docker-compose up
- se rendre à l'adresse : http://127.0.0.1:8000/

## Lancement de l'application à partir d'une image Docker stockée sur un dépôt DockerHub
- le nom du dépôt DockerHub est : romansainthilaire/oc_lettings_site
- récupérer l'image en spécifiant son label : docker pull romansainthilaire/oc_lettings_site:[label]
- lancer l'application : docker run -p 8000:8000 romansainthilaire/oc_lettings_site:[label]
- se rendre à l'adresse : http://127.0.0.1:8000/

## Pipeline CI/CD : CircleCI
Le pipeline CI/CD défini dans le fichier config.yml exécute trois travails.

### 1. Linting et lancement des tests
Ce travail s'effectue automatiquement lorsqu'un commit est effectué.
- Installation des packages
- Vérification du code avec Flake8
- Exécution des tests avec Pytest

### 2. Création d'une image Docker et chargement sur DockerHub
Ce travail s'effectue automatiquement lorsqu'un commit est effectué sur la branche *master*.
- Création d'une image Docker
- Chargement de l'image sur DockerHub

### 3. Déploiement de l'applcation sur Heroku
Ce travail s'effectue automatiquement lorsqu'un commit est effectué sur la branche *master*.
- Déploiement du site sur Heroku
- Création du superutilisateur admin (si il n'existe pas déjà)
