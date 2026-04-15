# 🐳 fops-flask-app — TP1 Docker

Application Flask conteneurisée avec Docker, développée dans le cadre du **CC1 — Conduite de Projet (Agile, DevOps, Kanban)** à **Keyce Informatique & IA**.

## 📁 Structure du projet

```
flask-docker-app/
├── app.py              # Application Flask (frontend intégré)
├── requirements.txt    # Dépendances Python
├── Dockerfile          # Instructions de build Docker
├── commands_history.sh # Historique des commandes exécutées
└── README.md
```

## 🚀 Lancer l'application

### En local (sans Docker)
```bash
pip install flask
python app.py
```

### Avec Docker
```bash
# Build
docker build -t fops-flask-app .

# Run
docker run -d -p 5000:5000 --name fops-flask-container fops-flask-app
```

Accéder à : **http://localhost:5000**

## 🐋 Image Docker Hub

```
docker pull <votre_dockerhub_username>/fops-flask-app:latest
```

## 👤 Auteur

**Fops** — DSI, Matrix Télécoms / GFC S.A.  
Keyce Informatique & IA — 2026
