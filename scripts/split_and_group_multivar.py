import pandas as pd
from typing import List
from scripts.remp_valores_col_multivar import reemplazar


def multi_var(data: pd.DataFrame, cols: List[str]) -> pd.DataFrame:
    """
    Transforma columnas de un DataFrame que contienen valores separados por comas 
    en múltiples columnas con variables dummy.

    Parameters:
    data (pd.DataFrame): El DataFrame de entrada.
    cols (List[str]): Lista de nombres de las columnas a transformar.

    Returns:
    pd.DataFrame: Un DataFrame con las nuevas variables dummy.
    """
    if not isinstance(data, pd.DataFrame):
        raise TypeError("El primer argumento debe ser un DataFrame")
    if not isinstance(cols, list) or not all(isinstance(col, str) for col in cols):
        raise TypeError("El segundo argumento debe ser una lista de cadenas de texto (strings)")

    final = pd.DataFrame()
    
    # Iterar sobre cada columna en la lista `cols`
    for col in cols:
        # Reemplazar valores en la columna antes de dividir
        data[col] = reemplazar(data, col)
        
        # Paso 1: Dividir la columna en múltiples columnas
        split_cols = data[col].str.split(',  ', expand=True)
        
        # Paso 2: Renombrar las columnas resultantes
        split_cols.columns = [f'{col}_var_{i+1}' for i in range(split_cols.shape[1])]
        
        # Paso 3: Crear variables dummies para cada columna dividida
        stack = split_cols.stack()
        dummies = pd.get_dummies(stack)
        dummies_group = dummies.groupby(level=0).sum()
        
        # Renombrar las columnas dummies
        dummies_group.columns = [f'{col}_{dummy_col}' for dummy_col in dummies_group.columns]
        
        # Concatenar al DataFrame final
        final = pd.concat([final, dummies_group], axis=1)
    
    return final