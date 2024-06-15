import pandas as pd
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.preprocessing import StandardScaler, FunctionTransformer
from sklearn.decomposition import PCA
from typing import List
import pickle

# Importar las funciones auxiliares desde los scripts
from scripts.trad_columnas import trad_columnas
from scripts.remp_valores_binarios import reemplazar_valores_binarios
from scripts.one_hot_encoder import one_hot_encode_dataframe
from scripts.split_and_group import split_and_group
from scripts.traducir_respuestas import reemplazar


def tuberia_transform(query_df: pd.DataFrame) -> pd.DataFrame:
    """
    Transforma el DataFrame aplicando una serie de pasos, incluyendo traducción de columnas,
    reemplazo de valores binarios, codificación one-hot, división y agrupación de columnas,
    estandarización y PCA.

    Parameters:
    df (pd.DataFrame): El DataFrame de entrada.

    Returns:
    pd.DataFrame: El DataFrame transformado.
    """
    df = trad_columnas(query_df)
    
    # reemplazar respuestas
    df = reemplazar(df)
    # Eliminar columnas no deseadas
    df = df.drop(columns=['PaisActual', 'CodigoPostalActual'])
        
    # # Reemplazar valores binarios
    df['TrabajariaEmpresaMisionNoDefinida'] = reemplazar_valores_binarios(df, 'TrabajariaEmpresaMisionNoDefinida')
    df['ProbabilidadTrabajarMisionDesalineada'] = reemplazar_valores_binarios(df, 'ProbabilidadTrabajarMisionDesalineada')
    
    # # Seleccionar columnas para X
    X = df[['TrabajariaEmpresaMisionNoDefinida', 'ProbabilidadTrabajarMisionDesalineada', 'ProbabilidadTrabajarSinImpactoSocial']]
        
    # # Obtener dummies
    dummies = df[['Genero', 'FactoresInfluenciaCarrera', 'EducacionSuperiorExtranjero', 'EntornoTrabajoPreferido', 'EmpleadoresPreferidos', 'EntornoAprendizajePreferido', 'TipoGerentePreferido']]
    df_encoded = one_hot_encode_dataframe(dummies)
    
    # Concatenar X con dummies
    X = pd.concat([X, df_encoded], axis=1)
    
    # Manejar variables multivaluadas
    multivariables = ['CarreraAspiracional', 'ConfiguracionPreferida']
    
    data_split = split_and_group(df,multivariables)
    
    X = pd.concat([X, data_split], axis=1)
    
    with open(r'C:\Users\ocata\OneDrive\Desktop\Proyecto7_DS\models\escalador.pkl', 'rb') as file:
        scaler = pickle.load(file)

    X_scaled = scaler.transform(X)

    with open(r'C:\Users\ocata\OneDrive\Desktop\Proyecto7_DS\models\pca.pkl', 'rb') as file:
        pca = pickle.load(file)    

    X_pca = pca.transform(X_scaled)
 
    # Cargar el modelo
    with open(r'C:\Users\ocata\OneDrive\Desktop\Proyecto7_DS\models\mejor_rf_modelo.pkl', 'rb') as f:
         classifier = pickle.load(f)

    # Realizar la predicción
    prediction = classifier.predict(X_pca)

    return prediction
    


