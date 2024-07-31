#!/usr/bin/env python3
"""Basic Flask App"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    """ Configuration for Babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@app.route('/')
def index():
    """ Index route that returns content of the index page
    """
    return render_template("5-index.html")


@babel.localeselector
def get_locale():
    """ Determines the best language match with the predefined/supported
        languages in the Config class
    """
    locale = request.args.get("locale")
    if locale and locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """ Returns a dictionary
    """
    login_as = request.args.get("login_as")
    if login_as:
        id = int(login_as)
        return users.get(id)
    return None


@app.before_request
def before_request():
    """ Executes before any other function
    """
    g.user = get_user()


if __name__ == "__main__":
    app.run(debug=True)
