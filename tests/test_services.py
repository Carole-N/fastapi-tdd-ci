"""
test_services.py

Tests unitaires de la logique métier (TDD).
- cible directement compute_bonus() (sans FastAPI)
- valide les règles métier (cas nominal + cas d'erreur)

Objectif pédagogique :
- appliquer le cycle TDD Red -> Green -> Refactor sur la logique métier
"""

import pytest
from app.services import compute_bonus


def test_bonus_low_sales():
    """Ventes < 50 000 € -> bonus 5 %."""
    assert compute_bonus(40000) == 2000


def test_bonus_high_sales():
    """Ventes >= 50 000 € -> bonus 10 %."""
    assert compute_bonus(60000) == 6000


def test_negative_sales():
    """Ventes négatives -> ValueError."""
    with pytest.raises(ValueError):
        compute_bonus(-1000)
