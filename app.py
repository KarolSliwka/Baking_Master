import os
from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('layout/base.html')

# Navigation routes
@app.route('/recipes')
def recipes():
    return  render_template('pages/recipes.html')
    
@app.route('/favourite-list')
def favourites():
    return render_template('pages/favourites.html')
    
@app.route('/my-recipes')
def my_recipes():
    return render_template('pages/search-result.html')

@app.route('/contact')
def contact():
    return render_template('pages/contact.html')
    
@app.route('/my-account')
def my_account():
    return render_template('pages/my-account.html')   

# Footer Useful routes
@app.route('/what-is-all-about')
def about():
    return  render_template('pages/about.html')
    
@app.route('/site-map')
def site_map():
    return  render_template('pages/site-map.html')

@app.route('/backing-equipement')
def equipement():
    return  render_template('pages/equipement.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)