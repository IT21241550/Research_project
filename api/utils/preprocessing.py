def preprocess_data(df):
    # Scale or normalize features if necessary
    df['pressure'] = (df['pressure'] - 900) / (1050 - 900)
    df['wind_speed'] = df['wind_speed'] / 150
    return df