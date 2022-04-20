#Usado apenas para testar a lógica, pode ignorar!

import requests

def dex():
    global pokemon
    choice = str(input('Escolha um Pokémon: '))
    pokedex = f'https://pokeapi.co/api/v2/pokemon/{choice}'
    res = requests.get(pokedex)
    pokemon = res.json()
    print(choice)
    typ(pokemon)
    atribute(pokemon)


def atribute(pokemon):
     print('Habilities: ')
     for abi in pokemon['abilities']:
         print(abi['ability']['name'])

def typ(pokemon):
     print('Tipo: ')
     for tip in pokemon['types']:
       print(tip['type']['name'])


if __name__ == '__main__':
    dex()