
from flask import render_template
from . import db

#Les routes
def main_page():
    return render_template("accueil.html")

# READ DANS MON CRUD
def service_page():
    services = Service.query.all()
    return render_template("service.html", services=services)

#def devis_envoye_page():
    # Récupérer les données du formulaire
    # Insérer ces données dans la base de données

#   return render_template("devis_envoye.html")
def test_services_page():
    services = Service.query.all()
    return render_template('test_service.html',services=services)

def devis_page(form):
    return render_template('devis.html', title='Devis', form=form)

def confirmation_devis_page():
    return render_template('confirmation_devis.html', title='Confirmation de Devis')

#BDD
class ClientAccount(db.Model):
    __tablename__ = 'client_accounts'


    id = db.Column(db.SmallInteger().with_variant(db.Integer, 'sqlite'), primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return f"ClientAccount('{self.username}')"


class Client(db.Model):
    __tablename__ = 'clients'
    
    id = db.Column(db.SmallInteger().with_variant(db.Integer, 'sqlite'), primary_key=True, autoincrement=True)
    id_account = db.Column(db.SmallInteger().with_variant(db.Integer, 'sqlite'), db.ForeignKey('client_accounts.id'), nullable=False)
    firstname = db.Column(db.String(64), nullable=False)
    lastname = db.Column(db.String(64), nullable=False)
    mail = db.Column(db.String(64), nullable=False)
    phone = db.Column(db.String(16), nullable=False)

    # Relation avec la table client_accounts
    account = db.relationship('ClientAccount', backref=db.backref('clients', lazy=True))

    def __repr__(self):
        return f"Client('{self.firstname}', '{self.lastname}', '{self.mail}', '{self.phone}')" #representation en chaine de caractère


class EmployeeAccount(db.Model):
    __tablename__ = 'employee_accounts'
    
    id = db.Column(db.SmallInteger().with_variant(db.Integer, 'sqlite'), primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return f"EmployeeAccount('{self.username}')"

class Employee(db.Model):
    __tablename__ = 'employees'
    
    id = db.Column(db.SmallInteger().with_variant(db.Integer, 'sqlite'), primary_key=True, autoincrement=True)
    id_account = db.Column(db.SmallInteger().with_variant(db.Integer, 'sqlite'), db.ForeignKey('employee_accounts.id'), nullable=False)
    firstname = db.Column(db.String(64), nullable=False)
    lastname = db.Column(db.String(64), nullable=False)
    mail = db.Column(db.String(64), nullable=False)
    phone = db.Column(db.String(16), nullable=False)

    account = db.relationship('EmployeeAccount', backref=db.backref('employees', lazy=True))

    def __repr__(self):
        return f"Employee('{self.firstname}', '{self.lastname}', '{self.mail}', '{self.phone}')"

class Devis(db.Model):
    __tablename__ = 'devis'
    
    id = db.Column(db.SmallInteger().with_variant(db.Integer, 'sqlite'), primary_key=True, autoincrement=True)
    id_client = db.Column(db.SmallInteger().with_variant(db.Integer, 'sqlite'), db.ForeignKey('clients.id'), nullable=False)
    id_employee = db.Column(db.SmallInteger().with_variant(db.Integer, 'sqlite'), db.ForeignKey('employees.id'), nullable=False)

    
    client = db.relationship('Client', backref=db.backref('devis', lazy=True))
    employee = db.relationship('Employee', backref=db.backref('devis', lazy=True))

    def __repr__(self):
        return f"Devis('{self.id}', 'Client ID: {self.id_client}', 'Employee ID: {self.id_employee}')"

class DevisDetail(db.Model):
    __tablename__ = 'devis_details'
    
    id = db.Column(db.SmallInteger().with_variant(db.Integer, 'sqlite'), primary_key=True, autoincrement=True)
    id_devis = db.Column(db.SmallInteger().with_variant(db.Integer, 'sqlite'), db.ForeignKey('devis.id'), nullable=False)
    id_service = db.Column(db.SmallInteger().with_variant(db.Integer, 'sqlite'), db.ForeignKey('services.id'), nullable=False)

    
    devis = db.relationship('Devis', backref=db.backref('devis_details', lazy=True))
    service = db.relationship('Service', backref=db.backref('devis_details', lazy=True))

    def __repr__(self):
        return f"DevisDetail('{self.id}', 'Devis ID: {self.id_devis}', 'Service ID: {self.id_service}')"

class Service(db.Model):
    __tablename__ = 'services'
    
    id = db.Column(db.SmallInteger().with_variant(db.Integer, 'sqlite'), primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(256))

    def __repr__(self):
        return f"Service('{self.name}')"
