# OC Lettings

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![CircleCI](https://img.shields.io/badge/circle%20ci-%23161616.svg?style=for-the-badge&logo=circleci&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)

Ce projet a été réalisé dans le cadre de la formation OpenClassrooms *Développeur d'application - Python*.

→ Mise à l'échelle d'une application *Django* :
- Refonte de l'architecture modulaire
- Implémentation de tests unitaires avec *Pytest*
- Création d'un pipeline CI/CD avec *Docker* et *CircleCI*
- Journalisation via *Sentry*

## Présentation de l'application
Note : l'application requiert un interpréteur Python, version 3.6 ou supérieure.

Le projet initial a été cloné depuis le dépôt suivant : https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR

*Orange County Lettings* est une start-up fictive dans le secteur de la location de biens immobiliers.
L'application permet de lister et d'afficher le détail de profils utilisateurs et de biens immobiliers.

## Installation
- créer un environnement virtuel : python -m venv [nom]
- activer l'environnement virtuel : [nom]\Scripts\activate
- installer les packages : pip install -r requirements.txt

## Linting & Tests
- vérifier la qualité du code : flake8
- exécuter les tests unitaires : pytest

## Lancement de l'application
- activer l'environnement virtuel : [nom]\Scripts\activate
- lancer le serveur de développement : python manage.py runserver
- se rendre à l'adresse : http://127.0.0.1:8000/

## Accès au site d'administration
- URL : http://127.0.0.1:8000/admin
- utilisateur : admin
- mot de passe : Abc1234!

## Lancement de l'application avec *Docker*
- créer l'image *Docker* : docker-compose build
- lancer l'application : docker-compose up
- se rendre à l'adresse : http://127.0.0.1:8000/

## Lancement de l'application à partir d'un dépôt *DockerHub*
Le nom du dépôt *DockerHub* est : romansainthilaire/oc_lettings_site
- récupérer l'image *Docker* en spécifiant son label : docker pull romansainthilaire/oc_lettings_site:[label]
- lancer l'application : docker run -p 8000:8000 romansainthilaire/oc_lettings_site:[label]
- se rendre à l'adresse : http://127.0.0.1:8000/

## Pipeline CI/CD

Le pipeline CI/CD a été construit avec *CircleCI*. Il permet, entre autres, d'automatiser le déploiement du site sur *Heroku*. 
Afin que le pipeline fonctionne correctement les variables d'environnement suivantes doivent être définies dans *CircleCI* :
- HEROKU_APP_NAME : le nom de l'application *Heroku*
- HEROKU_API_KEY : la clé API que l'on peut trouver dans les paramètres utilisateur du compte *Heroku*
- DOCKERHUB_USERNAME : le nom d'utilisateur du compte *DockerHub*
- DOCKERHUB_PASSWORD : le mot de passe du compte *DockerHub*
- SUPERUSER_USERNAME : le nom d'utilisateur de l'administrateur du site
- SUPERUSER_PASSWORD : le mot de passe de l'administrateur du site

Par ailleurs, une fois l'application crée sur *Heroku* il est nécessaire de définir les variables de configuration suivantes (dans *Settings* > *Config Vars*) :
- SECRET_KEY : clé générée aléatoirement (en utilisant par exemple : https://djecrety.ir/)
- DEBUG : 0 pour False
- ALLOWED_HOSTS : [nom application].herokuapp.com
- SENTRY_DSN : clé liée au projet *Sentry* (dans *Settings* > *Client Keys (DSN)*)

Le pipeline CI/CD exécute trois travaux décrits ci-après. Le travail n°1 s'effectue à chaque commit, quel que soit la branche affectée. Les travaux n°2 et n°3 s'effectuent uniquement lorsque le commit est réalisé sur la branche *master*. Par ailleurs, un travail n'est effectué que si le travail précédent est réalisé avec succès.

### Travail n°1 - Linting et lancement des tests
- Installation des packages définis dans le fichier *requirements.txt*
- Vérification du code avec *Flake8*
- Exécution des tests unitaires avec *Pytest*

### Travail n°2 - Création d'une image *Docker* et chargement sur *DockerHub*
- Création d'une image *Docker*
- Chargement de l'image sur *DockerHub*

### Travail n°3 - Déploiement de l'application sur *Heroku*
- Déploiement du site sur *Heroku*
- Création du super utilisateur admin (s'il n'existe pas déjà)