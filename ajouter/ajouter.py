from flask import Blueprint, render_template,request,jsonify
from sqlite3 import connect,IntegrityError
from main import *

ajouterBp = Blueprint('ajouter', __name__,template_folder='templates')

@ajouterBp.route('/ajouter',methods=['GET'])
def ajouter():
    return render_template('ajouter.html')

@ajouterBp.route('/ajouter',methods=['POST'])
def ajouterISBN():
    data = request.json
    isbn = data['isbn']
    print(isbn)
    title, author,_ = getData(isbn)
    split = author.split(' ')
    if len(split) == 1:
        prenom = ""
        nom = split[0]
    else:
        prenom = split[0]
        nom = " ".join(split[1:])
    connection=connect('livres.db', check_same_thread=False)
    cursor=connection.cursor()
    cursor.execute('SELECT id FROM Auteur WHERE nom=? AND prenom=?',(nom,prenom))
    id = cursor.fetchone()    
    if id == None:
        cursor.execute('INSERT INTO Auteur VALUES(NULL,?,?)',(nom,prenom))
        cursor.execute('SELECT id FROM Auteur WHERE nom=? AND prenom=?',(nom,prenom))
        id = cursor.fetchone()
    id = id[0]    
    try:
        cursor.execute('INSERT INTO Livre VALUES(?,?,?)',(isbn,title,id))
        connection.commit()
    except:
        connection.close()
        raise Exception()
    connection.close()
    return jsonify({"title":title,"author":author})