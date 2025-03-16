from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from backend.models import Patrimonio, Funcionario, db

main = Blueprint('main', __name__)

def check_access():
    if current_user.cargo not in ['Supervisor', 'Admin']:
        flash('Acesso restrito.')
        return redirect(url_for('main.listagem', username=current_user.username))

@main.route('/<username>/cadastro', methods=['GET', 'POST'])
@login_required
def cadastro(username):
    if username != current_user.username or current_user.cargo not in ['Admin', 'Supervisor']:
        flash('Acesso restrito.')
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
    if username != current_user.username or current_user.cargo not in ['Admin', 'Supervisor']:
        flash('Acesso restrito.')
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
        flash('Acesso restrito.')
        return redirect(url_for('main.listagem', username=current_user.username))
    
    # Aplicar filtros
    query = Patrimonio.query
    nome = request.args.get('nome')
    categoria = request.args.get('categoria')
    status = request.args.get('status')
    
    if nome:
        query = query.filter(Patrimonio.nome.ilike(f'%{nome}%'))
    if categoria:
        query = query.filter(Patrimonio.categoria.ilike(f'%{categoria}%'))
    if status:
        query = query.filter(Patrimonio.status == status)
    
    patrimonios = query.all()
    return render_template('listagem.html', patrimonios=patrimonios)

@main.route('/<username>/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar(username, id):
    if username != current_user.username or current_user.cargo not in ['Admin', 'Supervisor']:
        flash('Acesso restrito.')
        return redirect(url_for('main.listagem', username=current_user.username))
    patrimonio = Patrimonio.query.get_or_404(id)
    if request.method == 'POST':
        # Criar uma nova versão do patrimônio
        nova_versao = Patrimonio(
            nome=patrimonio.nome,
            categoria=patrimonio.categoria,
            status=request.form.get('status'),
            versao=patrimonio.versao + 1,
            funcionario_id=patrimonio.funcionario_id
        )
        db.session.add(nova_versao)
        db.session.commit()
        flash('Patrimônio atualizado com sucesso!')
        return redirect(url_for('main.listagem', username=username))
    return render_template('editar.html', patrimonio=patrimonio)

@main.route('/<username>/apagar/<int:id>', methods=['POST'])
@login_required
def apagar(username, id):
    if username != current_user.username or current_user.cargo not in ['Admin', 'Supervisor']:
        flash('Acesso restrito.')
        return redirect(url_for('main.listagem', username=current_user.username))
    patrimonio = Patrimonio.query.get_or_404(id)
    db.session.delete(patrimonio)
    db.session.commit()
    flash('Patrimônio apagado com sucesso!')
    return redirect(url_for('main.listagem', username=username))