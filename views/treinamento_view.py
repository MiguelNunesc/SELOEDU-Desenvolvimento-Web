from flask import render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
from extensions import db
from models.treinamento import Treinamento
from datetime import datetime

@login_required
def listar_treinamentos_view():
    treinamentos = Treinamento.query.all()
    return render_template("treinamento/listar.html", treinamentos=treinamentos)

@login_required
def novo_treinamento_view():
    if current_user.role != "coordenador" and current_user.role != "master":
        flash("Apenas coordenadores podem cadastrar treinamentos.", "danger")
        return redirect(url_for("treinamento_bp.listar_treinamentos"))

    if request.method == "POST":
        titulo = request.form.get("titulo")
        descricao = request.form.get("descricao")
        data_str = request.form.get("data")
        data = datetime.strptime(data_str, "%Y-%m-%d").date() if data_str else None

        if not titulo or not data:
            flash("Título e data são obrigatórios.", "warning")
            return redirect(url_for("treinamento_bp.novo_treinamento"))

        novo = Treinamento(
            titulo=titulo,
            descricao=descricao,
            data=data,
            coordenador_id=current_user.id
        )

        db.session.add(novo)
        db.session.commit()
        flash("Treinamento cadastrado com sucesso!", "success")
        return redirect(url_for("treinamento_bp.listar_treinamentos"))

    return render_template("treinamento/novo.html")
