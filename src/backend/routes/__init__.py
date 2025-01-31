from .auth_routes import auth
from .main_routes import main

def register_routes(app):
    """Carrega automaticamente todas as rotas na pasta routes."""
    app.register_blueprint(auth)
    app.register_blueprint(main)