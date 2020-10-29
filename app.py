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

class ReverseProxied(object):
    """ Create HTTPS connection for all rdirected urls """
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
    
users_collection = mongo.db.Users
recipes_collection = mongo.db.Recipes
    
# Home page
@app.route('/')
def home():
    """
    Renders landing page/home page
    """
    return render_template('pages/landing-page.html', 
    body_id='home-page', page_title = "Home Page")

# All Recieps page
@app.route('/recipes', methods=["GET", "POST"])
def recipes():
    """
    Renders recipes search page and return search result
    """
    if request.method == "POST": 
        
        req = request.form
        search_text = req.get('search')

        regex_query = { 'title' : {"$regex" : search_text.lower()} }
        search_request = recipes_collection.find(regex_query)

        search_count = search_request.count()
        
        return  render_template('pages/recipes.html', 
        body_id='recipes-page', page_title='Recieps',search_text=search_text,search_result="TRUE",
        search_request=search_request,search_count=search_count)
    
    recipe_range = recipes_collection.count()
    if recipe_range <= 9:
        recipe_range = recipe_range
    else: 
        recipe_range = 10
    random_10 =  recipes_collection.aggregate([{'$sample': {'size': 10 }}])
    
    if session.get('email') is None:
        my_favourites = []
    else:
        current_user = users_collection.find_one({'email':session.get('email')})
        my_favourites = current_user['favourites']
    
    return  render_template('pages/recipes.html', 
    body_id='recipes-page', page_title='Recipes',recipe_range=recipe_range,
    random_10=random_10,search_result="FALSE", my_favourites=my_favourites)

@app.route('/recipe/<recipe_id>', methods=['GET','POST'])
def recipe_page(recipe_id):
    """
    Render recipe page
    """
    this_recipe = recipes_collection.find_one({'_id':ObjectId(recipe_id)})
    recipe_author = users_collection.find_one({'email':this_recipe['author']})
    
    author_name = recipe_author['name']
    ingredients = this_recipe['ingredients']
    ingredients_scale = this_recipe['ingredients-scale']
    preparation = this_recipe['preparation']
    tips = this_recipe['tips']

    current_user = users_collection.find_one({'email': session.get('email')})

    if session.get('email') is None:
        my_fav = []
        session['url'] = request.referrer
    else:
        my_fav = current_user['favourites']
    
    return render_template('pages/recipe.html',body_id='recipe-page', page_title=this_recipe['title'],
    this_recipe=this_recipe, author_name=author_name,ingredients=ingredients,ingredients_scale=ingredients_scale,
    preparation=preparation,tips=tips,my_fav=my_fav,recipe_author=recipe_author)   

# Add Recipe
@app.route('/add/recipe', methods=['GET','POST'])
def add_recipe():
    """
    Render Add Recipe page, load first step number and allocate it to steps-count
    """
    if request.method == "POST":
        req = request.form
        
        recipe_title = req.get('recipe-title')
        recipe_prepare_time = req.get('preparing-time-hrs') + ":" + req.get('preparing-time-min')
        recpie_difficulty = req.get('difficulty-level')
        
        ingredients_array = []
        ingredients_scale_array = []
        preparation_array = []  
        tips_array = []
        
        for key in request.form:
            if key.startswith('ingredient-name-'):
                value = request.form[key]
                ingredients_array.append(value)
                    
            if key.startswith('ingredient-scale-'):
                value = request.form[key]
                ingredients_scale_array.append(value)
                
            if key.startswith('preparation-step-'):
                value = request.form[key]
                preparation_array.append(value)
                
            if key.startswith('tip-step-'):
                value = request.form[key]
                tips_array.append(value)
                    
        recipe_author = session['email']
        
        if 'preparing_image' in request.files:
            preparing_image = request.files['preparing_image']
            mongo.save_file(preparing_image.filename, preparing_image)
            insert_recipe = recipes_collection.insert_one({
                'recipe_image': preparing_image.filename,
                'title': recipe_title.lower(),
                'time': recipe_prepare_time,
                'difficulty': recpie_difficulty,
                'ingredients': ingredients_array,
                'ingredients-scale' :ingredients_scale_array,
                'preparation': preparation_array,
                'tips': tips_array,
                'author': recipe_author,
            })
            
            users_collection.find_one_and_update({'email': recipe_author},{'$push': {'recipes_id': insert_recipe.inserted_id}})

        flash('Your recipe was added successfully, enjoy baking!','recipe-added')
    return render_template('pages/add-recipe.html',
    body_id='new-recipe-page', page_title='Add Recipe')

