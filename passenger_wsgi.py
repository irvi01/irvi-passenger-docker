import sys
from main import app, db
from app.models import User, Item

sys.path.insert(0, "/opt/app")

with app.app_context():
    db.create_all()

from main import app as application
