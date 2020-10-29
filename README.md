<img src="https://www.abovewave.kylos.pl/bakingMaster/Logotype.png" style="margin-right:20px; margin-bottom:-15px; width:150px"/>

# Baking Master

Hi! If you're reading this, it means you love to bake.
This web application will let you develope your baking skills! Search through all amazing recipes, share your own recipes, change them at any time you want!
If you decide not to share them, simply removed them. You can save your favourite recipes and come back to them whenever you want! <br>Don't waist your time! It's bake time!

## Contents
- [User Experience](#user-experience)
  * [About Project](#about-project)
  * [Users Goals](#users-goals)
  * [Author Goals](#author-goals)
  * [User Stories](#user-stories)
  * [User Requirements & Expectations](#user-requirements---expectations)
    + [Requirements](#requirements)
    + [Expectations](#expectations)
- [Design](#design)
  * [Fonts](#fonts)
  * [Icons](#icons)
  * [Colors](#colors)
- [Wireframes](#wireframes)
- [Database](#database)
- [Features](#features)
  * [Features that have been developed](#features-that-have-been-developed)
  * [Features that will be developed in the future](#features-that-will-be-developed-in-the-future)
- [Technologies Used](#technologies-used)
    + [Languages](#languages)
    + [Tools & Libraries](#tools---libraries)
- [Planning & Testing](#planning---testing)
    + [Planning](#planning)
    + [Testing](#testing)
    + [Feature Testing](#feature-testing)
    + [Bugs During Development](#bugs-during-development)
- [Deployment](#deployment)
  * [Cloning BakingMaster from GitHub](#cloning-bakingmaster-from-github)
  * [Deploying BakingMaster to Heroku](#deploying-bakingmaster-to-heroku)
- [Credits / Acknowledgement](#credits---acknowledgement)
- [Contact](#contact)
- [Disclaimer](#disclaimer)

## User Experience

### About Project
This project was created to help people develope their baking skills. This web application is giving access to thousandes of different recipes. Users are able to create own recipes, add pictures of their bueatiful work, add their loved recipes to favourites list. Their also can remove and amend previously added recipes, if they decied not share them anymore.

### Users Goals
- To be able to search through different recipes.
- To create own recipes, add pictures of their work and share recipes with other users.
- To be able to register in a safe way.
- To have a possibility to restore forgotten password.
- Clean and simple design, with good mobile look and easy to use.
- A contact form to get more information about cooperation and sharing recipes.
- To be able to use web application on Desktops, Tablets and Mobile devices (especcialy on Apple products)

### Author Goals
- Engage users to develope their baking skills and to change their attitude to learn more.
- Collect user information in terms of site analytics and Edamam API request.
- Recieve messages from the users/customers about cooperation to expand baking courses etc.

### User Stories

Mark says: “I would like to know the website where I can find some great recipes, from very huge range of recipes. Recipes to bake some cakes and other sweets, the most…, but also normal recipes like salads, etc - for my girlfriend .”

Chloe says: “I haven’t found nice looking website, more looking like, you know 'pink and fluffy’ they saying. I love pink and red colour, also design should be realy simple and intuitive as I’ve seen lots of this not user frirendly websites.”

Abel says: “I’m a beginner in baking. I would like to find some nice and easy recipes and store them in my Favourite list so I can review them when I’ll finished baking and compare to some pictures to make sure it is looking like it should”

Debbie say: "It's good to have all in one place. Baking recipes and some equipment for the advance chefs like me."

### User Requirements & Expectations

#### Requirements
- Visually appealing website
- Easy user interface, navigation and quick website response on user actions
- Necessery information about recipes, ingridients and level of difficulty
- Nice and clear layout of all information
- Create own recipes or save liked ones to favourite list

#### Expectations
- Application loads in good speed without problems on slow internet connections
- User information store safely
- Users can easily interact with website buttons and elements 
- Website content  renders correctly on desktop, tablet and mobile devices
- Users have sufficient number of information about equipement and recipes

## Design
I've decied to use colours of high contrast. This should let the users, to see all the information clearly, on small devices. Especially with small ammount of screen brightnes, also it should help with outdoor/indoor light screen brightnes auto adjustments. I love minimalism that's why design of this application is so nice and clean. I tried not to overload pages with content to do not 'scare' the user with lots of informaiton.

### Fonts
I chose to use only one font from google fonts <a href="https://fonts.google.com/specimen/Roboto">Roboto</a>, as it makes my project more simplify and I think this font style is very good for ease of reading recipes descriptions. I've used a variety of font weight, colours to focus users attention on importnat information.

### Icons
All icons used in this project are coming from <a href="https://fontawesome.com">Font-Awesome</a> and their role is to improve visiblity and improve user expirience.

### Colors
The colours used in this project where wisely choosen to prevent unreadable recipes descriptions and to provide the best user expirience.
I've used opacity style option to create hover effects.
<img src="https://www.abovewave.kylos.pl/bakingMaster/Coloristic.png">

## Wireframes
I Built the wireframes for this project using <a href="https://www.invisionapp.com">InvisionApp</a>, this application is totally free of charge. I could easily create all wireframes for all platforms, sketch all the features that my website contains. Different colorisitc available, huge number of free templates to start with or simply you can create a blank wireframe. Very easy to use! Strongly recommend

View the <a href="https://github.com/KarolSliwka/Baking_Master/tree/master/wireframes">wireframes</a> for this project
 
## Database
I have used Cloud-hosted MongoDB service on AWS, because it's easy to control, it has good access to database. All database instances are deployed in a unique Virtual Private Cloud (VPC) to ensure network isolation. 
I've created MongoDB Cluster and lots of different collections in my database to suits my needs with this project.

Find more on <a href="https://www.mongodb.com/cloud/atlas/register">MongoDB</a>

## Features

### Features that have been developed
- Main page banner/carousel with beautifull cakes photo/s
- Register/create new account , Login to existing account, reset password functionality
- Contact form available for all user ( registered and unregistered )
- Add recipes to favourites list feature, allowing users to add any recipe to their own, private, 'favourites' list/page
- Users can create their own recipes, remove or amend anytime
- Sign in to Newsletter functionality, to keep up to date with the latest from BakingMaster

### Features that will be developed in the future
- Recipes comments functionality
- Social media share buttons ( facebook, instagram, tweeter, pinterest )
- Ingirdients easy print/one-click functionality to print ingridients shopping list
- Extend equipement option from link to equipement database from cooperating providers

## Technologies Used
#### Languages
* <a href="https://developer.mozilla.org/en-US/docs/Web/HTML">HTML</a>
* <a href="https://developer.mozilla.org/en-US/docs/Web/CSS">CSS</a>
* <a href="https://www.w3schools.com/js/">JavaScript</a>
* <a href="https://www.json.org/json-en.html">JSON</a>
* <a href="https://www.python.org/">Python</a>

#### Tools & Libraries

* <a href="https://jquery.com/">jQuery</a>
* <a href="https://git-scm.com/">Git</a>
* <a href="https://getbootstrap.com/">Bootstrap</a>
* <a href="https://fontawesome.com/icons?d=gallery">Font-Awesome</a>
* <a href="https://sass-lang.com/">SASS/SCSS</a>
* <a href="https://www.mongodb.com/cloud/atlas">MongoDB Atlas</a>
* <a href="https://pymongo.readthedocs.io/en/stable/">PyMongo</a>
* <a href="https://flask.palletsprojects.com/en/1.0.x/">Flask</a>
* <a href="https://jinja.palletsprojects.com/en/2.10.x/">Jinja</a>

## Planning & Testing

#### Planning
Project was well planned with a significant amount of a time. I moustly focused on design, UX/UI, page loading speed

#### Testing
Whole application was tested durign the designing and deploying period. Each feature was tested step by step to avoid user frustriation made by not working website elements. Whole web app responsivity was tested using build in tool in Safari Browser.

#### Feature Testing
 * Login & Register Form - Both form has been tested by entering values into entry fields and running script which should add details to database. Result : Worked as expected!
 * Contact form - All different variances with missing fields were tested while trying to send an email. Result : Sending failed
 * Subscribe Newsletter - Validation works with empty field. By clicking 'Subscribe' button, email address is saved in newsletter database. Result : Success!

#### Bugs During Development 
 * Contact form - After clicking send script should send an email from user form but it didn't work... The issue I faced was, google mailbox client has restrictions which will not allow outside app to send an email.</br>
       Solution - Google mail restrictions settings change</br>
         Result - Email sent, work as expected
 * Contact form - Message input box, while extending box, whole input field was overfloating contact form</br>
       Solution - Width setted as max width - calculated based on contact form size</br>
         Result - Message input field is not overflating whole contact form
 * Heroku pages error codes : H14 and H10</br>
       Solution - Requirements.txt file, Procfile recreated with small changes, old Python package removed</br>
         Result - Application successfully deployed to heroku pages
 * Flash message - All flash messages runned and show by running any of flash message code line from python.py file</br>
       Solution - Flash message change to messages by categories, 'hiddem' class applied to website elements</br>
         Result - Single flash message show while running single line of code

<p>During working on this project I faced lots of different issues. Some of them were created because of lack of knowledge and wrong code semantic...</p>

## Deployment
BakingMaster app was created in AWS Cloud9 IDE by using source code management functionality of Git, hosted on GitHub and deployed on Heroku Pages.

### Setting up an AWS Cloud9
1.If you haven't got a Cloud9 account on AWS you create it <a href="https://aws.amazon.com/cloud9/">here</a>.
Click on Get Started with AWS Cloud 9 and follow all the instruction untill account is created.

2.Click on the Create Environment button.

3.Create a individual Name for the Environment and write a app description and click - Next Step.

4.Leave the Configuration Settings as default values and click - Next Step.

5.On the Review page simply click Create Environment button. It will take a couple of minutes to create your environment.

### Cloning BakingMaster from GitHub to AWS Cloud9

<strong>Ensure</strong> you have the following installed:
* PIP 
* Python 3 
* Flask 
* PyMongo
* GIT

1: You can clone BakingMaster repository by downloading it from <a href="https://github.com/KarolSliwka/Baking_Master">GitHub/BakingMaster</a> or if you have Git installed, by typing the following command into your terminal.

<img src="https://www.abovewave.kylos.pl/bakingMaster/gtihub_info.png"/>
2. Type or paste into your bash command 
```bash
git clone https://github.com/KarolSliwka/Baking_Master.git
```

<strong>WARNING! You may need to follow a different guide when working in other IDE than AWS Cloud9.
<em>Read more here <a href="https://python.readthedocs.io/en/latest/library/venv.html">Creating Python Environment</a></em></strong>

<strong>You need to have an account at <a href="https://www.mongodb.com/">MongoDB</a> to create the database.</strong>

3: <strong>Install</strong> the relevant requirements & dependancies from the requirements.txt file.
```bash
sudo pip3 install -r requirements.txt
```
4: In your IDE you need to add some variables that can be get through environment. You can add them into <strong>.bashrc</strong> file using commands below to edit file. Make sure you are in you are not in your environemt folder.
```bash
cd ..
nano .bashrc
```
<strong>Make sure names of these variables match names from app.py file.</strong>

    IP, PORT, MONGO URI, SECRET KEY, EMAILUSERNAME, EMAIL PASSWORD, MAIL SERVER, MAIL PORT

5:  In order to run the Flask app we need to be inside the app folder.
 * Click Run Application or type in terminal ```python app.py```
 * Click Preview Running Application to see the app.
 
<img src="https://www.abovewave.kylos.pl/bakingMaster/ide_run.png"/>
```bash
flask run 
```
or 
```bash
Python3 app.py
```

### Deploying BakingMaster to Heroku

* 1: Create a <strong>requirements.txt</strong> file using command below.
```bash
pip3 freeze --local > "requirements.txt"
```
* 2: Create a <strong>Procfile</strong> file using command below.
```bash
echo web: python3 app.py > Procfile
```
* 3: Push all files to your git repository.
``` git push origin master ``` - your master branch
* 4: Create a new application for this project on the Heroku Pages. Click on 'New App' button and follow steps to create new app.
* 5: Select your deployment method by clicking on the <strong>deployment</strong> method button.
* 7: You can either follow Heroku Git deployment method or GitHub connect (I did it  this time - project is deployed automatically when master branch is pushed to repository)
* 6: Set the following config variables:

**Key**|**Value**
:-----:|:-----:
IP|0.0.0.0
PORT|5000
MDB\_NAME | "YOUR-DB-NAME"
MONGO\_URI|"mongodb+srv://'username':'password'.egcn1.mongodb.net/'clusterName'?""
SECRET\_KEY|"SECRET-KEY"
EMAIL\_USERNAME|"YOUR-EMAIL-USERNAME"
EMAIL\_PASSWORD|"YOUR-EMAIL-PASSWORD"
MAIL\_SERVER|"MAIL-PROTOCOL.DOMAIN.EXTENSION"
MAIL\_PORT|"YOUR-PORT-NUMBER"

* 7: Click the deploy button on the Heroku Pages dashboard.
* 8: The site has been deployed the Heroku Pages, Enjoy!;

## Credits / Acknowledgement

Simple and clear design came from heart of the author. Project coloristic was wisely chosen by the author.<br>
*   <a href="https://realfavicongenerator.net/favicon_checker#.X0WHei2ZMUG">Favicon Generator/Checker</a>
*   <a href="https://fonts.google.com/specimen/Roboto">Roboto</a>
*   <a href="https://fontawesome.com">Font-Awesome</a>
*   <a href="https://www.invisionapp.com">InvisionApp</a>
*   <a href="https://blog.sfceurope.com/famous-pastry-chefs-from-around-the-world">Landing page chef's information and images</a>
*   <a href="https://unsplash.com">Carousel photos</a>
*   <a href="https://www.bbcgoodfood.com">BBCGoodFood.com</a> - Few recipes including images were used to create basic recipe database.

## Contact
If you've got any questions please contact me via email: <a href="mailto:contact@karolsliwka.com">contact@karolsliwka.com</a>

## Disclaimer
The contents of this web application are for educational purposes only.