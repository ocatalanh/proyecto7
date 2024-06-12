import pandas as pd

def reemplazar(data: pd.DataFrame, col: str) -> pd.Series:
    """
    Reemplaza valores específicos en una columna de un DataFrame.

    Parameters:
    data (pd.DataFrame): El DataFrame que contiene la columna a modificar.
    col (str): El nombre de la columna en la cual se reemplazarán los valores.

    Returns:
    pd.Series: La columna del DataFrame con los valores reemplazados.
    """
    # Verificar los tipos de los argumentos
    if not isinstance(data, pd.DataFrame):
        raise TypeError("El primer argumento debe ser un DataFrame")
    if not isinstance(col, str):
        raise TypeError("El segundo argumento debe ser una cadena de texto (string)")

    reemplazos = {
        'Design and Creative strategy in any company': 'Estrategia de diseño y creatividad en cualquier empresa',
        'Look deeply into Data and generate insights': 'Analizar datos profundamente y generar insights',
        'Business Operations in any organization': 'Operaciones comerciales en cualquier organización',
        'Manage and drive End-to-End Projects or Products': 'Gestionar y dirigir proyectos o productos de principio a fin',
        'Build and develop a Team': 'Construir y desarrollar un equipo',
        'Teaching in any of the institutes/online or Offline': 'Enseñar en cualquier institución (en línea o presencial)',
        'Work as a freelancer and do my thing my way': 'Trabajar como freelancer y hacer las cosas a mi manera',
        'Design and Develop amazing software': 'Diseñar y desarrollar software increíble',
        'Become a content Creator in some platform': 'Convertirse en un creador de contenido en alguna plataforma',
        'Work in a BPO setup for some well known client': 'Trabajar en un centro de atención al cliente para algún cliente conocido',
        'Work with 5 to 6 people in my team': 'Trabajar con 5 a 6 personas en mi equipo',
        'Work with 2 to 3 people in my team': 'Trabajar con 2 a 3 personas en mi equipo',
        'Work alone': 'Trabajar solo',
        'Work with more than 10 people in my team': 'Trabajar con más de 10 personas en mi equipo',
        'Work with 7 to 10 or more people in my team': 'Trabajar con 7 a 10 o más personas en mi equipo'
    }

    # Verificar si la columna existe en el DataFrame
    if col not in data.columns:
        raise ValueError(f"La columna '{col}' no existe en el DataFrame.")

    # Reemplazar valores dentro de la columna `col` utilizando el diccionario
    data[col] = data[col].replace(reemplazos)
    
    return data[col]
