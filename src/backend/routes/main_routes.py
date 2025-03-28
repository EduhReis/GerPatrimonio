from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from backend.models import Patrimonio, Funcionario, Categoria, db

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
    categorias = Categoria.query.all()
    if request.method == 'POST':
        nome = request.form.get('nome')
        categoria_id = request.form.get('categoria_id')
        status = request.form.get('status')
        patrimonio = Patrimonio(nome=nome, categoria_id=categoria_id, status=status)
        db.session.add(patrimonio)
        db.session.commit()
        flash('Patrimônio cadastrado com sucesso!')
        return redirect(url_for('main.listagem', username=username))
    return render_template('cadastro.html', categorias=categorias)

@main.route('/<username>/cadastro_modal', methods=['GET', 'POST'])
@login_required
def cadastro_modal(username):
    if username != current_user.username or current_user.cargo not in ['Admin', 'Supervisor']:
        flash('Acesso restrito.')
        return redirect(url_for('main.listagem', username=current_user.username))
    categorias = Categoria.query.all()
    if request.method == 'POST':
        nome = request.form.get('nome')
        categoria_id = request.form.get('categoria_id')
        status = request.form.get('status')
        patrimonio = Patrimonio(nome=nome, categoria_id=categoria_id, status=status)
        db.session.add(patrimonio)
        db.session.commit()
        flash('Patrimônio cadastrado com sucesso!')
        return redirect(url_for('main.listagem', username=username))
    return render_template('cadastro_modal.html', categorias=categorias)

@main.route('/<username>/listagem')
@login_required
def listagem(username):
    if username != current_user.username:
        flash('Acesso restrito.')
        return redirect(url_for('main.index', username=current_user.username))
    
    # Aplicar filtros
    query = Patrimonio.query.filter_by(ativo=True)  # Filtra apenas patrimônios ativos
    nome = request.args.get('nome')
    categoria = request.args.get('categoria')
    status = request.args.get('status')
    
    if nome:
        query = query.filter(Patrimonio.nome.ilike(f'%{nome}%'))
    if categoria:
        query = query.filter(Patrimonio.categoria.has(nome=categoria))
    if status:
        query = query.filter(Patrimonio.status == status)
    
    patrimonios = query.all()
    categorias = Categoria.query.all()
    return render_template('index.html', patrimonios=patrimonios, categorias=categorias)

@main.route('/<username>/editar/<int:id>', methods=['POST'])
@login_required
def editar(username, id):
    if username != current_user.username or current_user.cargo not in ['Admin', 'Supervisor']:
        flash('Acesso restrito.')
        return redirect(url_for('main.listagem', username=current_user.username))
    
    patrimonio = Patrimonio.query.get_or_404(id)

    # Marcar a versão atual como inativa
    patrimonio.ativo = False
    db.session.commit()

    # Criar uma nova versão do patrimônio
    nova_versao = Patrimonio(
        nome=request.form.get('nome'),
        categoria_id=request.form.get('categoria_id'),
        status=request.form.get('status'),
        versao=patrimonio.versao + 1,
        ativo=True,
        funcionario_id=patrimonio.funcionario_id
    )
    db.session.add(nova_versao)
    db.session.commit()

    flash('Patrimônio atualizado com sucesso!')
    return redirect(url_for('main.listagem', username=username))

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

@main.route('/<username>/categorias', methods=['GET', 'POST'])
@login_required
def categorias(username):
    if username != current_user.username or current_user.cargo not in ['Admin', 'Supervisor']:
        flash('Acesso restrito.')
        return redirect(url_for('main.listagem', username=current_user.username))
    
    if request.method == 'POST':
        nome = request.form.get('nome')
        if Categoria.query.filter_by(nome=nome).first():
            flash('Categoria já existe. Escolha outro nome.')
            return redirect(url_for('main.categorias', username=username))
        categoria = Categoria(nome=nome)
        db.session.add(categoria)
        db.session.commit()
        flash('Categoria criada com sucesso!')
        return redirect(url_for('main.categorias', username=username))
    
    categorias = Categoria.query.all()
    return render_template('categorias.html', categorias=categorias)

@main.route('/<username>/editar_categoria/<int:id>', methods=['POST'])
@login_required
def editar_categoria(username, id):
    if username != current_user.username or current_user.cargo not in ['Admin', 'Supervisor']:
        flash('Acesso restrito.')
        return redirect(url_for('main.categorias', username=current_user.username))
    
    categoria = Categoria.query.get_or_404(id)
    nome = request.form.get('nome')
    if Categoria.query.filter_by(nome=nome).first() and nome != categoria.nome:
        flash('Categoria já existe. Escolha outro nome.')
        return redirect(url_for('main.categorias', username=username))
    
    categoria.nome = nome
    db.session.commit()
    flash('Categoria editada com sucesso!')
    return redirect(url_for('main.categorias', username=username))

@main.route('/<username>/remover_categoria/<int:id>', methods=['POST'])
@login_required
def remover_categoria(username, id):
    if username != current_user.username or current_user.cargo not in ['Admin', 'Supervisor']:
        flash('Acesso restrito.')
        return redirect(url_for('main.categorias', username=current_user.username))
    
    categoria = Categoria.query.get_or_404(id)
    db.session.delete(categoria)
    db.session.commit()
    flash('Categoria removida com sucesso!')
    return redirect(url_for('main.categorias', username=username))