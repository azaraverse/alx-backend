#!/usr/bin/env python3
"""Basic Flask App"""
from flask import Flask, render_template, request
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
    return render_template("4-index.html")


@babel.localeselector
def get_locale():
    """ Determines the best language match with the predefined/supported
        languages in the Config class
    """
    locale = request.args.get("locale")
    if locale and locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


if __name__ == "__main__":
    app.run(debug=True)
