from os import getenv
from flask import Flask, flash, redirect, render_template, request, session, abort


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def confirm():
        return render_template('confirm.html', title="Confirm")

    @app.route('/home')
    def home():
        return render_template('home.html', title="Home")

    @app.route('/about')
    def about():
        return render_template('about.html', title="about")
    

    return app


