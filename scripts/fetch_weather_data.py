import os
import requests
import json

def fetch_weather_data(location):
    # Récupération de la clé API
    api_key = os.getenv("API_KEY", "167e37e7a8204ddf848115830241012")  # Utilise la clé si aucune variable d'environnement n'est définie
    
    print("Starting to fetch weather data...")
    
    if not api_key:
        raise ValueError("API_KEY is not set. Please provide the API_KEY.")

    # URL de l'API WeatherAPI
    base_url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": api_key,
        "q": location,
        "aqi": "no"
    }

    try:
        # Faire une requête GET
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Vérifie si la requête a réussi
        weather_data = response.json()
        
        print("Weather data fetched successfully!")
        return weather_data
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        raise

if __name__ == "__main__":
    # Exemple de localisation
    location = "Paris"
    
    try:
        # Récupérer les données
        data = fetch_weather_data(location)
        print("Weather data:")
        print(json.dumps(data, indent=4))  # Afficher les données formatées
        
        # Sauvegarder les données dans un fichier JSON
        output_file = "data/weather_data.json"
        os.makedirs(os.path.dirname(output_file), exist_ok=True)  # Crée le répertoire si nécessaire
        
        with open(output_file, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Weather data saved to {output_file}.")
    
    except Exception as e:
        print(f"Failed to fetch and save weather data: {e}")

