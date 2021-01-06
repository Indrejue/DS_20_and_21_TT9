from os import getenv
from flask import Flask, flash, redirect, render_template, request, session, abort
from .models import DB, MIGRATE


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    DB.init_app(app)
    MIGRATE.init_app(app, DB)

    @app.before_request
    def before_request():
        return render_template('login.html', title="Confirm")

    @app.route('/success', methods=["POST"])
    def home():
        if request.method == "POST":
            return render_template('base.html', title="Welcome")

    return app


