import joblib
import numpy as np

from flask import Flask
from flask import jsonify

app = Flask(__name__)

#POSTMAN PARA PRUEBAS
@app.route('/predict', methods=['GET'])
def predict():
    X_test = np.array([709812.0,1674223.0,7.0,2019.0,1112.0,6.0,11.0])
    prediction = model.predict(X_test.reshape(1,-1))
    return jsonify({'prediccion' : list(prediction)})

if __name__ == "__main__":
    model = joblib.load('./models/best_model.pkl')
    app.run(port=8080)