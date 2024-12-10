from flask import Flask, request, jsonify
import pandas as pd
import joblib
import os
from utils.preprocessing import preprocess_data
from utils.predictions import make_prediction

app = Flask(__name__)
current_dir = os.path.dirname(os.path.abspath(__file__))
# Load the model with error handling
# model_path = "F:/projects/Cyclone/models/Cyclone_model.pkl"  # Ensure this path is correct
# model_path = os.path.join(current_dir, 'models', 'Cyclone_model.pkl') 
model_path = os.path.join(current_dir, "../models/Cyclone_model.pkl")

if os.path.exists(model_path):
    model = joblib.load(model_path)
    print(f"Model loaded from {model_path}")
else:
    print(f"Model file not found at {model_path}. Please train the model first.")
    model = None  # Set model to None if file not found

@app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        return jsonify({"error": "Model file is missing. Please train the model first."}), 500
    
    try:
        data = request.get_json()
        df = pd.DataFrame([data])
        processed_data = preprocess_data(df)
        prediction = make_prediction(model, processed_data)
        return jsonify({"storm_category": int(prediction[0])})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

