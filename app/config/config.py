from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


# Applying the flask one to be used
app = Flask(__name__)

# Configuring the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rede.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)


# Configuring the admin
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
admin = Admin(app, name='microblog', template_mode='bootstrap3')


# Creating user column
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(50),nullable=False)
    password = db.Column(db.String(50),nullable=False)
    user = db.Column(db.String(50),nullable=False)
    
    def __init__(self, name, email, password, user):
        self.name = name
        self.email = email
        self.password = password
        self.user = user


# Creating publications column 
class Publications(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50),nullable=False)
    autor = db.Column(db.String(50),nullable=False)
    text = db.Column(db.String(5000),nullable=False)
    user = db.Column(db.String(50),nullable=False)
    
    def __init__(self, name, autor, text, user):
        self.name = name
        self.autor = autor
        self.text = text
        self.user = user

# Creating DataBase
db.create_all()


# Creating ModelView admin
admin.add_view(ModelView(Users,db.session))
admin.add_view(ModelView(Publications,db.session))