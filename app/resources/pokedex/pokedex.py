from flask import Flask, render_template, session, flash, url_for, request, redirect
from app.resources import poke
from app.resources.pokedex.form import DexForm
import requests

pokedex_url = 'index.html'


@poke.route('/', methods=['GET', 'POST'])
@poke.route('/pokedex', methods=['GET', 'POST'])
def index():
    form = DexForm()
    if request.method == 'POST' and form.validate_on_submit():
        name = form.name.data.lower()
        try:
            api_request = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}')
            if api_request.status_code == 200:
                data = api_request.json()
                poke_id = data['id']
                img = f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{poke_id}.png'
                poke_type = []
                poke_habs = []
                for abi in data['abilities']:
                    poke_habs.append(abi['ability']['name'])
                for tip in data['types']:
                    poke_type.append(tip['type']['name'])
                return render_template(pokedex_url, form=form, type=poke_type, habs=poke_habs, dex=img)
        except Exception as e:
            flash("This pokemon doesn't exist", category='danger')
            return redirect('pokedex.index')
    return render_template(pokedex_url, form=form, dex=url_for('static', filename='pokeball.png'))


