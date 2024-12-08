import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model(input_path, model_path):
    data = pd.read_csv(input_path)
    X = data[['RainData', 'Standardized Precipitation Index', 'Standardized Precipitation Evapotranspiration Index']]
    y = data['DroughtCategory']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    print(f"Training Accuracy: {model.score(X_train, y_train):.2f}")
    print(f"Testing Accuracy: {model.score(X_test, y_test):.2f}")
    print(f"Anuradapura")
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    train_model("data/raw/drought_data.csv", "models/Drought_model.pkl")
