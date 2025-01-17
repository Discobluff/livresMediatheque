from flask import Blueprint, render_template,request
from sqlite3 import connect

ajouterBp = Blueprint('ajouter', __name__,template_folder='templates')

@ajouterBp.route('/ajouter',methods=['GET'])
def ajouter():
    return render_template('ajouter.html')

@ajouterBp.route('/ajouter',methods=['POST'])
def ajouterISBN():
    data = request.json
    isbn = data['isbn']
    connection=connect('livres.db', check_same_thread=False)
    cursor=connection.cursor()
    cursor.execute('INSERT INTO Livre VALUES(?)',(isbn,))
    connection.commit()
    connection.close()
    return "Added successfully"