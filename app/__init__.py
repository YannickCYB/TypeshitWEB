from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Création de l'instance principale de l'application Flask
app = Flask(__name__)

# Chargement des configurations depuis le fichier config.py
app.config.from_object('config.Config')

# Initialisez SQLAlchemy avec l'application Flask ici
db = SQLAlchemy(app)

# Initialisez Flask-Migrate
migrate = Migrate(app, db)

# Importation des vues depuis le dossier app
from app import views, models



"""
V 0.1
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

migrate = Migrate()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from . import views
        return app





# Importer Flask pour la création de l'application
from flask import Flask

# Création de l'instance principale de l'application Flask
app = Flask(__name__)

# Chargement des configurations depuis le fichier config.py
app.config.from_object('config')

# Importation des vues depuis le dossier app
from app import views
"""