from flask import Flask, request
from scripts.pipeline import tuberia_transform
import pandas as pd

app = Flask(__name__)

@app.route('/predice', methods=['POST'])
def predict():
    # Obtener los datos JSON de la solicitud
    json = request.json
    query_df = pd.DataFrame([json])
  
    prediction = tuberia_transform(query_df)

    # Devolver la respuesta basada en la predicción
    if prediction[0] == 0:
       return "Ningun grado de lealtad hacia la empresa"
    elif prediction[0] == 1:
       return "Mediano grado de lealtad hacia la empresa"
    elif prediction[0] == 2:
       return "Totalmente leal hacia la empresa"
    else:
       return "Predicción no reconocida"

if __name__ == "__main__":
    app.run(debug=True)




@app.route("/")
def hello_world():
    return "<p>Hola Mundo Bienvenido a Machine Learning</p>"

if __name__ == "__main__":
    app.run(port=8000, debug=True)


