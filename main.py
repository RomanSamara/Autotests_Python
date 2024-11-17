import requests
import pytest
URL='https://api.pokemonbattle.ru/v2/'
TOKEN='b5d4564c830387dbcc7f979fffb61d02'
HEADER={'Content-Type':'application/json', 'trainer_token':TOKEN}
a=requests.post(url=f'{URL}pokemons', headers=HEADER, json={ "name": "Питон", "photo_id": 1})
print(a.text)
b=requests.put(url=f'{URL}pokemons', headers=HEADER, json={"pokemon_id": "128230", "name": "Питончик", "photo_id": 2})
print(b.text)
c=requests.post(url=f'{URL}trainers/add_pokeball', headers=HEADER, json={"pokemon_id": "128230"})
print(c.text)