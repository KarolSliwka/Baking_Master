import os
import pymongo
import bcrypt
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "BakingMaster"
COLLECTION_NAME = "Users"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to database: %s") %e
        

conn = mongo_connect(MONGODB_URI)        

coll = conn[DBS_NAME][COLLECTION_NAME]

documents = coll.find()

for doc in documents:
    print(doc)


# Home page
@app.route('/')
@app.route('/home')
def home():
    return render_template('layout/base.html', body_id='home-page')

# All Recieps page
@app.route('/recipes')
def recipes():
    return  render_template('pages/recipes.html', body_id='recipes-page')
    
# Favourites Page
@app.route('/favouries')
def favourites():
    return render_template('pages/favourites.html', body_id='favourites-page')
    
# Search Page
@app.route('/search-results')
def search_results():
    return render_template('pages/search-results.html', body_id='search-page')

# Contact Page
@app.route('/contact')
def contact():
    return render_template('pages/contact.html', body_id='contact-page')
 
# Login Page   
@app.route('/login')
def login():
    return render_template('pages/login.html', body_id='login-page')
   
# Register Page 
@app.route('/register')
def register():
    return render_template('pages/register.html', body_id='register-page')
    
# Password Recovery Page
@app.route('/recovery')
def recovery():
    return render_template('pages/recovery.html', body_id='recovery-page')

# About Page
@app.route('/about')
def about():
    return  render_template('pages/about.html', body_id='about-page')
    
# Site Map Page
@app.route('/site-map')
def site_map():
    return  render_template('pages/site-map.html', body_id='site-map-page')
    
# Equipment Page
@app.route('/equipment')
def equipment():
    return  render_template('pages/equipment.html', body_id='equipment-page')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)