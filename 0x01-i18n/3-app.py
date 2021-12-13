#!/usr/bin/env python3
"""
Basic babel flask app.

Uses Config to set Babel's default local <en>
and timezone <UTC>

Uses that class as config for flask app.

Uses gettext to parameterize templates using message IDS
'home_title' and 'home_header'.
"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext


app = Flask(__name__)
babel = Babel(app)


class Config():
    """
    Configure Babel.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
_ = gettext
print(_('home_title'))
print(_('home_header'))


@babel.localeselector
def get_locale():
    """
    Get locale from request.
    """
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/')
def index():
    """
    Return the index page.
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()
