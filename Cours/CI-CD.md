# CI/CD avec OpenShift

La CI/CD (Intégration Continue / Déploiement Continu) est un ensemble de pratiques qui permettent aux équipes de développement de livrer du code rapidement et en toute sécurité.

## Concepts clés :
- **Intégration Continue (CI)** : Processus qui consiste à intégrer régulièrement des modifications de code dans une branche principale et à valider automatiquement les builds via des tests automatisés.
- **Déploiement Continu (CD)** : Le déploiement continu prend les builds validés et les déploie automatiquement dans différents environnements (test, production).

## OpenShift et CI/CD
OpenShift propose des pipelines CI/CD intégrés avec Jenkins et peut automatiser l'intégration et le déploiement des applications conteneurisées.

### Outils :
- **Jenkins** : Principalement utilisé pour orchestrer les pipelines CI/CD.
- **OpenShift Pipelines (Tekton)** : Permet de créer des pipelines cloud-native pour gérer l'intégration et le déploiement continu.
