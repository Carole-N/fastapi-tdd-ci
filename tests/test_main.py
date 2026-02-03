"""
test_main.py

Tests de la couche API FastAPI.
- utilise TestClient pour appeler l'application en mémoire
- ne lance pas de serveur (tests rapides et reproductibles)
- vérifie le statut HTTP et le contenu JSON

Objectif pédagogique :
- tester une API FastAPI sans démarrer uvicorn
- vérifier que l'API délègue correctement à la logique métier (services.py)
"""

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_bonus_endpoint_low_sales():
    """GET /bonus (ventes < 50 000) -> 200 + bonus 5 %."""
    response = client.get("/bonus?sales=40000")
    assert response.status_code == 200
    assert response.json()["bonus"] == 2000


def test_bonus_endpoint_high_sales():
    """GET /bonus (ventes >= 50 000) -> 200 + bonus 10 %."""
    response = client.get("/bonus?sales=60000")
    assert response.status_code == 200
    assert response.json()["bonus"] == 6000


def test_bonus_endpoint_negative_sales():
    """GET /bonus (ventes négatives) -> 400."""
    response = client.get("/bonus?sales=-1")
    assert response.status_code == 400
