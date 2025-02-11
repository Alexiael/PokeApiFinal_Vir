# tests/test_routers/test_main_router.py

from fastapi.testclient import TestClient
import pytest
from main import app

# Creamos un TestClient basado en la app de FastAPI
client = TestClient(app)

def test_home_endpoint():
    """
    Prueba el endpoint raíz GET / 
    """
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    # Depende de lo que devuelva tu home:
    #   {"message": "¡Bienvenido a la Pokémon App con FastAPI!"}
    assert "message" in data

def test_water_pokemon_endpoint():
    """
    Prueba el endpoint GET /pokemon/water
    """
    response = client.get("/pokemon/water")
    assert response.status_code == 200
    data = response.json()
    # Si devuelves {"water_pokemons": [...]}
    assert "water_pokemons" in data
    assert isinstance(data["water_pokemons"], list)
    # Al menos 1 pokémon de agua
    assert len(data["water_pokemons"]) > 0
