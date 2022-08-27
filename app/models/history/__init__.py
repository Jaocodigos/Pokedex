from app.models import db


class History(db.model):
    __tablename__ = 'history'

    id = db.Column(db.Integer, auto_increment=True, primary_key=True)
    dex = db.Column(db.String(50), nullable=False, unique=False)
