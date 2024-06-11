from flask import Flask
from flask import request
import pandas as pd
import joblib


app = Flask(__name__)

@app.route('/predice', methods=['POST'])
def predict():
    json_ = request.json
    query_df = pd.DataFrame(json_, index=[0])
    query = pd.get_dummies(query_df)
    
    classifier = joblib.load('classifier.pkl')
    prediction = classifier.predict(query)

    if prediction[0] == 0:
        return "De ninguna forma, 3 años con un empleador es para volverse loco"
    elif prediction[0] == 1:
        return "Eso sería dificil, pero si es la compañía correcta lo intentaría"
    elif prediction[0] == 2:
        return "Trabajaría por 3 años o más"
    else:
        return "Predicción no reconocida"

if __name__ == "__main__":
    app.run(port=8000, debug=True)


