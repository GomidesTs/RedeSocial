from app.site.users.routes.users_routes import users
from flask import Blueprint, render_template, request, redirect, url_for, session
from app.config.config import db, Publications

publications = Blueprint('publications_routes', __name__, url_prefix = '/publications' ,template_folder = 'templates')


@publications.route('/')
def index_publications():
    pu = Publications.query.all()
    return render_template ('index/index_publications.html', l=pu)


@publications.route('/registration',methods=['GET', 'POST'])
def registration_publications():
    if request.method == 'GET':
        return render_template ('registration/registration_publictions.html')
    else:
        name = request.form['name']
        autor = request.form['autor']
        text = request.form['text']
        users = session['user_login']
        if name and autor and text and users:
        
            pu = Publications(name,autor,text,users)
            db.session.add(pu)
            db.session.commit()

        return redirect(url_for('publications_routes.index_publications'))

@publications.route('/update')
def update_publications():
    return render_template('update/update.html')


@publications.route('/DeletePost/<id>')
def delete_publications(id):
    pu = Publications.query.filter_by(id=id).first()

    db.session.delete(pu)
    db.session.commit()

    pu = Publications.query.filter_by(users=session['user_login'])
    return redirect(url_for('users_routes.options_users'))
