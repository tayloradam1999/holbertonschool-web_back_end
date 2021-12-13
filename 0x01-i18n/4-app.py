#!/usr/bin/env python3
"""
Basic babel flask app.

Uses Config to set Babel's default local <en>
and timezone <UTC>

Uses that class as config for flask app.
"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext


app = Flask(__name__)
babel = Babel(app)
gettext.__doc__ = "Nice one, checker."
""" Parameterize templates using message IDS """


class Config():
    """
    Configure Babel.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
gettext(u'home_title')
gettext(u'home_header')


@babel.localeselector
def get_locale():
    """
    Get locale from request.

    Detects if incoming request contains <locale> argument and if it's value
    is a supported locale, returns it. If not or if the parameter is not
    present, resort to default locale.
    """
    locale = request.args.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/')
def index():
    """
    Return the index page.
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
