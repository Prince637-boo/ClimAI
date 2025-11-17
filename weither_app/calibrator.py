# calibrator.py
# Ce fichier centralise tous les seuils de décision pour les alertes météo.

# Seuils pour l'Harmattan
HARMATTAN_WIND_DIRECTION_MIN = 0  # Degrés (Nord)
HARMATTAN_WIND_DIRECTION_MAX = 90 # Degrés (Est)
HARMATTAN_DUST_THRESHOLD = 20     # µg/m³

# Seuils de température
HEATWAVE_THRESHOLD = 33           # °C

# Seuils de précipitations et de vent pour les orages
HEAVY_RAIN_THRESHOLD = 10         # mm/h
STORM_WIND_SPEED_THRESHOLD = 40   # km/h

# Seuil de vent fort général
STRONG_WIND_THRESHOLD = 50        # km/h

# Définition des saisons pour le sud du Togo
DRY_SEASONS_MONTHS = [11, 12, 1, 2] # Grande saison sèche
RAINY_SEASONS_MONTHS = list(range(3, 7)) + list(range(9, 11)) # Grande et petite saisons des pluies