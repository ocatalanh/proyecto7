import pandas as pd

def reemplazar_valores_binarios(data: pd.DataFrame, col: str) -> pd.Series:
    """
    Reemplaza los valores binarios en una columna de un DataFrame de pandas.

    Parameters:
    data (pd.DataFrame): El DataFrame que contiene la columna a modificar.
    col (str): El nombre de la columna que contiene los valores binarios.

    Returns:
    pd.Series: La columna modificada con los valores binarios reemplazados.
    """
    if not isinstance(data, pd.DataFrame):
        raise TypeError("El argumento 'data' debe ser un DataFrame")

    if not isinstance(col, str):
        raise TypeError("El argumento 'col' debe ser una cadena de texto (str)")

    reemplazos = {
        'Yes': 1,
        'No': 0,
        'Will NOT work for them': 0,
        'Will work for them': 1,
    }

    # Realizar el reemplazo de valores
    data[col] = data[col].replace(reemplazos)
    return data[col]

        










