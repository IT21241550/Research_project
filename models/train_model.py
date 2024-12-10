import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

def train_model():
    
    current_dir = os.getcwd()
  
    data_path = os.path.join(current_dir, 'data', 'raw', 'cyclone_data.csv')  

    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Data file not found at {data_path}. Please ensure the data exists.")

    print(f"Loading data from: {data_path}")
    data = pd.read_csv(data_path)

    X = data[["latitude", "longitude", "pressure", "wind_speed"]] 
    y = data["storm_category"]  
   
    print("Training the model...")
    model = RandomForestClassifier()
    model.fit(X, y)

    model_path = os.path.join(current_dir, 'models', 'Cyclone_model.pkl')  
    os.makedirs(os.path.dirname(model_path), exist_ok=True)  
    joblib.dump(model, model_path)
    print(f"Model trained and saved at {model_path}")

if __name__ == "__main__":
    try:
        train_model()
    except Exception as e:
        print(f"An error occurred: {e}")