#import dependencies
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#import Flask from sqlalchemy
from flask import Flask, jsonify


#setup database. This allows us to access and query the database
engine = create_engine("sqlite:///hawaii.sqlite")
#generate clases to reflect the database
Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

#create session link from python to database
session = Session(engine)

#set up Flask
app = Flask(__name__)

@app.route("/")
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')
    return