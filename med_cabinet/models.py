from os import getenv
import pandas as pd
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


DB = SQLAlchemy()
MIGRATE = Migrate()

def wrangle():
    """Split both effects and Flavor by comma, then lower case all data"""
    # Create a Copy
    df = pd.read_csv('cannabis.csv')
    df = df.copy()
    # Split both Effects and Flavor column by comma
    df1 = df['Effects'].str.split(',', expand=True)
    df2 = df['Flavor'].str.split(',', expand=True)
    # Rename new columns
    df1 = df1.add_prefix('Effects_')
    df2 = df2.add_prefix('Flavor_')
    # Drop original columns from DF
    df = df.drop(columns=['Effects','Flavor'])
    # Concat both DFs
    df = pd.concat([df, df1, df2], axis=1)
    # Lowercase columns
    df.columns = map(str.lower, df.columns)
    return df

def create_DB(df):
    """Connect to PostGresDB via sqlalchemy"""
    engine = DB.create_engine(getenv('DATABASE_URL'))
    return df.to_sql('cannabis', engine, if_exists='APPEND')