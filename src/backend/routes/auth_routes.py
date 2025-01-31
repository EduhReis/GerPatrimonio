from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from backend.models import User, db

auth = Blueprint('auth', __name__)

@auth.route('/')
def index():
    return redirect(url_for('auth.login'))

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Validação simples
        if not username or not password:
            flash('Por favor, preencha todos os campos.')
            return redirect(url_for('auth.login'))

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            if user.is_admin:
                return redirect(url_for('auth.admin'))
            else:
                return redirect(url_for('main.listagem', username=user.username))
        else:
            flash('Credenciais inválidas. Tente novamente.')
    return render_template('login.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    if not current_user.is_admin:
        flash('Acesso negado.')
        return redirect(url_for('main.listagem', username=current_user.username))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if User.query.filter_by(username=username).first():
            flash('Usuário já existe. Escolha outro nome.')
            return redirect(url_for('auth.admin'))
        user = User(username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash('Usuário criado com sucesso!')
        return redirect(url_for('auth.admin'))

    users = User.query.all()
    return render_template('admin.html', users=users)

@auth.route('/admin/delete/<int:id>', methods=['POST'])
@login_required
def delete_user(id):
    if not current_user.is_admin:
        flash('Acesso negado.')
        return redirect(url_for('main.listagem', username=current_user.username))

    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    flash('Usuário deletado com sucesso!')
    return redirect(url_for('auth.admin'))

@auth.route('/admin/deactivate/<int:id>', methods=['POST'])
@login_required
def deactivate_user(id):
    if not current_user.is_admin:
        flash('Acesso negado.')
        return redirect(url_for('main.listagem', username=current_user.username))

    user = User.query.get_or_404(id)
    user.deactivate()
    db.session.commit()
    flash('Usuário desativado com sucesso!')
    return redirect(url_for('auth.admin'))

@auth.route('/admin/activate/<int:id>', methods=['POST'])
@login_required
def activate_user(id):
    if not current_user.is_admin:
        flash('Acesso negado.')
        return redirect(url_for('main.listagem', username=current_user.username))

    user = User.query.get_or_404(id)
    user.activate()
    db.session.commit()
    flash('Usuário ativado com sucesso!')
    return redirect(url_for('auth.admin'))

@auth.route('/admin/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_user(id):
    if not current_user.is_admin:
        flash('Acesso negado.')
        return redirect(url_for('main.listagem', username=current_user.username))

    user = User.query.get_or_404(id)
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if User.query.filter_by(username=username).first() and username != user.username:
            flash('Usuário já existe. Escolha outro nome.')
            return redirect(url_for('auth.edit_user', id=id))
        user.username = username
        if password:
            user.set_password(password)
        db.session.commit()
        flash('Usuário atualizado com sucesso!')
        return redirect(url_for('auth.admin'))
    return render_template('edit_user.html', user=user)

@auth.route('/alterar_usuario', methods=['GET', 'POST'])
@login_required
def alterar_usuario():
    if request.method == 'POST':
        novo_username = request.form.get('username')
        if User.query.filter_by(username=novo_username).first():
            flash('Nome de usuário já existe. Escolha outro nome.')
            return redirect(url_for('auth.alterar_usuario'))
        current_user.username = novo_username
        db.session.commit()
        flash('Nome de usuário alterado com sucesso!')
        return redirect(url_for('main.listagem', username=current_user.username))
    return render_template('alterar_usuario.html')

@auth.route('/alterar_senha', methods=['GET', 'POST'])
@login_required
def alterar_senha():
    if request.method == 'POST':
        senha_atual = request.form.get('senha_atual')
        nova_senha = request.form.get('nova_senha')
        if not current_user.check_password(senha_atual):
            flash('Senha atual incorreta.')
            return redirect(url_for('auth.alterar_senha'))
        current_user.set_password(nova_senha)
        db.session.commit()
        flash('Senha alterada com sucesso!')
        return redirect(url_for('main.listagem', username=current_user.username))
    return render_template('alterar_senha.html')