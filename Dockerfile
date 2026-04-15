# Utilisation de l'image officielle Python comme base
FROM python:3.9

# Définition du répertoire de travail
WORKDIR /app

# Copie des fichiers de l'application dans l'image
COPY app.py /app/

# Installation des dépendances
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Exposition du port Flask
EXPOSE 5000

# Définition de la commande de lancement
CMD ["python", "app.py"]
