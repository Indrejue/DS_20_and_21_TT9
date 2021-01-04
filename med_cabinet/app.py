from os import getenv
from flask import Flask, render_template


def create_app():
    app = Flask(__name__)
    
    @app.route('/')
    def home():
        # show our html form to the user
        message = "Med Cabinet Login"
        return render_template("home.html", message = message)

    return app

