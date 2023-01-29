from flask import Blueprint

poke = Blueprint('pokedex', __name__)

from app.resources.pokedex.pokedex import *
from app.resources.history.history import *