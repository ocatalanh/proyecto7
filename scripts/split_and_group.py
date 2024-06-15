import pandas as pd
from typing import List
import pickle

def split_and_group(new_df: pd.DataFrame, multivariables: List[str]) -> pd.DataFrame:
    
    with open(r'C:\Users\ocata\OneDrive\Desktop\Proyecto7_DS\models\onehot_encoder_multi_var.pkl', 'rb') as file:
        encoders = pickle.load(file)

        # Preparar una lista para almacenar las columnas codificadas de los nuevos datos
    new_encoded_list = []

        #   Iterar sobre cada columna en la lista `multivariables`
    for col in multivariables:
        # Dividir la columna en múltiples columnas
        split_cols = new_df[col].str.split(', ', expand=True)
    
        # Recuperar el encoder entrenado para esta columna
        encoder = encoders[col]
    
        # Transformar las subcolumnas utilizando el encoder ya entrenado
        encoded_cols = encoder.transform(split_cols.stack().values.reshape(-1, 1))
    
        # Crear un DataFrame con las columnas codificadas
        encoded_df = pd.DataFrame.sparse.from_spmatrix(
            encoded_cols, 
            columns=[f'{col}_{name}' for name in encoder.get_feature_names_out()]
        )
    
        # Sumar las columnas codificadas para cada fila original
        summed_encoded_df = encoded_df.groupby(encoded_df.index // split_cols.shape[1]).sum()
    
        # Agregar al DataFrame final
        new_encoded_list.append(summed_encoded_df.reset_index(drop=True))

    # Concatenar todos los DataFrames de las columnas codificadas de los nuevos datos
    new_final = pd.concat(new_encoded_list, axis=1)

    # Reemplazar '_x0_' en los nombres de las columnas en el DataFrame final
    new_final.columns = new_final.columns.str.replace('_x0_', '_')

    return new_final