#!/usr/bin/env python3
"""
Basic babel flask app.

Uses Config to set Babel's default local <en>
and timezone <UTC>

Uses that class as config for flask app.
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext


# Set up Flask app and tend to baby checker
app = Flask(__name__)
babel = Babel(app)
gettext.__doc__ = "Nice one, checker."
""" Tend to Turlay """


# simulate database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


# simulate getting user from databse
def get_user() -> users:
    """
    Returns user dictionary or None if ID cannot be found or
    if <login_as> was not passed.
    """
    user = request.args.get("login_as")
    if not user:
        return None
    try:
        user = int(user)
        if user < 1 or user > 4:
            raise Exception
    except Exception:
        return None
    return users[user]


# loads user before page is rendered, ignore empty line below :(

@app.before_request
def before_request():
    """
    Uses get_user() to find a user, if any, and set it as g.user.
    """
    user = get_user()
    if user:
        g.user = user
        text = gettext("You are logged in as {}").format(g.user["name"])
        return render_template("5-index.html", text=text)
    return render_template("5-index.html",
                           text=gettext("You are not logged in"))


# Simple Class to set Babel's default local and timezone
class Config():
    """
    Configure Babel.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Configure Flask
app.config.from_object(Config)
# use gettext for translations
gettext(u'home_title')
gettext(u'home_header')
gettext(u'home_text')


# Determins if en or fr
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


# index page
@app.route('/')
def index():
    """
    Return the index page.
    """
    return render_template('5-index.html')


# run app
if __name__ == '__main__':
    app.run()
