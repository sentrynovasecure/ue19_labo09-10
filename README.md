# ue19_labo09-10


# Utiliser une image de base Python
FROM python:3.8

# Définir le répertoire de travail dans le conteneur
WORKDIR /usr/src/app

# Copier les fichiers nécessaires dans le conteneur
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .

# Commande pour exécuter l'application
CMD [ "python", "./app.py" ]
