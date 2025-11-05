from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
import os

from extensions import db
from utils.uploads import save_image, remove_file_safe
from forms.profile_form import ProfileForm
from models.profile import Profile


@login_required
def profile():
    form = ProfileForm()
    user = current_user

    # Busca ou cria perfil do usuário
    perfil = Profile.query.filter_by(user_id=user.id).first()
    if not perfil:
        perfil = Profile(user_id=user.id)
        db.session.add(perfil)
        db.session.commit()

    if request.method == "POST" and form.validate_on_submit():
        perfil.telefone = form.telefone.data
        perfil.instituicao = form.instituicao.data
        perfil.cargo = form.cargo.data
        perfil.bio = form.bio.data

        foto = request.files.get("foto")
        if foto and foto.filename != "":
            if getattr(perfil, "foto", None):
                remove_file_safe(perfil.foto)
            if getattr(perfil, "foto_thumb", None):
                remove_file_safe(perfil.foto_thumb)

            filename, thumb = save_image(foto, user_name=user.nome)
            perfil.foto = filename
            perfil.foto_thumb = thumb

        db.session.commit()
        flash("Perfil atualizado com sucesso!", "success")
        return redirect(url_for("users.profile"))

    return render_template("users/profile.html", form=form, profile=perfil, usuario=user)
