# Modules
from flask import Flask

# Controleurs
from accueil.accueil import accueilBp
from catalogue.catalogue import catalogueBp

# initialisation de l'app
def appInit():
    app = Flask(__name__)
    app.secret_key='SOME_SECRET'

    app.register_blueprint(accueilBp)
    app.register_blueprint(catalogueBp)

    return app

# execution
if __name__ == '__main__':
    app = appInit()
    app.run(debug=True)