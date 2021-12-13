#!/usr/bin/env python3
"""
Basic babel flask app.

Uses Config to set Babel's default local <en>
and timezone <UTC>

Uses that class as config for flask app.
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    Configure Babel.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


@babel.localeselector
def get_locale():
    """
    Get locale from flask.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """
    Get timezone from flask.
    """
    user = getattr(g, 'user', None)
    if user is not None:
        return user.timezone


@app.route('/')
def index():
    """
    Return the index page.
    """
    return render_template('1-index.html')


app.config.from_object(Config)
if __name__ == '__main__':
    app.run(debug=True)
