from flask import Flask, render_template, session, flash, url_for, request, redirect
import requests

app = Flask(__name__)

app.secret_key = 'thebestofthebests'


@app.route('/')
def index():
    return render_template('index.html', titulo='Pokedex 1.0')


@app.route('/buscar', methods=['POST', ])
def search():
    nome = str(request.form['poke'])

    buscar = f'https://pokeapi.co/api/v2/pokemon/{nome}'
    res = requests.get(buscar)
    pokemon = res.json()
    id = pokemon['id']
    deximg = f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{id}.png'
    type = []
    habs = []
    for abi in pokemon['abilities']:
        habs.append(abi['ability']['name'])
    for tip in pokemon['types']:
        type.append(tip['type']['name'])
    return render_template('index.html', titulo='Pokedex', type=type, habs=habs, dex=deximg)


if __name__ == '__main__':
    app.run(debug=True)
    #dex()


