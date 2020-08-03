from flask import Blueprint, render_template, request, redirect, url_for, session
from app.config.config import Users

index = Blueprint('index_routes', __name__,template_folder ='templates')

@index.route('/')
def index_index():
    return render_template('index/index.html')
    
@index.route('/login', methods=['GET', 'POST'])
def login_index():
    if request.method == 'GET':
        return render_template('login/login.html')
    else:
        user = request.form['user']
        password = request.form['password']
        
        us = Users.query.filter_by(user=user, password=password).first()
         
        if not us :
            return redirect(url_for('index_routes.login_index'))
        session['user_login'] = user
        return redirect(url_for('publications_routes.index_publications'))
    
@index.route('/logout')
def logout_index():
     session['user_login'] = None
     return redirect(url_for('index_routes.login_index'))