from os import getenv
from flask import Flask, flash, redirect, render_template, request, session, abort
from .models import flavors, effects, ailments, categories


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def confirm():
        return render_template('confirm.html', title="Confirm")

    @app.route('/home')
    def home():
#        categories1 = request.values['categories']
#        ailments1 = request.values['ailments']
#        effects1 = request.values['effects']
#        flavors1 = request.values['flavors']
        return render_template('home.html', title="Home", categories=categories,
                                ailments=ailments, effects=effects, flavors=flavors)

    @app.route('/about')
    def about():
        return render_template('about.html', title="about")

    @app.route('/insights')
    def insights():
        return render_template('insights.html', title="insights")
    

    return app


