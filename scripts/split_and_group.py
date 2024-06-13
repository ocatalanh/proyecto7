import pandas as pd
from typing import List

def split_and_group(data: pd.DataFrame, cols: List[str]) -> pd.DataFrame:
    final = pd.DataFrame()
    
    # Iterar sobre cada columna en la lista `cols`
    for col in cols:
           
        # Paso 1: Dividir la columna en múltiples columnas
        split_cols = data[col].str.split(', ', expand=True)
        
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