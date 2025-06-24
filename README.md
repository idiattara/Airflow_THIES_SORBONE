---
## Démarrage rapide d'Airflow avec Docker et VS Code

Ce guide vous expliquera comment configurer Apache Airflow localement à l'aide de Docker et de Visual Studio Code.

### Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre machine :

* **Visual Studio Code (VS Code)** : Un éditeur de code léger et puissant.  
    * Télécharger ici : [https://code.visualstudio.com/download](https://code.visualstudio.com/download)

* **Docker Desktop** : Une application qui vous permet d'exécuter des conteneurs Docker sur votre système.  
    * Télécharger ici : [https://docs.docker.com/desktop/setup/install/windows-install/](https://docs.docker.com/desktop/setup/install/windows-install/)

### Étapes d'installation

1.  **Créez un nouveau projet dans VS Code.**

2.  **Créez un fichier `.env`** à la racine de votre projet et ajoutez les lignes suivantes :

    ```
    AIRFLOW_IMAGE_NAME=apache/airflow:2.4.2
    AIRFLOW_UID=50000
    ```

3.  **Enregistrez le fichier `docker-compose.yaml`** dans votre projet. Vous pouvez le télécharger depuis ce lien :  
    [https://github.com/idiattara/Airflow_THIES_SORBONE/blob/main/docker-compose.yaml](https://github.com/idiattara/Airflow_THIES_SORBONE/blob/main/docker-compose.yaml)

4.  **Ouvrez le terminal intégré de VS Code** (Terminal > Nouveau Terminal) et exécutez les commandes suivantes dans l'ordre :

    * Démarrez les services Docker en arrière-plan :  
        ```bash
        docker-compose up -d
        ```

    * Initialisez Airflow :  
        ```bash
        docker-compose up airflow-init
        ```

    * Initialisez la base de données Airflow :  
        ```bash
        docker-compose run --rm airflow-webserver airflow db init
        ```

5.  **Créez un utilisateur administrateur Airflow** avec la commande ci-dessous. Le mot de passe par défaut est `airflow airflow`.

    ```bash
    docker-compose run airflow-worker airflow users create --role Admin --username admin --email admin --firstname admin --lastname admin --password admin
    ```

Une fois toutes les étapes terminées, Airflow devrait être opérationnel. Vous pouvez accéder à l'interface utilisateur d'Airflow en ouvrant votre navigateur et en naviguant vers `http://localhost:8080` (si le port par défaut n'a pas été modifié). Utilisez les identifiants `admin` / `admin` pour vous connecter.
---
