# Projet de Prévisions Météorologiques Assistées par IA

Ce projet vise à développer une application de prévisions météorologiques ultra-localisées, utilisant l'intelligence artificielle pour fournir des aides à la décision critiques pour des secteurs spécifiques tels que l'agriculture, l'aviation (aéroports) et la navigation maritime (zones portuaires).

## Vision du Projet

L'objectif final est de s'appuyer sur des modèles d'IA avancés (potentiellement des modèles comme GraphCast) pour offrir des prévisions plus précises et pertinentes que les modèles traditionnels. L'application fournira des alertes et des recommandations contextualisées pour aider les professionnels à optimiser leurs opérations, à améliorer la sécurité et à réduire les coûts liés aux conditions météorologiques.

## État Actuel (Phase 1)

Actuellement, le projet est dans sa phase initiale de développement. L'accent est mis sur la collecte et l'interprétation de données météorologiques via des APIs publiques.

- **Source de données** : [Open-Meteo API](https://open-meteo.com/)
- **Fonctionnalités actuelles** :
  - Récupération des données horaires (température, précipitations, vitesse du vent).
  - Analyse des données pour générer des alertes contextualisées pour le climat du sud du Togo (Harmattan, vagues de chaleur, pluies intenses).

## Comment utiliser

### Prérequis

- Python 3.x

Installez les dépendances avec pip :
```bash
pip install -r requirements.txt
```

### Exemple d'utilisation

Vous pouvez utiliser le script `app.py` pour obtenir des prévisions et des alertes pour une localisation donnée.

```python
# main.py (exemple de fichier pour utiliser le module app)
from app import get_weather, generate_agricultural_insights

# Coordonnées de Paris
LATITUDE = 48.85
LONGITUDE = 2.35

weather_data = get_weather(LATITUDE, LONGITUDE)
if weather_data:
    insights = generate_agricultural_insights(weather_data)
    for insight in insights:
        print(insight)
```

## Prochaines Étapes

- Développer des modules d'analyse pour les secteurs aéroportuaire et maritime.
- Mettre en place une base de données pour historiser les prévisions et les observations.
- Commencer l'exploration et l'intégration de modèles d'IA pour affiner les prévisions.
- Développer une interface utilisateur (API REST ou application web).