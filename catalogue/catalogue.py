from flask import Blueprint, render_template,redirect,request
from sqlite3 import connect

catalogueBp = Blueprint('catalogue', __name__,template_folder='templates')

@catalogueBp.route('/catalogue')
def catalogue():
    connection=connect('livres.db', check_same_thread=False)
    cursor=connection.cursor()
    cursor.execute('SELECT * FROM Livre ORDER BY Titre')
    livres=cursor.fetchall()
    connection.close()
    return render_template('catalogue.html',livres=livres)

@catalogueBp.route('/catalogue/supprimer/<int:isbn>')
def supprimer(isbn):
    connection=connect('livres.db', check_same_thread=False)
    cursor=connection.cursor()
    cursor.execute('DELETE FROM Livre WHERE isbn=?',(isbn,))
    connection.commit()
    connection.close()
    return redirect("/catalogue")

@catalogueBp.route('/catalogue/rechercher',methods=['POST'])
def chercher():
    data = request.form
    livre = data['searchBook']
    auteur = data['searchAuthor']
    split = auteur.split(' ')
    connection=connect('livres.db', check_same_thread=False)
    cursor=connection.cursor()
    ids = []
    if len(split)==1:
        cursor.execute('SELECT id FROM Auteur WHERE nom LIKE ? OR prenom LIKE ?',(split[0]+"%",split[0]+"%"))
        ids = cursor.fetchall()
        ids = [id[0] for id in ids]
    else:
        cursor.execute('SELECT id FROM Auteur WHERE (nom LIKE ? AND prenom LIKE ?) OR (nom LIKE ? AND prenom LIKE ?) OR (nom LIKE ?)',(split[1]+"%",split[0]+"%",split[0]+"%",split[1]+"%"," ".join(split)+"%"))
        ids = cursor.fetchall()
        ids = [id[0] for id in ids]    
    placeholders = ",".join("?" for _ in ids)    
    cursor.execute(f"SELECT * FROM Livre WHERE titre LIKE ? AND (? OR auteur IN ({placeholders}))",(livre+"%",auteur=="")+tuple(ids))
    livres = cursor.fetchall()
    connection.commit()
    connection.close()
    return render_template('catalogue.html',livres=livres)