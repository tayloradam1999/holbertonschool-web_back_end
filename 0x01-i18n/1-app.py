#!/usr/bin/env python3
"""
Basic babel flask app.

Uses Config to set Babel's default local <en>
and timezone <UTC>

Uses that class as config for flask app.
"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    Configure Babel.
    """
    LANGUAGES = ['en', 'fr']


@babel.localeselector
def get_locale():
    """
    Get locale from flask.
    """
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/')
def index():
    """
    Return the index page.
    """
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