# Edit Recipe
@app.route('/edit/recipe/<recipe_id>',methods=['GET','POST'])
def edit_recipe(recipe_id):
    """
    Render edit recipe page, update edited recipe record
    """
    recipe_doc = recipes_collection.find_one({'_id':ObjectId(recipe_id)})
    
    if request.method == "POST":
        req = request.form
        
        recipe_image = recipe_doc['recipe_image']
        recipe_title = req.get('recipe-title')
        recipe_prepare_time = req.get('preparing-time-hrs') + ":" + req.get('preparing-time-min')
        recpie_difficulty = req.get('difficulty-level')
        recipe_author = recipe_doc['author']
        
        ingredients_array = []
        ingredients_scale_array = []
        preparation_array = []  
        tips_array = []
        preparing_image = []
        
        for key in request.form:
            if key !="":
                if key.startswith('ingredient-name-'):
                    value = request.form[key]
                    ingredients_array.append(value)
                
                if key.startswith('ingredient-scale-'):
                    value = request.form[key]
                    ingredients_scale_array.append(value)
            
                if key.startswith('preparation-step-'):
                    value = request.form[key]
                    preparation_array.append(value)

                if key.startswith('tip-step-'):
                    value = request.form[key]
                    tips_array.append(value)
                    
        preparing_image = request.files['preparing_image']
        if not preparing_image:
            preparing_image.filename = recipe_image
            
        else:
            fs_files_search = mongo.db.fs.files.find_one({'filename':recipe_image})
            fsfiles_result = mongo.db.fs.files.find(fs_files_search)
            for doc in fsfiles_result:
                fsFiles_id = doc['_id']
            
            mongo.db.fs.files.remove({'_id':fsFiles_id})
            mongo.db.fs.chunks.remove({'files_id':fsFiles_id})
        
            preparing_image = request.files['preparing_image']
            mongo.save_file(preparing_image.filename, preparing_image)

        recipes_collection.find_one_and_replace({'_id':ObjectId(recipe_doc['_id'])},{
            'recipe_image': preparing_image.filename,
            'title': recipe_title.lower(),
            'time': recipe_prepare_time,
            'difficulty': recpie_difficulty,
            'ingredients': ingredients_array,
            'ingredients-scale' :ingredients_scale_array,
            'preparation': preparation_array,
            'tips': tips_array,
            'author': recipe_author
        })

        flash('Your recipe has been edited successfully, looks good!','recipe_edited')
        return redirect(url_for('recipe_page',recipe_id = recipe_doc['_id'],recipe_edited="Edited Successfully"))
            
    return render_template('pages/edit-recipe.html',recipe_doc=recipe_doc,
    body_id='edit-recipe-page', page_title='Edit Recipe')

# Remove Recipe
@app.route('/delete/recipe/<recipe_id>', methods=['GET','POST'])
def remove_recipe(recipe_id):
    """
    Render your recipes page and remove recipe record from database
    """
    user_session = session['email']
    users_collection.find_one_and_update({'email':user_session},{'$pull':{'recipes_id': ObjectId(recipe_id)}})
    
    recipe_search = recipes_collection.find_one({'_id':ObjectId(recipe_id)})
    result = recipes_collection.find(recipe_search)
    for doc in result:
        image_name = doc['recipe_image']

    fs_files_search = mongo.db.fs.files.find_one({'filename':image_name})
    fsfiles_result = mongo.db.fs.files.find(fs_files_search)
    for doc in fsfiles_result:
        fsFiles_id = doc['_id']
        
    mongo.db.fs.files.remove({'_id':fsFiles_id})
    mongo.db.fs.chunks.remove({'files_id':fsFiles_id})
    
    recipes_collection.remove({'_id': ObjectId(recipe_id)})
    
    return your_recipes()

# Add to Favourites
@app.route('/favourites/add/<recipe_id>', methods=['GET','POST'])
def add_to_favourites(recipe_id):
    """
    Add to favourite list and render refferer page
    """
    if session.get('email') is None:
        """ redirect user to login page """
        session['url'] = url_for('recipes')
        return redirect(url_for('login'))
    else:
        users_collection.find_one_and_update({'email':session.get('email')},
        {'$push':{'favourites': ObjectId(recipe_id)}})
        return redirect(request.referrer)
    
