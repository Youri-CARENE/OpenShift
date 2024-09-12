# Dockerfile

# Utiliser une image Python officielle
FROM python:3.8-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le code source dans le conteneur
COPY src/ /app/src/

# Installer Flask
RUN pip install flask

# Exposer le port 8080 pour Flask
EXPOSE 8080

# Lancer l'application Flask
CMD ["python", "/app/src/app.py"]