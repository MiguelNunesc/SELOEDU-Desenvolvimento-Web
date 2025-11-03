from extensions import db

class Treinamento(db.Model):
    __tablename__ = "treinamentos"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(120), nullable=False)
    descricao = db.Column(db.Text)
    data = db.Column(db.Date, nullable=False)
    coordenador_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    coordenador = db.relationship("User", backref="treinamentos")

    def __repr__(self):
        return f"<Treinamento {self.titulo}>"