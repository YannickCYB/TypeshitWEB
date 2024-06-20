
# Définition des la variables d'environnement pour l'hôte, le nom, l'utilisateur et le mot de passe de la base de données
DATABASE_HOST = 'localhost'
DATABASE_NAME = 'project'
DATABASE_USER = 'root'
DATABASE_PASS = 'root'


class Config:
    SECRET_KEY= 'CACAPIPI'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:root@localhost/typeshit'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

