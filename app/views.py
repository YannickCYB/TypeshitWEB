from flask import render_template, flash, redirect, url_for
from app import app, models 
from app.forms import DevisForm
from .models import db, Service


@app.route('/', methods=['GET'])
def route_racine():
    return models.main_page()

@app.route('/accueil', methods=['GET'])
def route_accueil():
    return models.main_page()

@app.route('/service', methods=['GET'])
def route_service():
    return models.service_page()

@app.route('/test_services', methods=['GET'])
def route_teste_services():
    return models.test_services_page()

@app.route('/devis', methods=['GET', 'POST'])
def route_devis():
    form = DevisForm()
    if form.validate_on_submit():
        flash('Votre demande de devis a été envoyée avec succès!', 'success')
        return redirect(url_for('confirmation_devis'))
    return models.devis_page(form)

@app.route('/confirmation_devis', methods=['GET'])
def route_confirmation_devis():
    return models.confirmation_devis_page()

@app.route('/service/<int:service_id>', methods=['GET'])
def route_service_detail(service_id):
    service = Service.query.get_or_404(service_id)
    return render_template('service_detail.html', service=service)
