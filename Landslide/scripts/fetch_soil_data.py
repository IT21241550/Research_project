import requests
import pandas as pd

API_KEY = 'your_api_key_here'
BASE_URL = 'https://api.soil-moisture.com/data'

def fetch_soil_data(location):
    url = f"{BASE_URL}?key={API_KEY}&location={location}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        soil_moisture = data['soil_moisture']
        return {'Region': location, 'Soil_Moisture': soil_moisture}
    else:
        print(f"Failed to fetch soil moisture data for {location}")
        return None

# Example usage
soil_data = fetch_soil_data('Kathmandu')

if soil_data:
    df = pd.DataFrame([soil_data])
    df.to_csv('../data/raw/soil_moisture_data.csv', mode='a', header=False, index=False)
    print("Soil moisture data saved.")
