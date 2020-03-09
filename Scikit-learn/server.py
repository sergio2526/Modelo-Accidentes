import joblib
import numpy as np

from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')

def modelo():
    model = joblib.load('./models/best_model.pkl')

if __name__ == '__main__':
    app.run()