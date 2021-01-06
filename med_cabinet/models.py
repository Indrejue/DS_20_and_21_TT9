from os import getenv
import pandas as pd
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


DB = SQLAlchemy()
MIGRATE = Migrate()