

import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Path to data and model
data_path = os.path.join(os.getcwd(), 'data', 'processed', 'landslide_data_cleaned.csv')
model_path = os.path.join(os.getcwd(),  'models', 'landslide_model.pkl')

# Ensure the models directory exists
os.makedirs(os.path.dirname(model_path), exist_ok=True)

# Load the dataset
data = pd.read_csv(data_path)

# Prepare the data
X = data[['Rainfall_mm', 'Soil_Moisture']]
y = data['Landslide']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Save the model
joblib.dump(model, model_path)
print(f"Model saved at: {model_path}")


