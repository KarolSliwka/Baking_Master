# <img src="https://www.abovewave.kylos.pl/bakingMaster/Logotype.png" style="margin-right:20px; margin-bottom:-15px; width:150px"></img> Baking Master

Hi! If you're reading this, it means you love to bake.
This web application will let you develope your baking skills! Search through all amazing recipes, share your own recipes, change them at any time you want!
If you decide not to share them, simply removed them. You can save your favourite recipes and come back to them whenever you want! <br>Don't waist your time! It's bake time!

## Contents: 
- UX:
    * About Porject
    * User Goals
    * Author Goals
    * User Stories
    * Requirements & Expectations
- Design:
    * Fonts
    * Icons
    * Colors
- Wireframes
- Database Design:
    * Data Storage Types
- Features:
    * Developed
    * Will be developed in the future
- Technologies Used:
    * Languages
    * Tools & Libraries
- Planning and Testing:
    * Planning
    * Testing
    * Feature Testing
- Bugs
- Deployment
- Credits
- Contact
- Disclaimer

## User Experience:

### About Project
This project was created to help people develope their baking skills. This web application is giving ccess to thousandes of different recipes. Users are able to create own recipes, add pictures of their bueatiful work, add their loved recipes to favourites list. Their also can remove and amend previously added recipes, if they decied not share them anymore.

### Users Goals
- To be able to search through different recipes.
- To create own recipes, add pictures of their work and share recipes with other users.
- To be able to register in a safe way.
- To have a possibility to restore forgotten password.
- Clean and simple design, with good mobile look and easy to use.
- A contact form to get more information about cooperation and sharing recipes.
- To be able to use web application on Desktops, Tablets and Mobile devices (especcialy on Apple products)

### Author Goals:
- Engage users to develope their baking skills and to change their attitude to learn more.
- Collect user information in terms of site analytics and Edamam API request.
- Recieve messages from the users/customers about cooperation to expand baking courses etc.

### User Stories:

Mark says: “I would like to know the website where I can find some great recipes, from very huge range of recipes. Recipes to bake some cakes and other sweets, the most…, but also normal recipes like salads, etc - for my girlfriend .”

Chloe says: “I haven’t found nice looking website, more looking like, you know 'pink and fluffy’ they saying. I love pink and red colour, also design should be realy simple and intuitive as I’ve seen lots of this not user frirendly websites.”

Abel says: “I’m a beginner in baking. I would like to find some nice and easy recipes and store them in my Favourite list so I can review them when I’ll finished baking and compare to some pictures to make sure it is looking like it should”

Debbie say: "It's good to have all in one place. Baking recipes and some equipment for the advance chefs like me."

### User Requirements & Expectations:

#### Requirements:
- Visually appealing website
- Easy user interface, navigation and quick website response on user actions
- Necessery information about recipes, ingridients and level of difficulty
- Nice and clear layout of all information
- Create own recipes or save liked ones to favourite list

#### Expectations:
- Application loads in good speed without problems on slow internet connections
- User information store safely
- Users can easily interact with website buttons and elements 
- Website content  renders correctly on desktop, tablet and mobile devices
- Users have sufficient number of information about equipement and recipes

## Design:
I've decied to use colours of high contrast. This should let the users, to see all the information clearly, on small devices. Especially with small ammount of screen brightnes, also it should help with outdoor/indoor light screen brightnes auto adjustments. I love minimalism that's why design of this application is so nice and clean. I tried not to overload pages with content to do not 'scare' the user with lots of informaiton.

### Fonts:
I chose to use only one font from google fonts <a href="https://fonts.google.com/specimen/Roboto">Roboto</a>, as it makes my project more simplify and I think this font style is very good for ease of reading recipes descriptions. I've used a variety of font weight, colours to focus users attention on importnat information.

### Icons:
All icons used in this project are coming from <a href="https://fontawesome.com">Font-Awesome</a> and their role is to improve visiblity and improve user expirience.

### Colors:
The colours used in this project where wisely choosen to prevent unreadable recipes descriptions and to provide the best user expirience.
I've used opacity style option to create hover effects.
<img src="https://www.abovewave.kylos.pl/bakingMaster/Coloristic.png">

## Wireframes:
I Built the wireframes for this project using <a href="https://www.invisionapp.com">InvisionApp</a>, this application is totally free of charge. I could easily create all wireframes for all platforms, sketch all the features that my website contains. Different colorisitc available, huge number of free templates to start with or simply you can create a blank wireframe. Very easy to use! Strongly recommend

