import os
import pymongo
import bcrypt
from flask import Flask, render_template, request, flash, session, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

# Initilize connection
app.config["MONGO_DBNAME"] = 'BakingMaster'
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.secret_key = os.environ.get('SECRET_KEY')
mongo = PyMongo(app)

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
@app.route('/register', methods=["GET", "POST"])
def register():
    """
    This function is rendering user registration template, when form is validated, new user is added into database.
    """
    if request.method == "POST":
        users = mongo.db.Users
        
        """ Request information from user form """
        req = request.form
        
        """ Get all necessery variables from user form"""
        name = req.get('name')
        email = req.get('email')
        password = req.get('password')
        
        """ Check if users exist in databas """
        current_user = users.find_one({'email': email})
        if current_user is None:
            
            """ Insert one record to database """
            users.insert_one({
                'name' : name,
                'email' : email,
                'password' : password
            })
            flash('Your account was created successfully! Enjoy browsing our amazing recipes','success')
            return render_template('pages/login.html', body_id='login-page', title='Sign In')
        flash('This email account already exist in our records. Please use different email addres or recover your password','error')
            
    """ Return register template """
    return render_template('pages/register.html', body_id='register-page', title='Register account')

# Password Recovery Page
@app.route('/recovery')
def recovery():
    return render_template('pages/recovery.html', body_id='recovery-page', title='Password recovery')

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