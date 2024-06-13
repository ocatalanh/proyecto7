import pandas as pd
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.preprocessing import StandardScaler, FunctionTransformer
from sklearn.decomposition import PCA
from typing import List

# Importar las funciones auxiliares desde los scripts
from scripts.trad_columnas import trad_columnas
from scripts.remp_valores_binarios import reemplazar_valores_binarios
from scripts.one_hot_encoder import one_hot_encode_dataframe
from scripts.split_and_group import split_and_group


def tuberia_transform(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transforma el DataFrame aplicando una serie de pasos, incluyendo traducción de columnas,
    reemplazo de valores binarios, codificación one-hot, división y agrupación de columnas,
    estandarización y PCA.

    Parameters:
    df (pd.DataFrame): El DataFrame de entrada.

    Returns:
    pd.DataFrame: El DataFrame transformado.
    """
    n_components = 32  # Definir el número de componentes dentro de la función

    # Traducir columnas
    df = trad_columnas(df)
    
    # Eliminar columnas no deseadas
    df = df.drop(columns=['ProbabilidadLealtadLaboral', 'PaisActual', 'CodigoPostalActual'])
    
    # Reemplazar valores binarios
    df['TrabajariaEmpresaMisionNoDefinida'] = reemplazar_valores_binarios(df, 'TrabajariaEmpresaMisionNoDefinida')
    df['ProbabilidadTrabajarMisionDesalineada'] = reemplazar_valores_binarios(df, 'ProbabilidadTrabajarMisionDesalineada')
    
    # Seleccionar columnas para X
    X = df[['TrabajariaEmpresaMisionNoDefinida', 'ProbabilidadTrabajarMisionDesalineada', 'ProbabilidadTrabajarSinImpactoSocial']]
    
    # Obtener dummies
    dummies = df[['Genero', 'FactoresInfluenciaCarrera', 'EducacionSuperiorExtranjero', 'EntornoTrabajoPreferido', 'EmpleadoresPreferidos', 'EntornoAprendizajePreferido', 'TipoGerentePreferido']]
    df_encoded = one_hot_encode_dataframe(dummies)
    
    # Concatenar X con dummies
    X = pd.concat([X, df_encoded], axis=1)
    
    # Manejar variables multivaluadas
    multivariables = ['CarreraAspiracional', 'ConfiguracionPreferida']
    X_multivar = split_and_group(df, multivariables)
    X = pd.concat([X, X_multivar], axis=1)
    
    # Estandarizar los datos
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Aplicar PCA
    pca = PCA(n_components=n_components)
    X_pca = pca.fit_transform(X_scaled)
    
    return X_pca


