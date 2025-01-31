import os
from flask import Flask
from flask_login import LoginManager
from .models import db, User
from flask_login import current_user

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sua-chave-secreta'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.abspath(os.path.join(os.path.dirname(__file__), "../infra/gerPtrimonio.db"))}'

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    @app.context_processor
    def inject_user():
        return dict(current_user=current_user)
    
    from .routes import register_routes
    register_routes(app)

    return app