import sys
sys.path.insert(0, 'src')

from backend import create_app
from backend.models import db

app = create_app()

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')