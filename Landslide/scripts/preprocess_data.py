


# import pandas as pd
# import os

# def load_csv(filepath):
#     """
#     Load a CSV file, ensuring the file exists.
#     Raises FileNotFoundError if the file does not exist.
#     """
#     absolute_path = os.path.abspath(filepath)
#     print(f"Checking file: {absolute_path}")
#     if os.path.exists(filepath):
#         print(f"Loading file: {absolute_path}")
#         return pd.read_csv(filepath)
#     else:
#         raise FileNotFoundError(
#             f"File not found: {absolute_path}\n"
#             f"Ensure the file exists in the correct directory.\n"
#             f"Example structure:\n"
#             f"  - {os.path.dirname(absolute_path)}\n"
#             f"      - rainfall_data.csv\n"
#             f"      - soil_moisture_data.csv\n"
#             f"      - landslide_history.csv"
#         )

# def preprocess_data():
#     """
#     Preprocess landslide data:
#     - Load rainfall, soil moisture, and landslide history datasets.
#     - Merge datasets on common keys ('Date', 'Region').
#     - Handle missing values by filling with 0.
#     - Save processed data to the 'data/processed/' directory.
#     """
#     # Define file paths relative to the script's location
#     base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
#     raw_data_dir = os.path.join(base_dir, "data", "raw")
#     processed_data_dir = os.path.join(base_dir, "data", "processed")

#     rainfall_path = os.path.join(raw_data_dir, "rainfall_data.csv")
#     soil_moisture_path = os.path.join(raw_data_dir, "soil_moisture_data.csv")
#     landslide_history_path = os.path.join(raw_data_dir, "landslide_history.csv")
#     output_path = os.path.join(processed_data_dir, "landslide_data_cleaned.csv")

#     try:
#         # Load raw data
#         rainfall = load_csv(rainfall_path)
#         soil_moisture = load_csv(soil_moisture_path)
#         landslide_history = load_csv(landslide_history_path)

#         # Print data shapes to debug
#         print(f"Rainfall data shape: {rainfall.shape}")
#         print(f"Soil moisture data shape: {soil_moisture.shape}")
#         print(f"Landslide history data shape: {landslide_history.shape}")

#         # Merge datasets on common keys (Date and Region)
#         print("Merging datasets...")
#         merged_data = pd.merge(rainfall, soil_moisture, on=["Date", "Region"], how="inner")
#         print(f"Merged data shape after merging rainfall and soil moisture: {merged_data.shape}")
        
#         merged_data = pd.merge(merged_data, landslide_history, on=["Date", "Region"], how="inner")
#         print(f"Merged data shape after merging landslide history: {merged_data.shape}")

#         # Handle missing values
#         print("Handling missing values...")
#         merged_data.fillna(0, inplace=True)

#         # Check if the merged data is empty after filling missing values
#         if merged_data.empty:
#             print("Warning: The merged data is empty after preprocessing.")
#         else:
#             # Ensure the output directory exists
#             os.makedirs(processed_data_dir, exist_ok=True)

#             # Save processed data
#             print(f"Saving processed data to: {output_path}")
#             merged_data.to_csv(output_path, index=False)
#             print("Data preprocessing completed.")

#     except FileNotFoundError as e:
#         print(f"Error: {e}")
#     except Exception as e:
#         print(f"Unexpected error: {e}")

# if __name__ == "__main__":
#     preprocess_data()


# import os
# import pandas as pd

# # Get absolute paths
# script_dir = os.path.dirname(os.path.abspath(__file__))
# project_dir = os.path.dirname(script_dir)

# # Define data directories
# raw_data_dir = os.path.join(project_dir, 'data', 'raw')
# processed_data_dir = os.path.join(project_dir, 'data', 'processed')

# # Create processed directory if it doesn't exist
# os.makedirs(processed_data_dir, exist_ok=True)

# # Define input and output file paths
# rainfall_file = os.path.join(raw_data_dir, 'rainfall_data.csv')
# soil_moisture_file = os.path.join(raw_data_dir, 'soil_moisture_data.csv')
# landslide_history_file = os.path.join(raw_data_dir, 'landslide_history.csv')
# output_file = os.path.join(processed_data_dir, 'landslide_data_cleaned.csv')

# try:
#     # Load raw data
#     rainfall = pd.read_csv(rainfall_file)
#     soil_moisture = pd.read_csv(soil_moisture_file)
#     landslide_history = pd.read_csv(landslide_history_file)

#     # Print shapes to check data loading
#     print(f"Rainfall data shape: {rainfall.shape}")
#     print(f"Soil moisture data shape: {soil_moisture.shape}")
#     print(f"Landslide history data shape: {landslide_history.shape}")

#     # Merge datasets on Date and Region
#     merged_data = pd.merge(rainfall, soil_moisture, on=["Date", "Region"], how="inner")
#     print(f"Merged data shape after merging rainfall and soil moisture: {merged_data.shape}")

#     merged_data = pd.merge(merged_data, landslide_history, on=["Date", "Region"], how="inner")
#     print(f"Merged data shape after merging landslide history: {merged_data.shape}")

#     # Handle missing values by filling with 0
#     merged_data.fillna(0, inplace=True)

#     # Check if the merged data is empty after preprocessing
#     if merged_data.empty:
#         print("Warning: The merged data is empty after preprocessing.")
#     else:
#         # Save the cleaned data
#         merged_data.to_csv(output_file, index=False)
#         print(f"Data preprocessed and saved to: {output_file}")

# except FileNotFoundError as e:
#     print(f"Error: {e}")
# except Exception as e:
#     print(f"Unexpected error: {e}")


import os
import pandas as pd

# Get absolute paths
script_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(script_dir)

# Define data directories
raw_data_dir = os.path.join(project_dir, 'data', 'raw')
processed_data_dir = os.path.join(project_dir, 'data', 'processed')

# Create processed directory if it doesn't exist
os.makedirs(processed_data_dir, exist_ok=True)

# Define input and output file paths
rainfall_file = os.path.join(raw_data_dir, 'rainfall_data.csv')
soil_moisture_file = os.path.join(raw_data_dir, 'soil_moisture_data.csv')
landslide_history_file = os.path.join(raw_data_dir, 'landslide_history.csv')
output_file = os.path.join(processed_data_dir, 'landslide_data_cleaned.csv')

# Load raw data
rainfall = pd.read_csv(rainfall_file)
soil_moisture = pd.read_csv(soil_moisture_file)
landslide_history = pd.read_csv(landslide_history_file)

# Merge datasets on Date
merged_data = pd.merge(rainfall, soil_moisture, on='Date',)
merged_data = pd.merge(merged_data, landslide_history, on='Date',)

# Save cleaned data
merged_data.to_csv(output_file, index=False)
print("Data preprocessed and saved.")
