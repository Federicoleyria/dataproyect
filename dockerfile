FROM apache/airflow:2.3.3

USER airflow

# Actualiza pip
RUN pip install --upgrade pip

# Instala paquetes adicionales
COPY requirements.txt .
RUN pip install -r requirements.txt

