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
       return "De ninguna forma, 3 años con un empleador es para volverse loco"
    elif prediction[0] == 1:
       return "Eso sería difícil, pero si es la compañía correcta lo intentaría"
    elif prediction[0] == 2:
       return "Trabajaría por 3 años o más"
    else:
       return "Predicción no reconocida"

if __name__ == "__main__":
    app.run(debug=True)




@app.route("/")
def hello_world():
    return "<p>Hola Mundo Bienvenido a Machine Learning</p>"

if __name__ == "__main__":
    app.run(port=8000, debug=True)


