import pickle
import numpy as np
import os

current_dir = os.path.dirname(__file__)

model_path = os.path.abspath(os.path.join(current_dir, "..", "model", "model.pkl"))
scaler_path = os.path.abspath(os.path.join(current_dir, "..", "model", "scaler.pkl"))

model = pickle.load(open(model_path, "rb"))
scaler = pickle.load(open(scaler_path, "rb"))

def predict_output(data):
    data = np.array(data).reshape(1, -1)
    data = scaler.transform(data)
    prediction = model.predict(data)
    return prediction[0]