# Remove from Favourites
@app.route('/favourites/remove/<recipe_id>', methods=['GET','POST'])
def remove_from_favourites(recipe_id):
    """
    Remove from favourite list and reneder reffer page
    """
    users_collection.find_one_and_update({'email':session.get('email')},
    {'$pull':{'favourites': ObjectId(recipe_id)}})
    return redirect(request.referrer)
    
# User menu page
@app.route('/user/menu')
def user_menu():
    """
    Render user menu page
    """
    return render_template("pages/index.html", body_id="user-menu", page_title='User Menu')

# Retrive image form MongoDB
@app.route('/file/<filename>')
def file(filename):
    """
    Return recipe image from database
    """
    return mongo.send_file(filename)

# Your Recipes 
@app.route('/user/recipes', methods=['GET','POST'])
def your_recipes():
    """
    Render user recipes pages, present all user recipes as cards
    """
    current_user = session['email']
    current_user_users = users_collection.find_one({'email':current_user})
    your_recipes_count = len(current_user_users['recipes_id'])

    recipes_user = current_user_users['recipes_id']
    all_recipes = recipes_collection.find({'author':current_user})
    
    return render_template('pages/your-recipes.html',body_id='your-recipes-page', 
    page_title='Your Recipes',your_recipes_count=your_recipes_count,
    recipes_user=recipes_user,all_recipes=all_recipes)   
    
# Favourites Page
@app.route('/favourites')
def favourites():
    """
    Renders favourite page only when user is logged in
    """
    if session.get('email') is None:
        session['url'] = url_for('favourites')
        return render_template('pages/favourites.html', 
        body_id='favourites-page', page_title='Favourites',no_user='true')
    else:
        current_user = users_collection.find_one({'email': session.get('email')})
            
        my_favourites =[]
        my_fav = current_user['favourites']
        for _id in my_fav:
            fav_id = recipes_collection.find_one({'_id': ObjectId(_id)})
            my_favourites.append(fav_id)
            
        favourites_count = len(current_user['favourites'])
    
        return render_template('pages/favourites.html', 
        body_id='favourites-page', page_title='Favourites',no_user='false',
        favourites_count=favourites_count,my_favourites=my_favourites)

# Register Page 
@app.route('/register', methods=["GET", "POST"])
def register():
    """
    This function is rendering user registration template.
    When form is validated correctly, new user is added into database.
    """
    if request.method == "POST":
        req = request.form
        
        name = req.get('name')
        email = req.get('email')
        password = req.get('password')
        hashpassword = bcrypt.hashpw(
                    password.encode('utf-8'), bcrypt.gensalt())
        empty_recipes_id = []
        empty_favourites = []
        
        current_user = users_collection.find_one({'email': email})
        if current_user is None:
            
            users_collection.insert_one({
                'name' : name,
                'email' : email.lower(),
                'password' : hashpassword,
                'newsletter' : 'Y',
                'recipes_id': empty_recipes_id,
                'favourites' : empty_favourites
            })
            
            login_newsletter = email
            add_to_newsletter(login_newsletter)
        
            flash('Your account was created successfully! Enjoy browsing our amazing recipes','register-added')
            return render_template('pages/login.html', body_id='login-page', page_title='Sign In')
        flash('This email account already exist. Please use different email addres or recover your password','register-exist')

    return render_template('pages/register.html', body_id='register-page', page_title='Register account')
 
# Login Page   
@app.route('/login', methods=["GET", "POST"])
def login():
    """
    This funciton will check if user exists in database.
    When exist, will go to account page. When failed, show flash message.
    """
    if request.method == "POST":
        req = request.form
        
        email_login = req.get('email')
        password = req.get('password')

        login_user = users_collection.find_one({'email': email_login.lower()})
        result = users_collection.find(login_user)
        for doc in result:
            username = doc["name"]
            
        if login_user:
            if bcrypt.hashpw(password.encode('utf-8'), login_user['password']) == login_user['password']:
                session['email'] = email_login
                session['name'] = username
                flash('You have been successfully logged in!')
                
                if session.get('email') is not None:
                    if 'url' in session:
                        return redirect(session['url'])
                    return redirect(url_for('user_menu'))
                else:
                    
                    flash("Incorrect username or password / user doesn't exist.","incorrect-user")
                    return redirect(url_for('login'))
                    
        flash("Incorrect username or password / user doesn't exist.","incorrect-user")
    return render_template('pages/login.html', body_id='login-page', page_title='Sign In')

