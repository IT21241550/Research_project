def preprocess_data(df):
    # Scale or normalize features if necessary
    df['RainData'] = df['RainData'] / 10
    df['Standardized Precipitation Index'] = (df['Standardized Precipitation Index'] + 3) / 6
    df['Standardized Precipitation Evapotranspiration Index'] = (df['Standardized Precipitation Evapotranspiration Index'] + 3) / 6
    return df
