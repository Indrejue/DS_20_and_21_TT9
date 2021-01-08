from os import getenv, getcwd
import pandas as pd
from flask import Flask, flash, redirect, render_template, request, session, abort
from pandas.core.base import DataError
from .models import flavors, effects, ailments, categories, columns
import joblib


model = joblib.load('predictor.joblib')
weed = pd.read_csv('Data/weed.csv')

def order_data(c, a, e, f):
    df = pd.DataFrame(data=[[0]*len(columns)], columns=columns)
    for val in c + a + e + f:
        df[val] = 1
    return df
    


def create_app():
    app = Flask(__name__, )

    @app.route('/')
    def confirm():
        return render_template('confirm.html', title="Confirm")

    @app.route('/home', methods=['GET', 'POST'])
    def home():
        return render_template('home.html', title="Home", categories=categories,
                                ailments=ailments, effects=effects, flavors=flavors)
    
    @app.route('/results', methods=['GET', 'POST'])
    def results():
        categories1 = request.form.getlist('categories')
        ailments1 = request.form.getlist('ailments')
        effects1 = request.form.getlist('effects')
        flavors1 = request.form.getlist('flavors')
        df = order_data(categories1, ailments1, effects1, flavors1)
        out = model.kneighbors([df.iloc[0].values])
        indexs = out[1].flat[0:5].tolist()
        pred = weed.iloc[indexs]
        
        print(pred[['name', 'brand', 'strain', 'rating']])
        return render_template('results.html', title="Results", message="Based on the selected inputs, we suggest:", results=[f"{name} by {brand} (Strain: {strain})" for name, brand, strain, rating in pred[['name', 'brand', 'strain', 'rating']].values])

    @app.route('/about')
    def about():
        return render_template('about.html', title="About")

    @app.route('/insights')
    def insights():
        return render_template('insights.html', title="Insights")
    

    return app


