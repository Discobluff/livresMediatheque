from flask import Blueprint, render_template

accueilBp = Blueprint('accueil', __name__,template_folder='templates')

@accueilBp.route('/')
def home():
    return render_template('accueil.html')