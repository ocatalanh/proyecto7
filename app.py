from flask import Flask, request, jsonify
import pickle
from scripts.pipeline import tuberia_transform
import pandas as pd
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.preprocessing import StandardScaler, FunctionTransformer
from sklearn.decomposition import PCA
from typing import List
import numpy as np

# Importar las funciones auxiliares desde los scripts
from scripts.trad_columnas import trad_columnas
from scripts.remp_valores_binarios import reemplazar_valores_binarios
from scripts.one_hot_encoder import one_hot_encode_dataframe
from scripts.split_and_group import split_and_group
from scripts.traducir_respuestas import reemplazar

app = Flask(__name__)

@app.route('/predice', methods=['POST'])
def predict():
    # Obtener los datos JSON de la solicitud
    json = request.json
    query_df = pd.DataFrame([json])
  
    #n_components = 32  # Definir el número de componentes dentro de la función

    # Traducir columnas
    df = trad_columnas(query_df)
    
    # reemplazar respuestas
    df = reemplazar(df)
    # Eliminar columnas no deseadas
    df = df.drop(columns=['ProbabilidadLealtadLaboral', 'PaisActual', 'CodigoPostalActual'])
        
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
    
    
    
    
    # X_multivar = split_and_group(df, multivariables)
    # X = pd.concat([X, X_multivar], axis=1)
    
    

    # Estandarizar los datos
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # # Aplicar PCA
    # pca = PCA(n_components=n_components)
    # X_pca = pca.fit_transform(X_scaled)
    
    # return X_pca




####################################################









    #     # Cargar el modelo
    # with open(r'C:\Users\ocata\OneDrive\Desktop\Proyecto7_DS\models\mejor_rf_modelo.pickle', 'rb') as f:
    #     classifier = pickle.load(f)

    # # Realizar la predicción
    # prediction = classifier.predict(query)

    # #     # Devolver la respuesta basada en la predicción
    # if prediction[0] == 0:
    #     return "De ninguna forma, 3 años con un empleador es para volverse loco"
    # elif prediction[0] == 1:
    #     return "Eso sería difícil, pero si es la compañía correcta lo intentaría"
    # elif prediction[0] == 2:
    #     return "Trabajaría por 3 años o más"
    # else:
    #     return "Predicción no reconocida"
    #except Exception as e:
    #     return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)




@app.route("/")
def hello_world():
    return "<p>Hola Mundo Bienvenido a Machine Learning</p>"

if __name__ == "__main__":
    app.run(port=8000, debug=True)


