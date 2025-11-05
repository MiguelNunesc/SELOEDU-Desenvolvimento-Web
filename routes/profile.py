from flask import Blueprint
from views.users_profile import exibir_perfil_view, atualizar_perfil_view

profile_bp = Blueprint("profile_bp", __name__)

@profile_bp.route("/perfil", methods=["GET"])
def exibir_perfil():
    return exibir_perfil_view()

@profile_bp.route("/perfil", methods=["POST"])
def atualizar_perfil():
    return atualizar_perfil_view()