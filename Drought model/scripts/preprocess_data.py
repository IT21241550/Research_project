import pandas as pd

def preprocess_data(input_path, output_path):
    data = pd.read_csv(input_path)
    
    # Normalize the features (RainData, SPI, SPEI)
    data['RainData'] = data['RainData'] / 10
    data['Standardized Precipitation Index'] = (data['Standardized Precipitation Index'] + 3) / 6
    data['Standardized Precipitation Evapotranspiration Index'] = (data['Standardized Precipitation Evapotranspiration Index'] + 3) / 6
    
    # Save processed data
    data.to_csv(output_path, index=False)
    print(f"Processed data saved to {output_path}")

if __name__ == "__main__":
    preprocess_data("data/raw/drought_data.csv", "data/processed/processed_data.csv")
