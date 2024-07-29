# Proyecto Clima
![]([https://github.com/Federicoleyria/dataproyect/images/flojo-trabajo.PNG])
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

1. **Clonar el repositorio:**
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd ProyectoClima
