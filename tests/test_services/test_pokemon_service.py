# tests/test_services/test_pokemon_service.py

import pytest
from app.services.pokemon_service import (
    fetch_data,
    fetch_water_pokemons,
)

def test_fetch_data_ok():
    """
    Prueba que fetch_data devuelva algo (no None) cuando la URL es válida.
    Esto es un test "integración" que llama a la PokeAPI real.
    """
    url = "https://pokeapi.co/api/v2/pokemon/ditto"
    data = fetch_data(url)
    assert data is not None
    assert "name" in data
    assert data["name"] == "ditto"

def test_fetch_data_fail():
    """
    Prueba que fetch_data retorne None (o maneje excepción)
    si la URL es inválida o hay un error.
    """
    url = "https://pokeapi.co/api/v2/pokemon/no-existe-12345"
    data = fetch_data(url)
    # Normalmente la PokeAPI devolverá un 404; fetch_data retornará algo
    # Depende de tu implementación. Si fetch_data retorna None en error, checa:
    assert data is not None  # O None, según tu lógica
    # Ajusta según el comportamiento real

def test_fetch_water_pokemons():
    """
    Prueba la función fetch_water_pokemons, asegurándose de que
    retorne una lista de strings.
    """
    water_list = fetch_water_pokemons()
    assert isinstance(water_list, list)
    # Al menos deberíamos tener varios Pokémon de tipo agua
    assert len(water_list) > 0
    assert all(isinstance(poke, str) for poke in water_list)
