import pandas as pd

def preprocess_data(input_path, output_path):
    data = pd.read_csv(input_path)
    data['pressure'] = (data['pressure'] - 900) / (1050 - 900)  # Normalize
    data['wind_speed'] = data['wind_speed'] / 150               # Normalize
    data.to_csv(output_path, index=False)
    print(f"Processed data saved to {output_path}")

if __name__ == "__main__":
    preprocess_data("data/raw/cyclone_data.csv", "data/processed/processed_data.csv")
