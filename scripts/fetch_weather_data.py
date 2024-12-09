import os
import requests

def fetch_weather_data(api_key, location):
    print("Starting to fetch weather data...")
    if not api_key:
        raise ValueError("API_KEY is not set.")
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}"
    print(f"Requesting data from {url}")
    response = requests.get(url)
    if response.status_code == 200:
        print("Data fetched successfully.")
        return response.json()
    else:
        print(f"Failed to fetch data: {response.status_code}, {response.text}")
        raise Exception(f"Failed to fetch data: {response.status_code}, {response.text}")

# Exemple d’appel
if __name__ == "__main__":
    api_key = os.getenv("API_KEY")
    location = "Paris"
    try:
        data = fetch_weather_data(api_key, location)
        print(data)
    except Exception as e:
        print(f"Error: {e}")
