from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import os

# Fonction de traitement 1 : Lire et filtrer le CSV
def read_and_filter_csv(**kwargs):
    df = pd.read_csv('/opt/input.csv')
    
    # Filtrer les personnes de plus de 30 ans
    df_filtered = df[df['age'] > 30]
    
    # Enregistrer les données dans XCom
    kwargs['ti'].xcom_push(key='filtered_data', value=df_filtered.to_json())

# Fonction de traitement 2 : Ajouter une colonne
def add_column_to_data(**kwargs):
    # Récupérer les données de la tâche précédente depuis XCom
    ti = kwargs['ti']
    filtered_data_json = ti.xcom_pull(task_ids='read_and_filter_csv', key='filtered_data')
    df_filtered = pd.read_json(filtered_data_json)
    
    # Ajouter une nouvelle colonne 'age_above_30'
    df_filtered['age_above_30'] = df_filtered['age'] > 30
    
    # Enregistrer les données modifiées dans XCom
    kwargs['ti'].xcom_push(key='modified_data', value=df_filtered.to_json())

# Fonction de traitement 3 : Calculer des statistiques
def calculate_statistics(**kwargs):
    # Récupérer les données de la tâche précédente depuis XCom
    ti = kwargs['ti']
    modified_data_json = ti.xcom_pull(task_ids='add_column_to_data', key='modified_data')
    df_modified = pd.read_json(modified_data_json)
    
    # Calculer la moyenne d'âge
    avg_age = df_modified['age'].mean()
    
    # Ajouter la statistique dans XCom
    kwargs['ti'].xcom_push(key='avg_age', value=avg_age)

# Fonction de traitement 4 : Sauvegarder le fichier final
def save_final_file(**kwargs):
    # Récupérer les données de la tâche précédente depuis XCom
    ti = kwargs['ti']
    modified_data_json = ti.xcom_pull(task_ids='add_column_to_data', key='modified_data')
    df_modified = pd.read_json(modified_data_json)
    
    # Sauvegarder le fichier final
    # cp dags\input.csv  9e8a9eeb5a31:/opt
    df_modified.to_csv('/tmp/output.csv', index=False)

# Définir le DAG
dag = DAG(
    'multi_step_csv_processing_dag',
    description='DAG avec plusieurs étapes de traitement d\'un fichier CSV',
    schedule_interval='@daily',  # Tous les jours
    start_date=datetime(2025, 4, 1),
    catchup=False
)

# Tâches du DAG
task_1 = PythonOperator(
    task_id='read_and_filter_csv',
    python_callable=read_and_filter_csv,
    provide_context=True,
    dag=dag
)

task_2 = PythonOperator(
    task_id='add_column_to_data',
    python_callable=add_column_to_data,
    provide_context=True,
    dag=dag
)

task_3 = PythonOperator(
    task_id='calculate_statistics',
    python_callable=calculate_statistics,
    provide_context=True,
    dag=dag
)

task_4 = PythonOperator(
    task_id='save_final_file',
    python_callable=save_final_file,
    provide_context=True,
    dag=dag
)

# Définir l'ordre des tâches
task_1 >> task_2 >> task_3 >> task_4