View the <a href="https://github.com/KarolSliwka/Baking_Master/tree/master/wireframes">wireframes</a> for this project
 
## Database Design:
MongoDB alowed me to use collections option.

----
To Do

### Data Storage Types:
The types of data that are stored in the MongoDB database.
- ObjectID
- String
- Boolean
- Object
- Array
- Binary

Beers Collection:
**Title**|**Key in Collection**|**Data Type**
:-----:|:-----:|:-----:
Beer Id|_id|ObjectId
Name|name|String
Brewery|brewery|String
Type|type|String
Excerpt|excerpt|String
Notes|notes|String
Abv|abv|String
Image|image|String
Reviews|reviews|Array


End to do 
----

## Features:

### Features that have been developed:
- Main page banner/carousel with beautifull cakes photo/s
- Register/create new account , Login to existing account, reset password functionality
- Contact form available for all user ( registered and unregistered )
- Add recipes to favourites list feature, allowing users to add any recipe to their own, private, 'favourites' list/page
- Users can create their own recipes, remove or amend anytime
- Sign in to Newsletter functionality, to keep up to date with the latest from BakingMaster

### Features that will be developed in the future:
- Recipes comments functionality
- Social media share buttons ( facebook, instagram, tweeter, pinterest )
- Ingirdients easy print/one-click functionality to print ingridients shopping list
- Extend equipement option from link to equipement database from cooperating providers

## Technologies Used:
#### Languages:
* <a href="https://developer.mozilla.org/en-US/docs/Web/HTML">HTML</a>
* <a href="https://developer.mozilla.org/en-US/docs/Web/CSS">CSS</a>
* <a href="https://www.w3schools.com/js/">JavaScript</a>
* <a href="https://www.json.org/json-en.html">JSON</a>
* <a href="https://www.python.org/">Python</a>

#### Tools & Libraries: 

* <a href="https://jquery.com/">jQuery</a>
* <a href="https://git-scm.com/">Git</a>
* <a href="https://getbootstrap.com/">Bootstrap</a>
* <a href="https://fontawesome.com/icons?d=gallery">Font-Awesome</a>
* <a href="https://sass-lang.com/">SASS/SCSS</a>
* <a href="https://www.mongodb.com/cloud/atlas">MongoDB Atlas</a>
* <a href="https://pymongo.readthedocs.io/en/stable/">PyMongo</a>
* <a href="https://flask.palletsprojects.com/en/1.0.x/">Flask</a>
* <a href="https://jinja.palletsprojects.com/en/2.10.x/">Jinja</a>
------  
To Do 

## Planning & Testing:

#### Planning: 
Planning for this project took a significant amount of a time as to not skip over any detail, when using new languages I would argue that planning is THE most important aspect so that you don't miss something down the line.

#### Testing: 
This project naturally will need alot of testing due to the scope of the website, therefore my testing plan and documentation had to be very detailed with high levels of scrutiny. Due to the way the website was built I could perform and deploy tests in an organised fashion, page by page, feature by feature. 

#### Feature Testing : 

<strong>Carousel -</strong>
- <strong>Plan</strong> : I want to include a sliding banner on the project on multiple pages, but also with varying images/size depending on what page the user is currently on. I will need to choose images the represent the theme of the website and that also work well for a sliding banner with content on, I may add a dark overlay on the sliding banner so that content is easier to read.

- <strong>Implementation</strong> : Using slick.js carousel and the documentation provided (see credits) implementing this feature was simple, also having used this tool alot i'm familiar with the structure. Using conditional statements thanks to Flask and Jinja frameworks I was able to make the slider dynamic and render different content based on the page the user is currently on.

- <strong>Test</strong> : To test this feature I had to check that the slider rendered correctly on each page specified and also on each device size too, thanks to chrome-dev-tools this wasn't that much of a challenge. 

- <strong>Result</strong> : The test passed on all fronts, the content displayed was correctly aligned with that specified in the conditional statement. Also the speed of the slide works as intended.

- <strong>Verdict</strong> : This test has passed based on the above criteria and notes.


## Bugs

#### Bugs During Development: 

<p>During development of this project, I face a few puzzling bugs that proved to be somewhat challenging, being new to Flask, Python etc means that it took me 
somewhat longer to find soltuions and fixes.</p>

<p>Case Sensitive Confusion:</p>

