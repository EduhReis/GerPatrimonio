import os
from backend import create_app
from backend.models import db, User, Patrimonio, Funcionario, Categoria

app = create_app()

with app.app_context():
    db.drop_all() 
    db.create_all()

    # Criar usuário admin
    admin = User(username='admin', is_admin=True, cargo='Admin')
    admin.set_password('admin')
    db.session.add(admin)


    db.session.commit()