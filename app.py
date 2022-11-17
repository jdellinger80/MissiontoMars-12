from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import pprint
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
import requests
from splinter import Browser
from pathlib import Path
from bs4 import BeautifulSoup as soup
import datetime as dt
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from splinter import Browser
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import datetime as dt
import pandas as pd
import pytest
import time

app = Flask(__name__)

# init flask pymongo
app.config["MONGO_URI"] = "mongodb://localhost:27017/Mars_db"
mongo  = PyMongo(app)

# root route 
@app.route("/")
def index():
    mars_data= mongo.db.Info.find_one()
    return render_template("index.html", mars=mars_data)

# scrape route 
@app.route("/scrape")   # call scrape 
def scrape_all():

   # reference to table, drop if exists 
    Info = mongo.db.Info
    mongo.db.Info.drop()
    
    # call scrape script and insert into MongoDB
    mars_data = scrap_mars.scrape_all()
    Info.insert_one(mars_data)
    return redirect("/")

# scrape route 
if __name__ == "__main__":
    app.run()