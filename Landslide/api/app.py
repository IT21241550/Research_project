

from flask import Flask, request, jsonify
import joblib
import pandas as pd
import os

app = Flask(__name__)

# Get the absolute path to the model file
# current_dir = os.path.dirname(os.path.abspath(__file__)) 
model_path = os.path.join(os.getcwd(),'models', 'landslide_model.pkl')

# Debugging: Print the model path to ensure it's correct
print(f"Looking for model at: {model_path}")

# Load the pre-trained model with error handling
try:
    model = joblib.load(model_path)
    print(f"Model loaded successfully from {model_path}")
except FileNotFoundError:
    print(f"Error: Model file not found at {model_path}")
    print("Please ensure the model file exists and the path is correct.")
    raise
except Exception as e:
    print(f"Error loading model: {str(e)}")
    raise

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON input data
        data = request.json
        if not data:
            return jsonify({'error': 'No input data provided'}), 400

        # Convert input data to DataFrame
        df = pd.DataFrame([data])

        # Make prediction
        prediction = model.predict(df)[0]
        probabilities = model.predict_proba(df)[0]

        # Structure the response
        response = {
            "Landslide Risk": "High Risk" if prediction == 1 else "Low Risk",
            "Probability": float(probabilities[1] if prediction == 1 else probabilities[0]),
            "Raw Probabilities": {
                "No Landslide": float(probabilities[0]),
                "Landslide": float(probabilities[1])
            },
            "Status": "success"
        }
        return jsonify(response)

    except Exception as e:
        # Handle any errors during prediction
        return jsonify({'error': str(e), 'status': 'error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
