from flask import Blueprint
from views.treinamento_view import listar_treinamentos_view, novo_treinamento_view, deletar_treinamento_view

treinamento_bp = Blueprint("treinamento_bp", __name__)

@treinamento_bp.route("/treinamentos")
def listar_treinamentos():
    return listar_treinamentos_view()

@treinamento_bp.route("/treinamentos/novo", methods=["GET", "POST"])
def novo_treinamento():
    return novo_treinamento_view()


@treinamento_bp.route("/treinamentos/delete/<int:id>", methods=["POST"])
def deletar_treinamento(id):
    return deletar_treinamento_view(id)