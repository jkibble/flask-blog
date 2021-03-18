from flask import Flask, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_babel import Babel, _

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'this is the secret key'
app.config['REMEMBER_COOKIE_HTTPONLY'] = True
app.config['REMEMBER_COOKIE_REFRESH_EACH_REQUEST'] = True
app.config['LANGUAGES'] = ['en', 'de', 'es']
app.config['BABEL_DEFAULT_LOCALE'] = 'de'

login = LoginManager(app)
db = SQLAlchemy(app)
babel = Babel(app)
csrf = CSRFProtect()

print(f'{__name__} starting')

import blog.routes
import blog.commands


@babel.localeselector
def get_locale():
    if session.get('language'):
        return session['language']

    return request.accept_languages.best_match(app.config['LANGUAGES'])
