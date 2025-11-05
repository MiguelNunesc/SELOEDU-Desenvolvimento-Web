from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import ForeignKey
from extensions import db

from extensions import db

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    telefone = db.Column(db.String(11))
    instituicao = db.Column(db.String(100))
    cargo = db.Column(db.String(50))
    bio = db.Column(db.String(1000))
    foto = db.Column(db.String(255))        # nome do arquivo original
    foto_thumb = db.Column(db.String(255))  # miniatura (thumb)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True, nullable=False)

    user = db.relationship('User', back_populates='perfil', uselist=False)

    user = db.relationship(
        'User',
        back_populates='perfil', # Nome do atributo de relacionamento na classe User
        uselist=False
    )