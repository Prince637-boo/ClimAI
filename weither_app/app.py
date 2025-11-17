from api_client import get_weather_data
from analyzer import generate_togo_insights

def main():
    """
    Point d'entrée principal de l'application.
    """
    # Coordonnées de Lomé, Togo
    LATITUDE = 6.13
    LONGITUDE = 1.22
    
    print(f"Récupération des données météo pour Lomé (Lat: {LATITUDE}, Lon: {LONGITUDE})...")
    weather_data = get_weather_data(LATITUDE, LONGITUDE)
    
    if weather_data:
        print("Analyse des données et génération des alertes...")
        insights = generate_togo_insights(weather_data)
        for insight in insights:
            print(f"- {insight}")
    else:
        print("Impossible de poursuivre sans données météo.")
        
if __name__ == "__main__":
    main()
