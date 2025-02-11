from fastapi import APIRouter
from app.models.pokemon import Pokemon
from app.services.pokemon_service import fetch_water_pokemons  # <-- importar el servicio

router = APIRouter()

@router.get("/")
def home():
    return {"message": "¡Bienvenido a la Pokémon App con FastAPI!"}

@router.get("/pokemon")
def list_pokemon():
    # Ejemplo: devuelves un listado estático o lo que tenías antes
    return ["pikachu", "charmander", "bulbasaur"]

@router.get("/pokemon/water")
def get_water_pokemon():
    """
    Devuelve la lista de Pokémon de tipo Agua.
    """
    water_pokemons = fetch_water_pokemons()
    return {"water_pokemons": water_pokemons}

