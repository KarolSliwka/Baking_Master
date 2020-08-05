import os
import bcrypt
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('layout/base.html', body_id='home-page')

@app.route('/recipes')
def recipes():
    return  render_template('pages/recipes.html', body_id='recipes-page')
    
@app.route('/favouries')
def favourites():
    return render_template('pages/favourites.html', body_id='favourites-page')
    
@app.route('/search_results')
def search_results():
    return render_template('pages/search-results.html', body_id='search-page')

@app.route('/contact')
def contact():
    return render_template('pages/contact.html', body_id='contact-page')
    
@app.route('/login')
def login():
    return render_template('pages/login.html', body_id='login-page')
    
@app.route('/register')
def register():
    return render_template('pages/register.html', body_id='register-page')
    
@app.route('/pass-recovery')
def recovery():
    return render_template('pages/pass-recovery.html', body_id='recovery-page')

@app.route('/about')
def about():
    return  render_template('pages/about.html', body_id='about-page')
    
@app.route('/site-map')
def site_map():
    return  render_template('pages/site-map.html', body_id='site-map-page')

@app.route('/equipment')
def equipment():
    return  render_template('pages/equipment.html', body_id='equipment-page')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)