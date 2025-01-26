import unittest
from flask_testing import TestCase
from backend import create_app
from backend.models import db, User, Patrimonio, Funcionario

class TestCRUD(TestCase):

    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        return app

    def setUp(self):
        db.create_all()
        admin = User(username='admin', is_admin=True)
        admin.set_password('admin')
        db.session.add(admin)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_patrimonio(self):
        # Arrange
        patrimonio = Patrimonio(nome='Computador', categoria='Eletrônicos', status='Ativo')

        # Act
        db.session.add(patrimonio)
        db.session.commit()

        # Assert
        self.assertEqual(Patrimonio.query.count(), 1)
        self.assertEqual(Patrimonio.query.first().nome, 'Computador')

    def test_create_funcionario(self):
        # Arrange
        funcionario = Funcionario(nome='João Silva', cpf='12345678902', cargo='Gerente', telefone='123456789')

        # Act
        db.session.add(funcionario)
        db.session.commit()

        # Assert
        self.assertEqual(Funcionario.query.count(), 1)
        self.assertEqual(Funcionario.query.first().nome, 'João Silva')

if __name__ == '__main__':
    unittest.main()