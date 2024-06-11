import pandas as pd
from sklearn.preprocessing import OneHotEncoder

def one_hot_encode_dataframe(data: pd.DataFrame) -> pd.DataFrame:
    """
    Aplica One-Hot Encoding a un DataFrame utilizando sklearn.preprocessing.OneHotEncoder.

    Parameters:
    data (pd.DataFrame): El DataFrame a transformar.

    Returns:
    pd.DataFrame: El DataFrame transformado con codificación One-Hot.
    """
    # Crear una instancia del transformador OneHotEncoder
    transformer = OneHotEncoder(sparse_output=False)

    # Aplicar OneHotEncoder y transformar los datos
    encoded_data = transformer.fit_transform(data)

    # Obtener los nombres de las columnas codificadas
    encoded_columns = transformer.get_feature_names_out(data.columns)

    # Crear un nuevo DataFrame con los datos codificados y los nombres de las columnas
    df_encoded = pd.DataFrame(encoded_data, columns=encoded_columns)

    return df_encoded
