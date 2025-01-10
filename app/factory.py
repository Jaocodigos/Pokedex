from flask import Flask
from os import environ
from app.config import get_config
from flask_migrate import Migrate
import requests

app = Flask(__name__)

# Get flask configuration
mode = environ['FLASK_ENV']
if mode not in ['testing', 'development']:
    raise ValueError("Invalid env.")
app.config.from_object(get_config(mode))


# Factory
def app_create():

    from app.models import db
    from app.schemas import schema
    db.init_app(app)
    schema.init_app(app)

    #starting migrations
    Migrate(app, db)

    from app.resources import poke
    app.register_blueprint(poke)

    return app



