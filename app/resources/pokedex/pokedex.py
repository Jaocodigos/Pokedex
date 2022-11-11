from flask import Flask, render_template, session, flash, url_for, request, redirect
from app.resources import poke
import requests


@poke.route('/', methods=['GET'])
def index():
    return render_template('index.html', titulo='Pokedex v0.2', dex=url_for('static', filename='pokeball.png'))


@poke.route('/dex', methods=['POST', ])
def search():
    nome = str(request.form['poke']).lower()

    buscar = f'https://pokeapi.co/api/v2/pokemon/{nome}'
    res = requests.get(buscar)
    if res.status_code == 200:
        pokemon = res.json()
        id = pokemon['id']
        deximg = f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{id}.png'
        type = []
        habs = []
        for abi in pokemon['abilities']:
            habs.append(abi['ability']['name'])
        for tip in pokemon['types']:
            type.append(tip['type']['name'])
        return render_template('index.html', titulo='Pokedex v0.2', type=type, habs=habs, dex=deximg)
    flash("O pokémon digitado não existe!")
    return redirect(url_for('pokedex.index'))
