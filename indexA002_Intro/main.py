"""
Lien : https://www.youtube.com/watch?v=0-yncL0bqZs
Cours : Fast API : Créer facilement une API en Python

Librairies installées :
FastAPI
uvicorn

À saisir au terminal après être certain d'être sur le bon chemin d'accès...:
uvicorn main:app --reload

À saisir au server web pour avoir la documentation :
http://127.0.0.1:8000/docs

Date : 05-05-24
"""

from fastapi import FastAPI, Path, HTTPException
import json
from dataclasses import dataclass, asdict
from typing import Union

# ===== Structure de données : dictionnaire indexé par pokemon id ========

# Chargement du fichier json et récupération des données
with open("pokemons.json", "r") as f:
    pokemons_list = json.load(f)

# Comprehension de dictionnaire : données json converties en type dict
list_pokemons = {k+1:v for k, v in enumerate(pokemons_list)}
# ============================================================================

# ==================== attributs affectés au Pokemon =======================
@dataclass
class Pokemon(): # les types sont référencés en fonction du fichier JSON
    id: int
    name: str
    types : list[str]
    total: int
    hp: int
    attack: int
    defense: int
    attack_special: int
    defense_special: int
    speed: int
    evolution_id: Union[int, None] = None # possib de ne pas avoir d'évolut°
# ============================================================================

# Instanciation de la librairie FastApi
app = FastAPI()

# Récupérer le nombre de pokemons : le nom de la fonction va s'afficher sur le @
@app.get("/total_pokemons") # URL à récupérer
def total_pokemons() -> dict: # return au format dict
    return {"Nombre total de pokemons":len(list_pokemons)}

# Récupérer la liste des pokemons
@app.get("/pokemons")
def all_pokemons() -> list: 
    return [(Pokemon(**list_pokemons[id])) for id in list_pokemons]

# Récupérer les données d'un pokemon
@app.get("/pokemon/{id}")
def pokemon_by_id(id: int = Path(ge=1)) -> Pokemon: # valeur minimum = 1
    if id not in list_pokemons:
        raise HTTPException(status_code=404, detail="Ce pokemon n'existe pas")
    return Pokemon(**list_pokemons[id])

# Créer un pokemon
@app.post("/pokemon/")
def create_pokemon(pokemon:Pokemon) -> Pokemon:
    if pokemon.id in list_pokemons:
        raise HTTPException(
            status_code=404, detail=f"Le pokemon {pokemon.id} existe déjà")
    list_pokemons[pokemon.id] = asdict(pokemon)
    return Pokemon

# Modifier un pokemon
@app.put("/pokemon/{id}")
def update_pokemon(pokemon:Pokemon, id:int = Path(ge=1)) -> Pokemon:
    if id not in list_pokemons:
        raise HTTPException(status_code=404, detail="Ce pokemon n'existe pas")
    list_pokemons[id] = asdict(pokemon)
    return Pokemon

# Supprimer un pokemon
@app.delete("/pokemon/{id}")
def delete_pokemon(id:int = Path(ge=1)) -> Pokemon:
    if id in list_pokemons:
        pokemon = Pokemon(**list_pokemons[id])
        del list_pokemons[id]
        return pokemon
    raise HTTPException(status_code=404, detail="Ce pokemon n'existe pas")

# Récupérer tous les types de pokemon
@app.get("/types")
def all_types() -> list[str]:
    types = []
    for pokemon in pokemons_list:
        for type in pokemon["types"]:
            if type not in types:
                types.append(type)
    types.sort()
    return types
