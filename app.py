# Modules
from flask import Flask

# Controleurs
from accueil.accueil import accueilBp
from catalogue.catalogue import catalogueBp
from ajouter.ajouter import ajouterBp
from livre.livre import livreBp

# initialisation de l'app
def appInit():
    app = Flask(__name__)
    app.secret_key='SOME_SECRET'

    app.register_blueprint(accueilBp)
    app.register_blueprint(catalogueBp)
    app.register_blueprint(ajouterBp)
    app.register_blueprint(livreBp)

    return app

app = appInit()
# execution
if __name__ == '__main__':
    app.run(debug=True)