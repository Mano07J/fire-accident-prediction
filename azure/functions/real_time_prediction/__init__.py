import json
import joblib

model = joblib.load("fire_prediction_model.pkl")

def main(req):
    data = req.get_json()
    X = [[data["temperature"], data["smoke"], data["humidity"], data["gas"]]]
    prediction = model.predict(X)
    return {"fire_risk": prediction[0]}
