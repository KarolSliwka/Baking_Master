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
    
@app.route('/my_account')
def my_account():
    return render_template('pages/my-account.html')   

@app.route('/about')
def about():
    return  render_template('pages/about.html')
    
@app.route('/site-map')
def site_map():
    return  render_template('pages/site-map.html')

@app.route('/equipement')
def equipement():
    return  render_template('pages/equipement.html')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)