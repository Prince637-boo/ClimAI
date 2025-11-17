# analyzer.py
import calibrator as cal
from utils import get_month_from_time_str, format_time_for_alert

def generate_togo_insights(weather_data):
    """
    Analyse les données météo et génère des alertes spécifiques au contexte du sud du Togo.
    """
    if not weather_data or 'hourly' not in weather_data:
        return ["Impossible de générer des alertes : données météo non disponibles."]

    insights = []
    hourly = weather_data['hourly']
    
    # Utilisation de zip pour itérer sur toutes les listes en même temps de manière sécurisée
    data_points = zip(
        hourly.get('time', []),
        hourly.get('temperature_2m', []),
        hourly.get('precipitation', []),
        hourly.get('wind_speed_10m', []),
        hourly.get('wind_direction_10m', []),
        hourly.get('dust', [])
    )

    for time, temp, precip, w_speed, w_dir, dust in data_points:
        month = get_month_from_time_str(time)
        formatted_time = format_time_for_alert(time)

        # --- Analyse Saisons Sèches ---
        if month in cal.DRY_SEASONS_MONTHS:
            # Règle 1: Détection de l'Harmattan
            if cal.HARMATTAN_WIND_DIRECTION_MIN <= w_dir <= cal.HARMATTAN_WIND_DIRECTION_MAX and dust > cal.HARMATTAN_DUST_THRESHOLD:
                insights.append(f"ALERTE HARMATTAN: Le {formatted_time}, vent sec et poussiéreux attendu. Visibilité réduite possible. Poussière: {dust:.1f} µg/m³.")

            # Règle 2: Vague de chaleur
            if temp > cal.HEATWAVE_THRESHOLD:
                insights.append(f"ALERTE CHALEUR: Le {formatted_time}, forte chaleur attendue ({temp}°C). Risque pour les cultures et le bétail.")

        # --- Analyse Saisons des Pluies ---
        if month in cal.RAINY_SEASONS_MONTHS:
            # Règle 3: Détection de pluies intenses / Lignes de grains
            if precip > cal.HEAVY_RAIN_THRESHOLD:
                alert_msg = f"ALERTE PLUIES INTENSES: Le {formatted_time}, fortes averses prévues ({precip} mm/h)."
                if w_speed > cal.STORM_WIND_SPEED_THRESHOLD:
                    alert_msg += f" Accompagnées de vents forts ({w_speed} km/h). Risque d'inondations et de dégâts."
                insights.append(alert_msg)

    if not insights:
        return ["Aucune alerte particulière pour les prochaines heures."]

    return insights