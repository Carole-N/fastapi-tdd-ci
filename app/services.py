"""
services.py

Couche "métier" (logique pure) :
- contient les règles de calcul indépendantes de FastAPI/HTTP
- est testée en premier en TDD (tests unitaires rapides et stables)

Objectif pédagogique :
- séparer la logique métier de la couche API (main.py)
"""

def compute_bonus(sales: float) -> float:
    """
    Calcule le bonus salarial à partir du montant des ventes.

    Règles métier :
    - ventes < 50 000 €  -> bonus de 5 %
    - ventes >= 50 000 € -> bonus de 10 %
    - ventes négatives   -> erreur (ValueError)
    """
    if sales < 0:
        raise ValueError("Sales must be positive")

    if sales < 50000:
        return sales * 0.05

    return sales * 0.30 # erreur volontaire pour l'exercice TDD (valeur correcte 0.10)
