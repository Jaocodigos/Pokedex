from app.models import db


class History(db.model):
    __tablename__ = 'history'

    id = db.Column(db.Integer, auto_increment=True, primary_key=True)
    dex = db.Column(db.String(30), nullable=False, unique=False)
    name = db.Column(db.String(30), nullable=False, unique=False)
    type = db.Column(db.String(20), nullable=False, unique=False)
