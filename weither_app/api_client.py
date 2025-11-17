import requests
from requests.exceptions import RequestException

def get_weather_data(lat, lon):
    """
    Récupère les données météorologiques brutes depuis l'API Open-Meteo.

    Args:
        lat (float): La latitude du lieu.
        lon (float): La longitude du lieu.

    Returns:
        dict: Les données météo au format JSON, ou None en cas d'erreur.
    """
    if not all(isinstance(coord, (int, float)) for coord in [lat, lon]):
        print("Erreur: La latitude et la longitude doivent être des nombres.")
        return None

    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m,precipitation,wind_speed_10m,wind_direction_10m,dust"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except RequestException as e:
        print(f"Erreur lors de l'appel à l'API météo: {e}")
        return None