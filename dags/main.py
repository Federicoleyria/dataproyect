from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import timedelta  # Asegúrate de importar timedelta
from dags.etl import fetch_weather_data

# Define default arguments
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'fetch_weather_data',
    default_args=default_args,
    description='Un DAG para importar datos del clima',
    schedule_interval='@daily',  # Ejecuta diariamente
    start_date=days_ago(1),
)

# Define the PythonOperator
fetch_weather_data_task = PythonOperator(
    task_id='fetch_weather_data_task',
    python_callable=fetch_weather_data,
    dag=dag,
)
