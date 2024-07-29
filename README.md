# Proyecto ETL datos climatico de la ciudad de Córdoba
![](https://github.com/Federicoleyria/dataproyect/blob/main/images/flojo-trabajo.PNG)
## Descripción
Proyecto Clima es una aplicación diseñada para recopilar y analizar datos climáticos de la ciudad de Córdoba utilizando la API de OpenWeatherMap. La aplicación está implementada en Python y orquestada con Apache Airflow para ejecutar tareas ETL (Extracción, Transformación y Carga) diariamente. Utiliza Docker para asegurar un entorno de ejecución consistente y manejable, y PostgreSQL como base de datos para almacenar los datos recopilados.

## Estructura del Proyecto
El proyecto contiene los siguientes archivos y directorios clave:

- `dags/`: Directorio que contiene el archivo `etl.py` con la lógica de ETL.
- `etl.py`: Archivo que contiene la lógica para extraer datos de la API, transformarlos y cargarlos en la base de datos.
- `dag.py`: Archivo que define el DAG (Grafo Acíclico Dirigido) en Airflow para orquestar la tarea ETL.
- `requirements.txt`: Lista de dependencias de Python necesarias para ejecutar la aplicación.
- `Dockerfile`: Instrucciones para construir la imagen Docker de la aplicación.
- `docker-compose.yaml`: Configuración para levantar un contenedor Docker con la aplicación y la base de datos PostgreSQL.
- `.gitignore`: Archivo que especifica qué archivos y directorios deben ser ignorados por Git.

## Configuración y Uso

### Prerrequisitos
- Docker y Docker Compose instalados en tu máquina.

### Instrucciones

1. Clonar el repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd ProyectoClima
Configurar el entorno de Docker:
Asegúrate de que los archivos docker-compose.yaml y Dockerfile estén en el directorio raíz del proyecto.

2. Construir y ejecutar la aplicación:
Ejecuta el siguiente comando para construir y levantar los contenedores Docker:

bash
Copiar código
docker-compose up --build
Acceder a la aplicación:

La interfaz web de Airflow debería estar disponible en http://localhost:8080.
Utiliza las credenciales por defecto airflow/airflow para iniciar sesión.
Verificar la ejecución del DAG:

Navega a la pestaña de DAGs en la interfaz web de Airflow.
Habilita y ejecuta el DAG fetch_weather_data.
Explicación del Código
etl.py
Este archivo contiene la lógica para extraer, transformar y cargar datos climáticos:

Extracción: Utiliza la API de OpenWeatherMap para obtener datos climáticos de Córdoba.
Transformación: Normaliza los datos JSON en un DataFrame de Pandas, añade columnas adicionales y realiza conversiones de temperatura de Kelvin a Celsius.
Carga: Conecta a una base de datos PostgreSQL y guarda los datos transformados en una tabla llamada weather_data.
dag.py
Este archivo define el DAG en Apache Airflow:

Configura las tareas con default_args para manejar los reintentos y los retrasos.
Define el DAG fetch_weather_data que se ejecuta diariamente.
Utiliza PythonOperator para ejecutar la función fetch_weather_data definida en etl.py.
docker-compose.yaml
Este archivo define los servicios Docker necesarios para ejecutar la aplicación:

PostgreSQL: Configura una base de datos PostgreSQL para almacenar los datos climáticos.
Airflow: Configura el servidor web de Airflow y el scheduler para orquestar las tareas ETL.
Volúmenes: Monta los directorios locales dags y logs dentro de los contenedores para facilitar el desarrollo y la persistencia de datos.
Dockerfile
Este archivo define el entorno de ejecución para la aplicación Airflow:

Utiliza apache/airflow:2.3.3 como imagen base.
Actualiza pip y instala las dependencias listadas en requirements.txt.
Contribuciones
Si deseas contribuir a este proyecto, por favor sigue estos pasos:

Haz un fork del repositorio.
Crea una rama con tu nueva característica (git checkout -b feature/nueva-caracteristica).
Haz commit de tus cambios (git commit -am 'Agrega nueva característica').
Haz push a la rama (git push origin feature/nueva-caracteristica).
Abre un Pull Request.
