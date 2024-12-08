import requests
import pandas as pd
import datetime

API_KEY = 'your_api_key_here'
BASE_URL = 'https://api.weatherapi.com/v1/history.json'

def fetch_weather_data(location, date):
    url = f"{BASE_URL}?key={API_KEY}&q={location}&dt={date}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        rainfall = data['forecast']['forecastday'][0]['day']['totalprecip_mm']
        return {'Date': date, 'Region': location, 'Rainfall_mm': rainfall}
    else:
        print(f"Failed to fetch weather data for {location} on {date}")
        return None

# Example usage
today = datetime.datetime.now().strftime('%Y-%m-%d')
weather_data = fetch_weather_data('Kathmandu', today)

if weather_data:
    df = pd.DataFrame([weather_data])
    df.to_csv('../data/raw/rainfall_data.csv', mode='a', header=False, index=False)
    print("Weather data saved.")
