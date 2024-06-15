import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import pickle

def one_hot_encode_dataframe(data: pd.DataFrame) -> pd.DataFrame:
    """
    Aplica One-Hot Encoding a un DataFrame utilizando sklearn.preprocessing.OneHotEncoder.

    Parameters:
    data (pd.DataFrame): El DataFrame a transformar.

    Returns:
    pd.DataFrame: El DataFrame transformado con codificación One-Hot.
    """
    
     # Cargar el OneHotEncoder entrenado
    with open(r'C:\Users\ocata\OneDrive\Desktop\Proyecto7_DS\models\onehot_encoder.pkl', 'rb') as f:
        transformador = pickle.load(f)
    
    # Aplicar el OneHotEncoder a los datos nuevos
    encoded_data = transformador.transform(data)

    encoded_columns = transformador.get_feature_names_out(data.columns)
    
    df_encoded = pd.DataFrame(encoded_data, columns=encoded_columns)


    return df_encoded
