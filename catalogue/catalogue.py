from flask import Blueprint, render_template,redirect
from sqlite3 import connect

catalogueBp = Blueprint('catalogue', __name__,template_folder='templates')

@catalogueBp.route('/catalogue')
def catalogue():
    connection=connect('livres.db', check_same_thread=False)
    cursor=connection.cursor()
    cursor.execute('SELECT * FROM Livre')
    livres=cursor.fetchall()
    connection.close()
    livres = [l[0] for l in livres]
    return render_template('catalogue.html',livres=livres)

@catalogueBp.route('/catalogue/supprimer/<int:isbn>')
def supprimer(isbn):
    connection=connect('livres.db', check_same_thread=False)
    cursor=connection.cursor()
    cursor.execute('DELETE FROM Livre WHERE isbn=?',(isbn,))
    connection.commit()
    connection.close()
    return redirect("/catalogue")