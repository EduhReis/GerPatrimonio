from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from backend.models import Patrimonio, Funcionario, db

main = Blueprint('main', __name__)

@main.route('/<username>/cadastro', methods=['GET', 'POST'])
@login_required
def cadastro(username):
    if username != current_user.username:
        flash('Acesso negado.')
        return redirect(url_for('main.listagem', username=current_user.username))
    if request.method == 'POST':
        nome = request.form.get('nome')
        categoria = request.form.get('categoria')
        status = request.form.get('status')
        patrimonio = Patrimonio(nome=nome, categoria=categoria, status=status)
        db.session.add(patrimonio)
        db.session.commit()
        flash('Patrimônio cadastrado com sucesso!')
        return redirect(url_for('main.listagem', username=username))
    return render_template('cadastro.html')

@main.route('/<username>/cadastro_modal', methods=['GET', 'POST'])
@login_required
def cadastro_modal(username):
    if username != current_user.username:
        flash('Acesso negado.')
        return redirect(url_for('main.listagem', username=current_user.username))
    if request.method == 'POST':
        nome = request.form.get('nome')
        categoria = request.form.get('categoria')
        status = request.form.get('status')
        patrimonio = Patrimonio(nome=nome, categoria=categoria, status=status)
        db.session.add(patrimonio)
        db.session.commit()
        flash('Patrimônio cadastrado com sucesso!')
        return redirect(url_for('main.listagem', username=username))
    return render_template('cadastro_modal.html')

@main.route('/<username>/listagem')
@login_required
def listagem(username):
    if username != current_user.username:
        flash('Acesso negado.')
        return redirect(url_for('main.listagem', username=current_user.username))
    patrimonios = Patrimonio.query.all()
    return render_template('listagem.html', patrimonios=patrimonios)

@main.route('/<username>/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar(username, id):
    if username != current_user.username:
        flash('Acesso negado.')
        return redirect(url_for('main.listagem', username=current_user.username))
    patrimonio = Patrimonio.query.get_or_404(id)
    if request.method == 'POST':
        patrimonio.nome = request.form.get('nome')
        patrimonio.categoria = request.form.get('categoria')
        patrimonio.status = request.form.get('status')
        db.session.commit()
        flash('Patrimônio atualizado com sucesso!')
        return redirect(url_for('main.listagem', username=username))
    return render_template('editar.html', patrimonio=patrimonio)

@main.route('/<username>/apagar/<int:id>', methods=['POST'])
@login_required
def apagar(username, id):
    if username != current_user.username:
        flash('Acesso negado.')
        return redirect(url_for('main.listagem', username=current_user.username))
    patrimonio = Patrimonio.query.get_or_404(id)
    db.session.delete(patrimonio)
    db.session.commit()
    flash('Patrimônio apagado com sucesso!')
    return redirect(url_for('main.listagem', username=username))