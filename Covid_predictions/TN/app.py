import numpy as np
import sqlalchemy
import pandas as pd
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from collections import OrderedDict
from flask import Flask, jsonify, Response, render_template
import psycopg2
import datetime


# #################################################
# # Database Setup
# #################################################
# engine = create_engine('postgres+psycopg2://postgres:(password)@localhost:5432/Spotify')

# # reflect an existing database into a new model
# Base = automap_base()
# # reflect the tables
# Base.prepare(engine, reflect=True)


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


@app.route("/")
def index():
    """Return the homepage."""

    return render_template("index.html")


@app.route("/TNDeptHealth_counties")
def viz_counties():
    daily = "https://www.tn.gov/health/cedep/ncov.html"
    viral = pd.read_html(daily)
    df2 = viral[4]
    date = datetime.datetime.today()
    date_modify = str(date)
    date_for_export = date_modify[0:10]
    df2.to_csv('C:/Users/clayf/Documents/HOC/Covid_predictions/TN/Resources/' + date_for_export +'_counties.csv',index=False)
    viral_counties = df2.to_json(orient='columns')

    return viral_counties


@app.route("/TNDeptHealth_overall")
def viz_overall():
    daily = "https://www.tn.gov/health/cedep/ncov.html"
    viral = pd.read_html(daily)
    df = viral[0]
    date = datetime.datetime.today()
    date_modify = str(date)
    date_for_export = date_modify[0:10]
    df.to_csv('C:/Users/clayf/Documents/HOC/Covid_predictions/TN/Resources/' + date_for_export +'_overall.csv',index=False)
    viral_overall = df.to_json(orient='columns')

    return viral_overall


@app.route("/TNDeptHealth_age")
def viz_age():
    daily = "https://www.tn.gov/health/cedep/ncov.html"
    viral = pd.read_html(daily)
    df3 = viral[3]
    date = datetime.datetime.today()
    date_modify = str(date)
    date_for_export = date_modify[0:10]
    df3.to_csv('C:/Users/clayf/Documents/HOC/Covid_predictions/TN/Resources/' + date_for_export +'_age.csv',index=False)
    viral_age = df3.to_json(orient='columns')

    return viral_age


if __name__ == '__main__':
    app.run(debug=True)
