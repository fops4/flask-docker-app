# ============================================================
#  HISTORIQUE DES COMMANDES — TP1 Docker (CC1 Keyce 2026)
#  Auteur : Fops
# ============================================================

# ── 0. Se placer dans le répertoire du projet ─────────────────
cd flask-docker-app

# ── 1. Construction de l'image Docker ─────────────────────────
docker build -t fops-flask-app .

# Vérifier que l'image a bien été créée
docker images | grep fops-flask-app

# ── 2. Lancement du conteneur en local ────────────────────────
docker run -d -p 5000:5000 --name fops-flask-container fops-flask-app

# Vérifier que le conteneur tourne
docker ps

# Accéder à l'application dans le navigateur :
#   http://localhost:5000

# ── 3. Consulter les logs du conteneur ────────────────────────
docker logs fops-flask-container

# ── 4. Publication sur Docker Hub ─────────────────────────────

# 4a. Se connecter à Docker Hub
docker login

# 4b. Tagger l'image avec votre nom d'utilisateur Docker Hub
docker tag fops-flask-app <votre_dockerhub_username>/fops-flask-app:latest

# 4c. Pousser l'image vers Docker Hub
docker push <votre_dockerhub_username>/fops-flask-app:latest

# ── 5. Commandes utiles de nettoyage ──────────────────────────

# Arrêter le conteneur
docker stop fops-flask-container

# Supprimer le conteneur
docker rm fops-flask-container

# Supprimer l'image localement
docker rmi fops-flask-app
