from flask import Flask
from .views import views
from .auth import auth
from os import path
from .models import db

DB_NAME = 'database.db'


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Himanshu is Sexy'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    create_database(app)

    return app


def create_database(app):
    if not path.exists('webstie/' + DB_NAME):
        db.create_all(app=app)
        print('Database Created!')
