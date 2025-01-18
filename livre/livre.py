from flask import Blueprint, render_template
import main

livreBp = Blueprint('livre', __name__,template_folder='templates')

@livreBp.route('/livre/<string:isbn>')
def home(isbn):
    title, author, image = main.getData(isbn, True)
    return render_template('livre.html',livre=[isbn,title,author,image])