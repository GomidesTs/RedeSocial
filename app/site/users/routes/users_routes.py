from flask import Blueprint, render_template, request, redirect, url_for, session
from app.config.config import db, Users, Publications


users = Blueprint('users_routes', __name__, url_prefix = '/users' ,template_folder = 'templates')


@users.route('/registration', methods=['GET', 'POST'])
def registration_users():
    if request.method == 'GET':
            return render_template('registration/registration.html')
    else:
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        user = request.form['user']
            
        if name and email and password and user:
            us = Users(name, email, password, user)
            db.session.add(us)
            db.session.commit()
                
        return redirect(url_for('index_routes.login_index'))
    

@users.route('/options', methods=['GET', 'POST'])
def options_users():
    if request.method == 'GET':
        return render_template('options/options.html')
    else:
        pu = Publications.query.filter_by(user=session['user_login'])
        return render_template('user_page/user_page.html', l=pu)


@users.route('/update', methods=['GET', 'POST'])
def update_users():
    us = Users.query.filter_by(user= session['user_login']).first()

    if request.method == 'POST':
        nome = request.form['name']
        email = request.form['email']
        password = request.form['password']
        user = request.form['user']

        if nome and email and password and user:
            us.nome = nome
            us.email = email
            us.password = password
            us.user = user

            db.session.commit()
            
            return redirect(url_for('users_routes.options_users'))
    
    us = Users.query.filter_by(user= session['user_login'])

    return render_template('update/update.html', l=us)


@users.route('/delete')
def delete_users():
    us = Users.query.filter_by(user=session['user_login']).first()

    db.session.delete(us)
    db.session.commit()

    return redirect(url_for('index_routes.index_index'))

