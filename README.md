# Introduction à OpenShift

Ce dépôt contient du contenu pédagogique pour apprendre les bases d'OpenShift, une plateforme Kubernetes d'entreprise développée par Red Hat.

## Prérequis
- Connaissance de base de Kubernetes et des conteneurs Docker
- OpenShift installé ou accès à un cluster OpenShift

## Installation
Pour une installation locale, vous pouvez utiliser Minishift.

```bash
minishift start


### 2. **`INSTALLATION.md`**
- Détaille le processus d'installation d'OpenShift, Minishift ou OKD (version open source).
- Peut inclure des instructions spécifiques pour différents systèmes d'exploitation (Linux, Mac, Windows).

**Contenu exemple :**
```markdown
# Installation d'OpenShift

Voici les étapes pour installer Minishift sur votre machine locale :

## 1. Prérequis
- VirtualBox ou KVM installé
- Git installé
- Docker installé

## 2. Installation de Minishift
### Sous Linux :
```bash
curl -LO https://github.com/minishift/minishift/releases/download/v1.34.3/minishift-1.34.3-linux-amd64.tgz
tar -xvzf minishift-1.34.3-linux-amd64.tgz
sudo mv minishift /usr/local/bin
