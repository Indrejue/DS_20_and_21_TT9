from os import getenv
import pandas as pd
from flask import Flask, flash, redirect, render_template, request, session, abort
from pandas.core.base import DataError
from .models import flavors, effects, ailments, categories
import joblib


def create_app():
    app = Flask(__name__)
    model = joblib.load('predictor.joblib')
    weed = pd.read_csv('Data/weed.csv')

    @app.route('/')
    def confirm():
        return render_template('confirm.html', title="Confirm")

    @app.route('/home', methods=['GET', 'POST'])
    def home():
        categories1 = request.form.getlist('mycategories')
        ailments1 = request.form.getlist('myailments')
        effects1 = request.form.getlist('myeffects')
        flavors1 = request.form.getlist('myflavors')
        data = [categories1, ailments1, effects1, flavors1]
        df = pd.DataFrame(data)
        df.to_csv('data.csv')
        return render_template('home.html', title="Home", categories=categories,
                                ailments=ailments, effects=effects, flavors=flavors)
    
    @app.route('/results', methods=['GET', 'POST'])
    def results():
        df = pd.read_csv('data.csv')
        out = model.kneighbors([df.iloc[0].values])
        indexs = out[1].flat[0:5].tolist()
        pred = df.iloc[indexs]
        message = (str(df.columns) + str(df.shape) + str(df.values))
        return render_template('results.html', title="results", message=message, results=pred)


    @app.route('/about')
    def about():
        return render_template('about.html', title="about")

    @app.route('/insights')
    def insights():
        return render_template('insights.html', title="insights")
    

    return app


