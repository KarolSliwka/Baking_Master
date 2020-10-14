import os
import pymongo
import requests
import bcrypt
from flask import Flask, render_template, url_for, session, redirect, request, flash
from flask_mail import Mail
from flask_mail import Message
from threading import Thread
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from py_edamam import PyEdamam



""" Create HTTPS connection for all rdirected urls """
class ReverseProxied(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        scheme = environ.get('HTTP_X_FORWARDED_PROTO')
        if scheme:
            environ['wsgi.url_scheme'] = scheme
        return self.app(environ, start_response)

app = Flask(__name__)
app.wsgi_app = ReverseProxied(app.wsgi_app)

# Initilize connection
app.config["MONGO_DBNAME"] = os.getenv('MDB_NAME')
app.config["MONGO_URI"] = os.getenv('MONGO_URI')
app.secret_key = os.getenv('SECRET_KEY')
mongo = PyMongo(app)

# Flask email configuration
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = os.getenv('MAIL_PORT')
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.getenv('EMAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('EMAIL_PASSWORD')
mail = Mail(app)

#API config
API_ID = os.getenv('API_ID')
API_KEY = os.getenv('API_KEY')
def _force_https(app):
    def wrapper(environ, start_response):
        environ['wsgi.url_scheme'] = 'https'
        return app(environ, start_response)
    return wrapper
    
# Home page
@app.route('/')
def home():
    """Renders landing page/home page"""

    return render_template('pages/landing-page.html', body_id='home-page', title = "Home Page")

# All Recieps page
@app.route('/recipes', methods=["GET", "POST"])
def recipes():
    """
    Renders recipes search page and return search result
    """

    if request.method == "POST": 
        """ Request information from user form """
        req = request.form
        
        """ Get variable from user form"""
        search = req.get('search')
        
        """ Request serach from EDAMAM API """
        e = PyEdamam(recipes_appid=API_ID,recipes_appkey=API_KEY)
        dict = e.search_recipe(search)
        
        for recipe in dict:
            print(recipe)
            print(recipe.calories)
            print(recipe.ingredient_quantities)
    
        return  render_template('pages/recipes.html', body_id='recipes-page', search=search)
    
    return  render_template('pages/recipes.html', body_id='recipes-page')

# This Recipe
@app.route('/recipe', methods=["GET", "POST"])
def this_recipe():
    
    return (print('ready'))
    

# Contact Page
@app.route('/contact', methods=["GET", "POST"])
def contact():
    """
    This function is sending email from userform in contact page
    """
    if request.method == "POST":
        
        """ Request information from user form """
        req = request.form
        
        """ Get variable from user form"""
        username = req.get('contact-name')
        email_address = req.get('contact-email').lower()
        contact_message = req.get('contact-message')
        email_from = os.getenv('EMAIL_USERNAME')
            
        """ Run email application """
        def send_email(app, msg):
            with app.app_context():
                mail.send(msg)
        msg = Message()
        msg.subject = 'Message from contact form'
        msg.recipients = [email_from, email_address]
        msg.sender = email_from
        msg.html = render_template('components/emails/contact-email.html', username = username, contact_message = contact_message)
        Thread(target=send_email, args=(app, msg)).start()
        
        flash('Your message was sent successfully','contact-send')
    return render_template('pages/contact.html', body_id='contact-page', title="Contact Page")
 
# Login Page   
@app.route('/login', methods=["GET", "POST"])
def login():
    """
    This funciton will check if user exists in database.
    When exist, will go to account page. When failed, show flash message.
    """
    if request.method == "POST":
        users = mongo.db.Users
        """ Request information from user form """
        req = request.form
        
        """ Collect information from login form """
        email_login = req.get('email')
        password = req.get('password')

        """ Find user details """
        login_user = users.find_one({'email': email_login.lower()})
        result = users.find(login_user)
        for doc in result:
            username = doc["name"]
            
        """ Main login statement """
        if login_user:
            if bcrypt.hashpw(password.encode('utf-8'), login_user['password']) == login_user['password']:
                session['email'] = email_login
                session['name'] = username
                flash('You have been successfully logged in!')
                return redirect(url_for('user_menu'))   
            flash("Incorrect username or password / user doesn't exist.","incorrect-user")
            return redirect(url_for('login'))
        flash("Incorrect username or password / user doesn't exist.","incorrect-user")
    return render_template('pages/login.html', body_id='login-page', title='Sign In')
   
# Home page
@app.route('/user-menu')
def user_menu():
    """
    """
    return render_template("pages/index.html", body_id="user-menu", page_title="user-menu")

# User account page
@app.route('/account', methods=['GET','POST'])
def account():
    
    try:
        """ Return user acocunt page with user information """
        
        user_info = mongo.db.Users.find_one({'email': session['email']})
        user_info_collection = mongo.db.Users.find(user_info)
        """ Collect user details """
        for doc in user_info_collection:
            active_user = doc["name"]
            email = doc["email"]
            recipes_count = doc["recipes"]
            fav_recipe_count = len(doc['favourites'])

        return render_template("pages/account.html", body_id="user-account",page_title="Account",active_user=active_user,email=email,recipes_count=recipes_count,fav_recipe_count=fav_recipe_count)

    except:
        """
        Return user account page without user name
        """
        return render_template("pages/account.html", body_id="user-account", page_title="account")

# Add Recipe
@app.route('/add-recipe', methods=['GET','POST'])
def add_recipe():
    """
    """

    return render_template('pages/add-recipe.html')

# Edit Recipe
@app.route('/edit-recipe', methods=['GET','POST'])
def edit_recipe():
    """
    """

    return render_template('pages/edit-recipe.html')
 
# Your Recipes 
@app.route('/your-recipes', methods=['GET','POST'])
def your_recipes():
    """
    """

    return render_template('pages/your-recipes.html')   
    
# Add to Favourites
@app.route('/add-to-favourites', methods=['GET','POST'])
def add_to_favourites():
    """
    """

    
    
# Favourites Page
@app.route('/favourites')
def favourites():
    """
    Renders favourite page only when user is logged in
    """
    return render_template('pages/favourites.html', body_id='favourites-page')


# Register Page 
@app.route('/register', methods=["GET", "POST"])
def register():
    """
    This function is rendering user registration template.
    When form is validated correctly, new user is added into database.
    """
    if request.method == "POST":
        users = mongo.db.Users
        """ Request information from user form """
        req = request.form
        
        """ Get all necessery variables from user form"""
        name = req.get('name')
        email = req.get('email')
        password = req.get('password')
        hashpassword = bcrypt.hashpw(
                    password.encode('utf-8'), bcrypt.gensalt())
        empty_favourites = []
        
        """ Check if users exist in databas """
        current_user = users.find_one({'email': email})
        if current_user is None:
            
            """ Insert new user, new record to database """
            users.insert_one({
                'name' : name,
                'email' : email.lower(),
                'password' : hashpassword,
                'newsletter' : 'Y',
                'favourites' : empty_favourites,
                'recipes': 0
            })
            
            """ Use add to newsletter funtcion to add new user to newsletter database """
            login_newsletter = email
            add_to_newsletter(login_newsletter)
        
            flash('Your account was created successfully! Enjoy browsing our amazing recipes','register-added')
            return render_template('pages/login.html', body_id='login-page', title='Sign In')
        flash('This email account already exist. Please use different email addres or recover your password','register-exist')
            
    """ Return register template """
    return render_template('pages/register.html', body_id='register-page', title='Register account')

# Password Recovery Page
@app.route('/recovery',  methods=["GET", "POST"])
def recovery():
    """
    This function is sendind recovery message when submit
    """
    if request.method == "POST":
        users = mongo.db.Users
        
        """ Request information from user form """
        req = request.form
        
        """ Get variable from user form"""
        email = req.get('recovery_email').lower()
        """ Prevent to sending request when field is empty"""
        
        """ Check if users exist in databas """
        current_user = users.find_one({'email': email})
        
        """ If users exist do next steps, else show error message """
        if current_user is not None:
            """ If user is found, collect all information from database"""
            current_user_name = current_user['name']
            current_user_email = current_user['email']
            
            """ Run email application """
            def send_email(app, msg):
                with app.app_context():
                    mail.send(msg)
            msg = Message()
            msg.subject = 'Password Recovery'
            msg.recipients = [current_user_email]
            msg.sender = os.getenv('EMAIL_USERNAME')
            msg.html = render_template('components/emails/recovery-email.html', user = current_user_name)
            Thread(target=send_email, args=(app, msg)).start()
            
            flash('Please find a password recovery message in your inbox or spam folder','recovery-positive')
            return render_template('pages/recovery.html', body_id='login-page', title='Sign In')
        flash("This email account doesn't exist is our database. Check email address and try once again.","recovery-negative")
    
    """ Return recovery template """
    return render_template('pages/recovery.html', body_id='recovery-page', title='Password recovery')


# Remove Account
@app.route('/account-removed')
def remove_account():
    """
    Renders remove account page
    Remove account from database and show message
    """
    users = mongo.db.Users
    newsletter = mongo.db.Newsletter
    
    users_email = users.find_one({'email': session['email']})
    users_newsletter = newsletter.find_one({'email': session['email']})
    
    """ Remove user from Users db """
    users_result = users.find(users_email)
    for doc in users_result:
        user_id = doc["_id"]
    mongo.db.Users.remove({'_id': user_id})
    
    """ Remove user from Newsletter db """
    newsletter_result = newsletter.find(users_newsletter)
    for doc in newsletter_result:
        newsletter_user_id = doc["_id"]
    mongo.db.Newsletter.remove({'_id': newsletter_user_id})
    
    """ Clear session and redirect to main page"""
    """ Show flash message on main page after redirecting """
    session.clear()
    
    flash('Your account has been removed successfully!','account-removed')
    return render_template('pages/landing-page.html', body_id='home-page', title = "Home Page",account_removed="account-removed")

# Logout user
@app.route('/logout')
def logout():
    """
    This route is clearing user session variables
    Redirecting user to landing page (home page)
    """
    session.clear()
    return redirect(url_for('home'))

# About Page
@app.route('/about')
def about():
    """
    Renders about page
    """
    return  render_template('pages/about.html', body_id='about-page')
    
# Newsletter subscription
@app.route('/newsletter', methods=["GET", "POST"])
def add_to_newsletter(login_newsletter):
    """ 
    This function will collect email addres from inout box
    Information will be stored in newsletter database
    """
    if request.method == "POST":
        users = mongo.db.Users
        newsletter = mongo.db.Newsletter
        
        """ Check if register form string is not empty """
        if login_newsletter !='':
            
            exist_in_newsletter = newsletter.find_one({'email': login_newsletter})
            if exist_in_newsletter is None:
            
                newsletter.insert_one({
                'email' : login_newsletter,
                'newsletter' : 'Y'
                })
            
        else:
        
            """ Request information from user form """
            req = request.form
            
            """ Get email as variable from user form"""
            newsletter_email = req.get('newsletter-email').lower()
            
            """ Search for email address in User database """
            existing_user = users.find_one({'email' : newsletter_email})
        
            """ If user exisit show flash message with error """
            if existing_user is not None:
                flash('You are subscribing newsletter already', 'newsletter-error')
            else:
                """ Check if email address already exist in newsletter database """
                exist_in_newsletter = newsletter.find_one({'email': newsletter_email})
                if exist_in_newsletter is None:
            
                    newsletter.insert_one({
                        'email' : newsletter_email,
                        'newsletter' : 'Y'
                    })
                    
                    flash('Welcome in our newsletter group!','newsletter-success')
                else:    
                    flash('You are subscribing newsletter already','newsletter-error')
                    
            """ NOT WORKING ....."""
            return redirect(request.referrer)
        
# Page not found error route
@app.errorhandler(404)
def Error404(error):
    """
    This route renders an error 404
    """
    error_type = str(error)
    return render_template('pages/error-page.html', error_type=error_type, body_id='error-page'), 404 

# Server error route
@app.errorhandler(500)
def Error500(error):
    """
    This route renders server error 500
    """
    error_type = str(error)
    return render_template('pages/error-page.html', error_type=error_type, body_id='error-page'), 500

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=os.getenv('MY_DEBUG'))