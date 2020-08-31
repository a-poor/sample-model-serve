
import json
import pickle
import pathlib

import numpy as np
from flask import Flask, request


def load_model(path):
    """Loads the sklearn model from pickle"""
    with path.open("rb") as f:
        return pickle.load(f)
    
def format_input(model_input):
    """Attempts to format the model input"""
    assert model_input, "Empty model input"
    data = np.array([
        json.loads(model_input)
        ]).reshape((-1,1))
    assert len(data.shape) in (1,2), "Data should be either 1D or 2D"
    return data

def predict(model,data):
    """Attempts to use model to make prediction"""
    return model.predict(data).tolist()

def fmt_response(rtype,k,v):
    """Formats json response."""
    return {"type": rtype, k: v}

def fmt_prediction(prediction):
    """Uses fmt_response() to create
    successful JSON model response"""
    return fmt_response("success","prediction",prediction)

def fmt_error(err):
    """Uses fmt_response() to create
    unsuccessful JSON error response"""
    return fmt_response("error","message",err)


# Create the flask app and
# load the iris model
app = Flask(__name__)
model_path = pathlib.Path(__file__).parent / "model.pkl"
model = load_model(model_path)


# Model serve function
@app.route("/iris")
def iris_predict():
    # Does the request have arguments?
    if not request.args:
        return fmt_error("No data provided")
    
    # Is "input" on of the arguments?
    if not request.args.get("input"):
        return fmt_error("No input data provided")

    # Can the input be processed?
    try:
        data = format_input(request.args.get("input"))
    except:
        return fmt_error("Error formatting input")

    # Can the model make a prediction?
    try:
        prediction = predict(model,data)
    except:
        return fmt_error("Error making prediction")

    # Return the prediction as JSON
    return fmt_prediction(prediction)

    
# Run the app in debug mode
if __name__ == "__main__":
    app.run(debug=True)
