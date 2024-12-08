import joblib
import pandas as pd

# Load the trained model
model = joblib.load('../models/landslide_model.pkl')

def make_prediction(data):
    """
    Perform prediction using the trained model.
    Args:
        data (dict): Input features (Rainfall_mm, Soil_Moisture).
    Returns:
        list: Predicted labels (0 or 1).
    """
    df = pd.DataFrame(data)
    predictions = model.predict(df)
    return predictions.tolist()