- <strong>Bug</strong> : <p>The code that handles the creation and and registration of the user accounts on `BT` captures the inputted data and then transforms that into lowercase to then store into the database, the code that checks to see what current user was in session was throwing errors because it WAS looking for a case sensitive value.</p>
 
- <strong>Fix</strong> : <p>Altered the code so that it is no longer case sensitive when determining which user is currently active or in session on the website.</p>

- <strong>Verdict</strong> : <p>This bug was squashed and meant I could continue working on other aspects of the project.</p>

<p>Favourites Array Issue:</p>

- <strong>Bug</strong> : <p>When the user adds or removes a beer from their 'my-list' or favourites array with multiple beers on the page, the last rendered beer on the page gets added or removed from the list.</p>
 
- <strong>Fix</strong> : <p>Altering the jQuery selector code fixed this issue and only submits the forms that are the relevant parents of the input.</p>

- <strong>Verdict</strong> : <p>This bug was debugged, dealt with and moved on from.</p>

End To Do
---

## Deployment
BakingMaster was developed in AWS Cloud9. GIT and GitHub was used to store Repository.

### Cloning BakingMaster from GitHub:

<strong>Ensure</strong> you have the following installed:
* PIP
* Python 3
* Flask
* PyMongo
* GIT

<strong>You need to have an account at <a href="https://www.mongodb.com/">MongoDB</a> to create the database.</strong>

* 1: <strong>Clone</strong> the BakingMaster repository by either downloading from <a href="https://github.com/KarolSliwka/Baking_Master"> here</a>, or if you have Git installed typing the following command into your terminal.
```bash
git clone https://github.com/KarolSliwka/Baking_Master.git
```
* 2: <strong>Install</strong> the relevant requirements & dependancies from the requirements.txt file.
```bash
pip3 -r requirements.txt
```
* 3: In your IDE you need to add some variables that can be get through environment. You can add them into <strong>.bashrc</strong> file using commands below to edit file. Make sure you are in you are not in your environemt folder.
```bash
cd ..
nano .bashrc
```
<strong>Make sure names of these variables match names from app.py file.</strong>

    IP, PORT, MONGO URI, SECRET KEY ,API ID, API KEY, EMAILUSERNAME, EMAIL PASSWORD, MAIL SERVER, MAIL PORT

* 4: Run the application using <strong>Run</strong> button in your IDE Dashboard or 
```bash
flask run 
```
or 
```bash
Python3 app.py
```

### Deploying BakingMaster to Heroku:

* 1: Create a <strong>requirements.txt</strong> file using command below.
```bash
pip3 freeze --local > "requirements.txt"
```
* 2: Create a <strong>Procfile</strong> file using command below.
```bash
echo web: python3 app.py > Procfile
```
* 3: Push all files to your repository.
* 4: Create a new application for this project on the Heroku Pages.
* 5: Select your deployment method by clicking on the <strong>deployment</strong> method button and select GitHub.
* 6: Set the following config variables:

**Key**|**Value**
:-----:|:-----:
IP|0.0.0.0
PORT|5000
MONGO\_URI|"mongodb+srv://'username':'password'.egcn1.mongodb.net/'clusterName'?""
SECRET\_KEY|"SECRET-KEY"
API\_ID|"YOUR-ID"
API\_KEY|"YOUR-KEY"
EMAIL\_USERNAME|"YOUR-EMAIL-USERNAME"
EMAIL\_PASSWORD|"YOUR-EMAIL-PASSWORD"
MAIL\_SERVER|"MAIL-PROTOCOL.DOMAIN.EXTENSION"
MAIL\_PORT|"YOUR-PORT-NUMBER"

* 7: Click the deploy button on the Heroku Pages dashboard.
* 8: The site has been deployed the Heroku Pages, Enjoy!;

## Credits / Acknowledgement

Simple and clear design came from heart of the author. Project coloristic was wisely chosen by the author.<br>
*   <a href="https://www.edamam.com" target="_blank">Edamam API - Recipes</a>
*   <a href="https://realfavicongenerator.net/favicon_checker#.X0WHei2ZMUG">Favicon Generator/Checker</a>
*   <a href="https://fonts.google.com/specimen/Roboto">Roboto</a>
*   <a href="https://fontawesome.com">Font-Awesome</a>
*   <a href="https://www.invisionapp.com">InvisionApp</a>

## Contact
If you've got any questions please contact me via email: <a href="mailto:contact@karolsliwka.com">contact@karolsliwka.com</a>

## Disclaimer
The contents of this web application are for educational purposes only.