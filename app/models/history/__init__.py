from app.models import db


class History(db.Model):
    __tablename__ = 'history'

    id = db.Column(db.Integer, auto_increment=True, primary_key=True)
    dex = db.Column(db.String(30), nullable=False, unique=False)
    name = db.Column(db.String(30), nullable=False, unique=False)
    type = db.Column(db.String(20), nullable=False, unique=False)
    ability = db.Column(db.String(100), nullable=False, unique=False)
    weight = db.Column(db.Integer, nullable=False, unique=False)
    height = db.Column(db.Integer, nullable=False, unique=False)
