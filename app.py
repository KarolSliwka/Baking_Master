import os
from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('layout/base.html')

@app.route('/recipes')
def recipes():
    return  render_template('pages/recipes.html')
    
@app.route('/favouries')
def favourites():
    return render_template('pages/favourites.html')
    
@app.route('/search_results')
def search_results():
    return render_template('pages/search-results.html')

@app.route('/contact')
def contact():
    return render_template('pages/contact.html')
    
@app.route('/login')
def login():
    return render_template('pages/login.html')
    
@app.route('/register')
def register():
    return render_template('pages/register.html')
    
@app.route('/pass-recovery')
def recovery():
    return render_template('pages/pass-recovery.html')

@app.route('/about')
def about():
    return  render_template('pages/about.html')
    
@app.route('/site-map')
def site_map():
    return  render_template('pages/site-map.html')

@app.route('/equipment')
def equipment():
    return  render_template('pages/equipment.html')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)