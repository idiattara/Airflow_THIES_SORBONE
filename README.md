# Installation et démarrage d'Airflow avec VSCode et Docker sur Windows

## Prérequis

- [Installer VSCode](https://code.visualstudio.com/download)
- [Installer Docker Desktop pour Windows](https://docs.docker.com/desktop/setup/install/windows-install/)

---

## Étapes d’installation

1. **Créer un nouveau projet dans VSCode**  
   Ouvre VSCode et crée un nouveau dossier pour ton projet Airflow.

2. **Créer un fichier `.env`**  
   Dans le dossier projet, crée un fichier `.env` et ajoute les lignes suivantes :

   ```env
   AIRFLOW_IMAGE_NAME=apache/airflow:2.4.2
   AIRFLOW_UID=50000
