from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class DevisForm(FlaskForm):
    genre = SelectField('Genre', choices=[('', 'Sélectionnez un genre'), ('homme', 'Homme'), ('femme', 'Femme'), ('non-binaire', 'Non-binaire')], validators=[DataRequired()])
    nom = StringField('Nom', validators=[DataRequired(), Length(max=64)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=64)])
    message = TextAreaField('Développement de votre demande', validators=[DataRequired(), Length(max=500)])
    submit = SubmitField('Envoyer')

