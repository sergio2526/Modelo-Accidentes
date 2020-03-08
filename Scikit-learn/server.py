import joblib
import numpy as np

from flask import Flask
from flask import jsonify

app = Flask(__name__)

if __name__ == '__main__':
    model = joblib.load('./models/best_model.pkl')
    app.run(port=8080)