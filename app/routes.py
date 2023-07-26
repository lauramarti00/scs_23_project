from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import SearchForm
from app.models import *
#from models import * 

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    user = {'username': 'Laura'}
    # films = [
    #     {
    #         'title' : 'hp1',
    #         'author': 'J.K. Rowling'
            
    #     },
    #     {
    #         'title' : 'hp2',
    #         'author': 'J.K. Rowling'
    #     },
    #     {
    #         'title' : 'hp3',
    #         'author': 'J.K. Rowling'
    #     }
    # ]  

    
 
    form = SearchForm()
    if form.validate_on_submit():
        #flash('Film searched with title {}'.format(form.title.data))
        #return redirect(url_for('film_page'))
        film = getFilmByTitle(form.title.data)
        return render_template('index.html', title='Home', user=user, film=film, form=form)

    return render_template('index.html', title='Home', user=user, form=form)


@app.route('/film_page')
def film_page():
    return 'this is film page'