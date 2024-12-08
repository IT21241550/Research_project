import pandas as pd

def preprocess_input(data):
    """
    Preprocess input data for prediction.
    Args:
        data (dict): Raw input data.
    Returns:
        DataFrame: Cleaned and formatted data.
    """
    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Handle missing values
    df.fillna(0, inplace=True)

    # Ensure correct data types
    df['Rainfall_mm'] = df['Rainfall_mm'].astype(float)
    df['Soil_Moisture'] = df['Soil_Moisture'].astype(float)

    return df
