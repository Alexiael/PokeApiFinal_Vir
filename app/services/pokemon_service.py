# app/services/pokemon_service.py

import requests
from typing import List, Optional, Dict, Any

def fetch_data(url):
    resp = requests.get(url)
    try:
        resp.raise_for_status() 
    except requests.HTTPError:
        
        return {"error": resp.status_code}
    return resp.json()

def get_water_type_url() -> Optional[str]:
    """
    Retrieves the URL for the "Water" type Pokémon from the PokeAPI.
    """
    url = 'https://pokeapi.co/api/v2/type/'
    data = fetch_data(url)
    if data:
        for type_info in data['results']:
            if type_info['name'] == 'water':
                return type_info['url']
    return None

def fetch_water_pokemons() -> List[str]:
    """
    Fetches the list of all Water-type Pokémon by making an API request.
    """
    water_type_url = get_water_type_url()
    if water_type_url:
        data = fetch_data(water_type_url)
        if data:
            return [pokemon['pokemon']['name'] for pokemon in data['pokemon']]
    return []

def display_pokemons(pokemons: List[str]) -> None:
    """
    Displays the names of all Water-type Pokémon in a readable format.
    """
    if pokemons:
        print("The Water-type Pokémon are: " + ", ".join(pokemons) + ".")
    else:
        print("No Water-type Pokémons found.")
