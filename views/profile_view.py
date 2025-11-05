import os
from flask import render_template, request, redirect, url_for, flash, current_app
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from extensions import db
from models.profile import Profile
from models.users import User
from forms.profile_form import ProfileForm
from utils.uploads import save_image, remove_file_safe

@login_required
def profile_view():
    """Exibe o perfil do usuário logado e permite edição"""
    form = ProfileForm()
    user = User.query.get(current_user.id)
    profile = Profile.query.filter_by(user_id=current_user.id).first()

    if request.method == "POST" and form.validate_on_submit():
        if not profile:
            profile = Profile(user_id=current_user.id)

        # Atualizar dados
        profile.telefone = form.telefone.data
        profile.instituicao = form.instituicao.data
        profile.cargo = form.cargo.data
        profile.bio = form.bio.data

        # Upload de foto (se houver)
        foto_file = form.foto.data
        if foto_file:
            # remover arquivos antigos
            remove_file_safe(profile.foto)
            remove_file_safe(profile.foto_thumb)

            filename, thumb = save_image(foto_file, user_name=user.nome)
            profile.foto = filename
            profile.foto_thumb = thumb

        # Se não houver imagem, gerar avatar automático
        elif not profile.foto and not profile.foto_thumb:
            _, thumb = save_image(None, user_name=user.nome)
            profile.foto_thumb = thumb

        db.session.add(profile)
        db.session.commit()
        flash("Perfil atualizado com sucesso!", "success")
        return redirect(url_for("users.profile"))

    # preencher form com dados existentes
    if profile and request.method == "GET":
        form.telefone.data = profile.telefone
        form.instituicao.data = profile.instituicao
        form.cargo.data = profile.cargo
        form.bio.data = profile.bio

    return render_template("users/profile.html", form=form, profile=profile)