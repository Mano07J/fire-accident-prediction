import json
import joblib
import numpy as np

# Load model
model = joblib.load('fire_prediction_model.pkl')

def run(raw_data):
    try:
        data = json.loads(raw_data)
        features = np.array([data['temperature'], data['smoke'], data['humidity'], data['gas']]).reshape(1, -1)
        prediction = model.predict(features)
        return {"fire_risk": int(prediction[0])}
    except Exception as e:
        return {"error": str(e)}
