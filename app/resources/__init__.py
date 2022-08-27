from flask import Blueprint

pokedex = Blueprint('pokedex', __name__)

from app.resources.pokedex import *