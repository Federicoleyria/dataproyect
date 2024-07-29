import pandas as pd
import requests
from pandas import json_normalize
from sqlalchemy import create_engine

def fetch_weather_data():
    api_key = '747e70cf6b39240f7d2fff46a326d781'
    city = 'Cordoba'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    
    # Normalizar datos de 'weather' y 'main'
    weather_df = json_normalize(data['weather'])
    main_df = json_normalize(data['main'])
    
    # Añadir columnas adicionales
    main_df['Ciudad'] = city
    main_df['coord_lon'] = data['coord']['lon']
    main_df['coord_lat'] = data['coord']['lat']
    main_df['Visibilidad'] = data['visibility']
    main_df['Velocidad del viento'] = data['wind']['speed']
    main_df['Fecha'] = pd.to_datetime(data['dt'], unit='s')
    main_df['Pais'] = data['sys']['country']
    
    # Unir los DataFrames
    df = pd.concat([weather_df, main_df], axis=1)
    
    # Eliminar columnas no deseadas (verifica si realmente existen)
    columns_to_drop = ['id', 'description', 'icon', 'main', 'sea_level', 'grnd_level']
    df = df.drop(columns=[col for col in columns_to_drop if col in df.columns], errors='ignore')
    
    # Renombrar columnas y convertir temperaturas de Kelvin a Celsius
    df.rename(columns={
        'temp': 'Temperatura',
        'feels_like': 'Sensacion',
        'pressure': 'Presion',
        'humidity': 'Humedad'
    }, inplace=True)
    
    # Conversión de temperaturas
    df['Temperatura'] = (df['Temperatura'] - 273.15).round(2)
    df['Sensacion'] = (df['Sensacion'] - 273.15).round(2)
    df['temp_min'] = (df['temp_min'] - 273.15).round(2)
    df['temp_max'] = (df['temp_max'] - 273.15).round(2)
    
    # Agregar una columna de ID manualmente
    df['id'] = range(1, len(df) + 1)
    
    # Conectar a la base de datos PostgreSQL
    engine = create_engine('postgresql+psycopg2://airflow:airflow@postgres/airflow')
    
    # Importar DataFrame a la base de datos (añadir datos sin reemplazar)
    df.to_sql('weather_data', engine, if_exists='append', index=False)
    
    print("Datos importados exitosamente")    

fetch_weather_data()
