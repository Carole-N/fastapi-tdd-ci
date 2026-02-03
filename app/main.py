"""
main.py

Couche "API" (HTTP) :
- expose la logique métier via FastAPI
- transforme les entrées/sorties en format HTTP/JSON
- convertit les erreurs métier (ValueError) en erreurs HTTP (400)

Important :
- ce fichier ne doit pas contenir la logique de calcul
- il délègue le calcul à services.py
"""

from fastapi import FastAPI, HTTPException
from app.services import compute_bonus

app = FastAPI()


@app.get("/bonus")
def get_bonus(sales: float):
    """
    Endpoint GET /bonus

    Entrée :
    - sales : montant des ventes (float) reçu en query string

    Sortie (succès) :
    - JSON { "sales": <sales>, "bonus": <bonus> }

    Erreur :
    - si sales < 0, retourne HTTP 400 avec un message d'erreur
    """
    try:
        return {"sales": sales, "bonus": compute_bonus(sales)}
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
