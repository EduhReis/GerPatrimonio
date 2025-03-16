import os
from backend import create_app
from backend.models import db, User, Patrimonio, Funcionario

app = create_app()

with app.app_context():
    db.drop_all() 
    db.create_all()

    # Criar usuário admin
    admin = User(username='admin', is_admin=True, cargo='Admin')
    admin.set_password('admin')
    db.session.add(admin)

    # Criar alguns funcionários
    funcionario1 = Funcionario(nome='João Silva', cpf='12345678901', cargo='Gerente', telefone='123456789')
    funcionario2 = Funcionario(nome='Maria Souza', cpf='10987654321', cargo='Assistente', telefone='987654321')
    db.session.add(funcionario1)
    db.session.add(funcionario2)

    # Criar alguns patrimônios
    patrimonio1 = Patrimonio(nome='Computador', categoria='Eletrônicos', status='Ativo', funcionario=funcionario1)
    patrimonio2 = Patrimonio(nome='Mesa', categoria='Móveis', status='Inativo', funcionario=funcionario2)
    db.session.add(patrimonio1)
    db.session.add(patrimonio2)

    db.session.commit()