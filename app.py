import os
import pymongo
import requests
import bcrypt
from flask import Flask, render_template, request, flash, session, redirect, url_for
from flask_mail import Mail
from flask_mail import Message
from threading import Thread
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

# Initilize connection
app.config["MONGO_DBNAME"] = 'BakingMaster'
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

# Home page
@app.route('/')
@app.route('/home')
def home():
    
    
    #url = "https://api.edamam.com/search?q=apple&app_id=3fbc3ca8&app_key="+ API_KEY
    #response = requests.request("GET", url)

    #print(response.text)
    
    return render_template('layout/base.html', body_id='home-page', title = "Home Page")

# All Recieps page
@app.route('/recipes')
def recipes():
    return  render_template('pages/recipes.html', body_id='recipes-page')
    
# Favourites Page
@app.route('/top-hundred')
def top_hundredd():
    return render_template('pages/favourites.html', body_id='favourites-page')
    
# Search Page
@app.route('/search-results')
def search_results():
    return render_template('pages/search-results.html', body_id='search-page')

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
        email_address = req.get('contact-email')
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
@app.route('/login')
def login():
    """
    This function is comparing information provided in user form with database information
    If result is positive then it's returning user - my account page, if not shows the error info
    """
    
    return render_template('pages/login.html', body_id='login-page')
   
# Register Page 
@app.route('/register', methods=["GET", "POST"])
def register():
    """
    This function is rendering user registration template, when form is validated, new user is added into database.
    """
    if request.method == "POST":
        users = mongo.db.Users
        newsletter = mongo.db.Newsletter
        """ Request information from user form """
        req = request.form
        
        """ Get all necessery variables from user form"""
        name = req.get('name')
        email = req.get('email')
        password = req.get('password')
        hashpassword = bcrypt.hashpw(
                    password.encode('utf-8'), bcrypt.gensalt())
        
        """ Check if users exist in databas """
        current_user = users.find_one({'email': email})
        if current_user is None:
            
            """ Insert new user, new record to database """
            users.insert_one({
                'name' : name,
                'email' : email,
                'password' : hashpassword,
                'newsletter' : 'Y'
                
            })
            
            """ New user newsletter subscription added to newsletters database """
            newsletter.insert_one({
                'email' : email,
                'newsletter' : 'Y'
            })
            
            flash('Your account was created successfully! Enjoy browsing our amazing recipes','register-added')
            return render_template('pages/login.html', body_id='login-page', title='Sign In')
        flash('This email account already exist in our records. Please use different email addres or recover your password','register-exist')
            
    """ Return register template """
    return render_template('pages/register.html', body_id='register-page', title='Register account')

# Password Recovery Page
@app.route('/recovery',  methods=["GET", "POST"])
def recovery():
    """
    This function is checking information from database and sending recovered password to email provided in userform
    """
    if request.method == "POST":
        users = mongo.db.Users
        
        """ Request information from user form """
        req = request.form
        
        """ Get variable from user form"""
        email = req.get('recovery_email')
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
    
# Newsletter subscription
@app.route('/newsletter', methods=["GET", "POST"])
def add_to_newsletter():
    
    """ This function will get email addres from newsletter form and store newsletter subscription into Newsletter database """
    if request.method == "POST":
        users = mongo.db.Users
        newsletter = mongo.db.Newsletter
        
        """ Request information from user form """
        req = request.form
        
        """ Get email as variable from user form"""
        newsletter_email = req.get('newsletter-email')
        
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
    return redirect(request.referrer)
        

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)