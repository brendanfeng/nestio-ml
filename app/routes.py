from app import app
import regression
from flask import request, jsonify
import numpy as np

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/predict')
def predict():
    neighborhood = request.args.get('neighborhood')
    layout = request.args.get('layout')
    bathrooms = request.args.get('bathrooms')
    square_footage = request.args.get('square_footage')

    predicted_price = regression.run([{
        'neighborhood': neighborhood,
        'layout': layout, 
        'bathrooms': bathrooms,
        'square_footage': int(square_footage)
    }])

    return jsonify(predicted_price[0][0])
