#!/usr/bin/env python
from flask import Flask, request, jsonify
from flask.logging import create_logger

import pandas as pd
from sklearn.externals import joblib
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

def scale(payload):
    """Scales Payload"""
    
    scaler = StandardScaler().fit(payload.astype(float))
    scaled_adhoc_predict = scaler.transform(payload.astype(float))
    return scaled_adhoc_predict

@app.route("/")
def home():
    html = f"<h3>Sklearn Prediction Home</h3>"
    return html.format(format)

@app.route("/predict", methods=['POST'])
def predict():
    """Performs an sklearn prediction
        
        input looks like:
        {
        "CHAS":{
        "0":0
        },
        "RM":{
        "0":6.575
        },
        "TAX":{
        "0":296.0
        },
        "PTRATIO":{
        "0":15.3
        },
        "B":{
        "0":396.9
        },
        "LSTAT":{
        "0":4.98
        }
        
        result looks like:
        { "prediction": [ <val> ] }
        
        """
    json_payload = request.json
    inference_payload = pd.DataFrame(json_payload)
    app.logger.info('in app: JSON payload:\n %s',json_payload)
    # scale the input
    app.logger.info('in app: Inference payload DataFrame:\n %s',inference_payload)
    scaled_payload = scale(inference_payload)
    # get an output prediction from the pretrained model, clf
    app.logger.info('in app: Scaling Payload:\n %s',scaled_payload)
    prediction = list(clf.predict(scaled_payload))
    app.logger.info('in app: prediction: %s',prediction)
    return jsonify({'prediction': prediction})

if __name__ == "__main__":
    # load pretrained model as clf
    clf = joblib.load("./model_data/boston_housing_prediction.joblib")
    app.run(host='0.0.0.0', port=80, debug=True) # specify port=80
