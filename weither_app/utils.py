# utils.py
from datetime import datetime

def get_month_from_time_str(time_str):
    """Convertit une chaîne de temps ISO en numéro de mois."""
    return datetime.fromisoformat(time_str).month

def format_time_for_alert(time_str):
    """Formate une chaîne de temps ISO pour l'affichage dans une alerte."""
    return datetime.fromisoformat(time_str).strftime('%d/%m à %Hh')