# ue19_labo09-10


ue19_labo09-10
À propos

Ce repository contient une application Python simple qui interroge le service d'API public PunAPI pour afficher un jeu de mots aléatoire. Cette application est un exemple basique d'utilisation de l'API REST avec Python.
Prérequis

Pour exécuter cette application, vous aurez besoin de Python 3 et de pip, le gestionnaire de paquets Python.
Installation

    Clonez le repository sur votre machine locale :

    bash

git clone https://github.com/blackfeeather/ue19_labo09-10.git
cd ue19_labo09-10

Installez les dépendances nécessaires :

    pip install -r requirements.txt

Utilisation

Pour lancer l'application, exécutez :

python app.py

L'application affichera un jeu de mots aléatoire récupéré depuis PunAPI.
Docker

Cette application peut également être exécutée dans un conteneur Docker.

    Construisez l'image Docker à partir du Dockerfile :

docker build -t ue19_labo09-10 .

Une fois l'image construite, lancez le conteneur :

arduino

    docker run ue19_labo09-10

Contribution

Les contributions à ce projet sont les bienvenues. Veuillez suivre les bonnes pratiques de développement et de documentation.

Licence

[Nel]
