Install Vscode 
https://code.visualstudio.com/download
Install Docker
https://docs.docker.com/desktop/setup/install/windows-install/

create a new file .env and add the following lines:

AIRFLOW_IMAGE_NAME=apache/airflow:2.4.2
AIRFLOW_UID=50000

save docker-compose.yaml file: https://airflow.apache.org/docs/apache-airflow/2.5.1/docker-compose.yaml
docker-compose up -d

docker-compose up airflow-init

docker-compose run --rm airflow-webserver airflow db init


create Admin user using below command:
 Mot de passe par defaut :  airflow airflow
docker-compose run airflow-worker airflow users create --role Admin --username admin --email admin --firstname admin --lastname admin --password admin




















