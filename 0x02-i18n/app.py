#!/usr/bin/env python3
"""Basic Flask App"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime
import pytz


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
    g.time = format_datetime()
    return render_template("index.html")


@babel.localeselector
def get_locale():
    """ Determines the best language match with the predefined/supported
        languages in the Config class
    """
    locale = request.args.get("locale")
    if locale and locale in app.config["LANGUAGES"]:
        return locale

    elif g.user:
        user_settings = g.user.get("locale")
        if user_settings:
            if user_settings in app.config["LANGUAGES"]:
                return user_settings

    accept_langs = request.headers.get("Accept-Language")
    if accept_langs:
        langs = []
        for lang in accept_langs.split(","):
            langs.append(lang.split(";")[0])
        for lang in langs:
            if lang in app.config["LANGUAGES"]:
                return lang

    return app.config["BABEL_DEFAULT_LOCALE"]


@babel.timezoneselector
def get_timezone():
    """ Finds the user timezone
    """
    get_timezone = request.args.get("timezone")
    if get_timezone:
        try:
            timezone = pytz.timezone(get_timezone)
            return timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    elif g.user:
        user_timezone = g.user.get("timezone")
        if user_timezone:
            try:
                timezone_user = pytz.timezone(user_timezone)
                return timezone_user
            except pytz.exceptions.UnknownTimeZoneError:
                pass

    return pytz.timezone(app.config["BABEL_DEFAULT_TIMEZONE"])


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
