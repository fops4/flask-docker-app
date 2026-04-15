# ⚙️ Dossier Jenkins — TP2 CI/CD

Pipeline Jenkins automatisant le build et la publication de l'image Docker Flask.

## 📁 Contenu

```
jenkins/
├── Jenkinsfile        # Script du pipeline CI/CD
└── README.md          # Ce fichier
```

---

## 🔄 Étapes du pipeline

```
┌─────────────────────────────────────────────────────────┐
│                    PIPELINE JENKINS                     │
├──────────────┬──────────────────┬───────────────────────┤
│  1. Clonage  │   2. Image       │   3. Publication      │
│              │                  │                       │
│  git clone   │  docker build    │  docker tag           │
│  GitHub repo │  -t fops-flask   │  docker push          │
│              │  -app .          │  → Docker Hub         │
└──────────────┴──────────────────┴───────────────────────┘
```

---

## 🛠️ Configuration Jenkins (étapes préalables)

### 1. Ajouter les credentials Docker Hub

Dans Jenkins :
```
Manage Jenkins → Credentials → System → Global credentials
  → Add Credentials
      Kind     : Username with password
      Username : <votre_username_dockerhub>
      Password : <votre_token_dockerhub>
      ID       : dockerhub-credentials      ← doit correspondre au Jenkinsfile
```

> 💡 Utiliser un **Access Token** Docker Hub (pas votre mot de passe) :
> Docker Hub → Account Settings → Security → New Access Token

### 2. Mettre à jour les variables dans le Jenkinsfile

```groovy
DOCKERHUB_USERNAME = "fops"           // ← votre username Docker Hub
GITHUB_REPO        = "https://github.com/<username>/flask-docker-app.git"
```

### 3. Créer le pipeline dans Jenkins

```
New Item → Pipeline
  → Pipeline script from SCM
      SCM           : Git
      Repository URL: <votre_repo_github>
      Branch        : */main
      Script Path   : jenkins/Jenkinsfile
```

---

## ▶️ Lancer le pipeline

```
Dashboard → votre_pipeline → Build Now
```

---

## 📋 Résultat attendu

```
Stage View :
┌──────────┬─────────┬─────────────┐
│ Clonage  │  Image  │ Publication │
│   ✅     │   ✅    │     ✅      │
└──────────┴─────────┴─────────────┘
BUILD SUCCESS
```

---

## 👤 Auteur

**Fops** — Keyce Informatique & IA — CC1 DevOps 2026
