import requests
import pytest
URL='https://api.pokemonbattle.ru/v2/'
TOKEN='b5d4564c830387dbcc7f979fffb61d02'
HEADER={'Content-Type':'application/json', 'trainer_token':TOKEN}
def test_a ():
    a=requests.get(url=f'{URL}trainers?trainer_id=7320', headers=HEADER)
    assert a.status_code==200
def test_b ():
    b=requests.get(url=f'{URL}trainers?trainer_id=7320', headers=HEADER)
    assert b.json()["data"][0]["id"]=='7320'

