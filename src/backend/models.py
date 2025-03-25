from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import UserMixin

db = SQLAlchemy()
bcrypt = Bcrypt()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    active = db.Column(db.Boolean, default=True)
    cargo = db.Column(db.String(50), nullable=False)  # Novo campo

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def deactivate(self):
        self.active = False

    def activate(self):
        self.active = True

    @property
    def is_active(self):
        return self.active

class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), unique=True, nullable=False)
    
class Patrimonio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'), nullable=False)
    categoria = db.relationship('Categoria', backref=db.backref('patrimonios', lazy=True))
    status = db.Column(db.String(20))
    versao = db.Column(db.Integer, nullable=False, default=1)  # Novo campo de versão
    funcionario_id = db.Column(db.Integer, db.ForeignKey('funcionario.id'), nullable=True)
    funcionario = db.relationship('Funcionario', back_populates='patrimonios')

class Funcionario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    cargo = db.Column(db.String(20), nullable=False)
    telefone = db.Column(db.String(12))
    patrimonios = db.relationship('Patrimonio', back_populates='funcionario')