# User account page
@app.route('/user/account', methods=['GET','POST'])
def account():
    
    try:
        user_info = users_collection.find_one({'email': session['email']})
        user_info_collection = users_collection.find(user_info)

        for doc in user_info_collection:
            active_user = doc['name']
            email = doc['email']
            recipes_count = len(doc['recipes_id'])
            fav_recipe_count = len(doc['favourites'])

        return render_template("pages/account.html", body_id="user-account", 
        page_title="User Account",active_user=active_user,email=email,
        recipes_count=recipes_count,fav_recipe_count=fav_recipe_count)

    except:
        """
        Return user account page without user name
        """
        return render_template("pages/account.html", body_id="user-account", 
        page_title="User Account")  
    
# Password Recovery Page
@app.route('/recovery',  methods=["GET", "POST"])
def recovery():
    """
    This function is sendind recovery message when submit
    """
    if request.method == "POST":
        req = request.form

        email = req.get('recovery_email').lower()
        current_user = users_collection.find_one({'email': email})
        
        if current_user is not None:
            current_user_name = current_user['name']
            current_user_email = current_user['email']
            
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
            return render_template('pages/recovery.html', body_id='login-page', page_title='Sign In')
        flash("This email account doesn't exist is our database. Check email address and try once again.","recovery-negative")
    
    return render_template('pages/recovery.html', body_id='recovery-page', page_title='Password recovery')

# Remove Account
@app.route('/remove/account')
def remove_account():
    """
    Renders remove account page
    Remove account from database and show message
    """
    newsletter = mongo.db.Newsletter
    
    users_email = users_collection.find_one({'email': session['email']})
    users_newsletter = newsletter.find_one({'email': session['email']})
    
    users_result = users_collection.find(users_email)
    for doc in users_result:
        user_id = doc["_id"]
    mongo.db.Users.remove({'_id': user_id})
    
    newsletter_result = newsletter.find(users_newsletter)
    for doc in newsletter_result:
        newsletter_user_id = doc["_id"]
    mongo.db.Newsletter.remove({'_id': newsletter_user_id})
    session.clear()
    
    flash('Your account has been removed successfully!','account-removed')
    return render_template('pages/landing-page.html', body_id='home-page', 
    page_title='Home Page',account_removed="account-removed")

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
        
# Contact Page
@app.route('/contact', methods=["GET", "POST"])
def contact():
    """
    This function is sending email from userform in contact page
    """
    if request.method == "POST":
        req = request.form
        
        username = req.get('contact-name')
        email_address = req.get('contact-email').lower()
        contact_message = req.get('contact-message')
        email_from = os.getenv('EMAIL_USERNAME')

        def send_email(app, msg):
            with app.app_context():
                mail.send(msg)
        msg = Message()
        msg.subject = 'Message from contact form'
        msg.recipients = [email_from, email_address]
        msg.sender = email_from
        msg.html = render_template('components/emails/contact-email.html', 
        username = username, contact_message = contact_message)
        Thread(target=send_email, args=(app, msg)).start()
        
        flash('Your message was sent successfully','contact-send')
    return render_template('pages/contact.html', body_id='contact-page', page_title="Contact Page") 
    
# Newsletter subscription
@app.route('/newsletter', methods=["GET", "POST"])
def add_to_newsletter(login_newsletter):
    """ 
    This function will collect email addres from inout box
    Information will be stored in newsletter database
    """
    if request.method == "POST":
        newsletter = mongo.db.Newsletter
        
        if login_newsletter !='':
            exist_in_newsletter = newsletter.find_one({'email': login_newsletter})
            if exist_in_newsletter is None:
                newsletter.insert_one({
                'email' : login_newsletter,
                'newsletter' : 'Y'
                })
            
        else:
        
            req = request.form
            newsletter_email = req.get('newsletter-email').lower()
            
            existing_user = users_collection.find_one({'email' : newsletter_email})

            if existing_user is not None:
                flash('You are subscribing newsletter already', 'newsletter-error')
            else:
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
    return render_template('pages/error-page.html', error_type=error_type, 
    body_id='error-page404',page_title='Error 404'), 404 

# Server error route
@app.errorhandler(500)
def Error500(error):
    """
    This route renders server error 500
    """
    error_type = str(error)
    return render_template('pages/error-page.html', error_type=error_type,
    body_id='error-page500', page_title='Error 500'), 500

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=os.getenv('DEBUG'))