from flask import Flask
from app.site.index.routes.index_routes import index
from app.site.users.routes.users_routes import users
from app.site.publications.routes.publications_routes import publications
# Applying the flask one to be used
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Gomidests'

# Recording blueprints
app.register_blueprint(index)
app.register_blueprint(users)
app.register_blueprint(publications)

# Site running 
if __name__ == '__main__':
    app.run(debug=True) 