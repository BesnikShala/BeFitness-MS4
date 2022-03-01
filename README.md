![Responsive](https://github.com/BesnikShala/BeFitness-MS4/blob/main/testing/media/responsive.jpeg?raw=true)


# BeFitness | Milestone Project 4

View the live site here - [BeFitness](https://befitness-ms4.herokuapp.com/)

BeFitness is a E-commerce site where users are able to purchase fitness products, nutrition plans and exercise plans. Users can browse the site for their needs to achieve their fitness goals. They can set up an account in order to complete purchases, rate products, and even post their fitness gains and achievments. The site allows the owner to create online sales via products or fitness plans, adding a social aspect to the site can generate more online traffic and attention to the site hopefully generating more sales and giving users a reason to come back. 


# User Experience

## User Stories

### As a First Time User, I want to:

* View the site from all devices such as mobile, tablet and desktop.

* Browse the products and content without having to create a profile.

* Have a clear way of navigating between products and services.

* Be able to search for products/services by keywords.

* To have a reason to register an account with the site.

* Have enough range of products and services to suit my needs.

* Sort through different products.

### As a Returning User, I want to:

* Securely log into my account.

* Securely be able to checkout and pay for products.

* View my order history.

* Edit my profile delivery information.

* Select product sizes where applicable.

* Receive email confirmation of orders. 

### As a Site Owner, I want to:

* Be able to add, edit or delete products/services.

* Be able to encourage users to sign up to the site.

* Make sure payments are secure.

* Allow users to rate or share their thoughts on the products/services.

## Design

### Colour Scheme

* The main colour scheme of my site is Black and Yellow with a white and elegant background. The idea is to keep the colours and desing minimalistic
to show off the content. The imagery is key to products as the user is ideally paying for a service or product without seeing it in person. The images
and text are the providers vital information. In order to make these components stick out I have chosen light colours.  

### Typography

* I have used google fonts for this project again and the main font I have chosen is 'Lato'. This is for the simplicity and readability of the font. It is very clear and easy to read especially when using letter spacing as the text sits very well when centered. The other font used is Sans Serif, however this is a fallback font just incase google fonts cannot load. Again Sans Serif is widely used and very simple and easy to read. As this is mainly a recipe app and want to be able to easily read the information being given. Lato is dervied from Sans Serif so even if the font should fail it's replacement is very similiar.

### Icons

* Font Awesome 5.13.1 - I chose to use Font Awesone Icons instead of the Materialise Icons due to there being much more range and options. They are also better to target and style. They are also responsive on all screensizes.

### Imagery

* The majority of the images for products have been sourced from existing E-commerce sites with full reference of each image. The main site images have been sourced form professional sites such as Pexels and unsplash. The images are able to be changed by the admin. Users have access to upload and image for their profile. The images as mentioned are key when going for a minimalistic style as the images take focal point and attract the users to either view products or read more about them. I have spent a great deal in finding the best images to display so that the site can be both enticing and visually attractive for new users and returning users. 

### Wireframes

* The wireframes were drawn using Balsamiq. They have differed from the actual rendering of the site. With great recommendations from my mentor I was able to implement design changes which slightly differ from the intial design. 

Click to view all Wireframes in folder [here!](https://github.com/BesnikShala/BeFitness-MS4/tree/main/wireframes)

![Wireframe 1](https://raw.githubusercontent.com/BesnikShala/BeFitness-MS4/main/wireframes/login-wireframe.jpeg)
![Wireframe 2](https://raw.githubusercontent.com/BesnikShala/BeFitness-MS4/main/wireframes/register-wireframe.jpeg)
![Wrieframe 3](https://raw.githubusercontent.com/BesnikShala/BeFitness-MS4/main/wireframes/home-wireframe.jpeg)
![Wrieframe 4](https://raw.githubusercontent.com/BesnikShala/BeFitness-MS4/main/wireframes/product-wireframe.jpeg)
![Wrieframe 5](https://raw.githubusercontent.com/BesnikShala/BeFitness-MS4/main/wireframes/product-detail-wireframe.jpeg)
![Wrieframe 6](https://raw.githubusercontent.com/BesnikShala/BeFitness-MS4/main/wireframes/profile-wireframe.jpeg)
![Wrieframe 7](https://raw.githubusercontent.com/BesnikShala/BeFitness-MS4/main/wireframes/plan-wireframe.jpeg)

### Database Schema

![Database Schema](https://raw.githubusercontent.com/BesnikShala/BeFitness-MS4/main/media/database-schem.jpeg)

* The relationship database revolves around the two apps called Products and Plans. The design changed initially and I decided to make two different types of services. The plans are workout's which consumers can purchase. The products are physical products such as clothes and equipment. The core focus is the products and plans as Users can hopefully find what they are looking for. The link starts when a user creates a UserProfile which has all the necessary data which communicates with the order and orderlineitem. They can save their data and view their previous order on the profile page. 

## Features

* Navigation

Users are able to easily navigate the site via navbar. They also have the use of back buttons when viewing products/plans or in the checkout services. 

* View Products

Users are able to view products within categories. They have the option to expand the product to view product details. At this point they can view product information and have more options to add to bag or return to view other products.

* View Fitness Plans

Users are able to view the plans within categories just as products. They can also expand the plans to show a different layout as the plans will hold more information than the products. 

* Select Quantity

Users can specify the quantity of the products/plans they want to purchase. 

* Sorting Plans

Users can sort between plans via category, price, rating and name. This gives the user more flexibility in narrowing down what they want. 

* Sorting Products

Users can sort products to display and sort by price, category, rating or name. They can view from high to low or low to high. This provides a niche section to make it easier for users to find what they are looking for. 

* Search Products

Users are able to search products by key words from the navbar. A responsive search input can sort and find all products that match a key word. This gives the user easy access to find exactly what they are looking for or to sort more specifically by keywords. 

* Checkout / Purchase

Users are able to complete a payment via stripe. They will need to create an account if they want to save order details to their profile or to save products to their cart. 

* Real Email Confirmation

Users will receive a confirmation of their order with the details they provided. The email will come from Gmail.com, which is the platform used for this service. 

* Select Size

Users can choose sizes and quantity on products which have sizes. They can also alter the quantity within the checkout cart before payment. 

* Create a Profile / Register

Users are able to create a profile. They are able to save order information and billing/delivery details.

* Add / Edit / Delete Products

The admin will be able to add new products, amend any product or even delete anything from the site including other posts.

* Validate on Delete

The admin may accidentally press the delete button, if so there will be a prompt to confirm if the item selected is to be deleted. The confirmation link will trigger the view to delete the item. Another will redirect back to the main page. 

* Plans 

Users can view and purchase different plans to suit their fitness needs. The users will be able to view plan details and add to cart to purchase.

* Toast Messages

The user and admin will be notfied when using features around the site. If the checkout or bag is used a message will pop up via a toast from bootstrap. This notifies the user of any actions carried out. It will also notfify of any errors.


## Features Left to Implement

* Remove Plans from checkout

There was a clash with two apps (products and plans) merging together to work with the bag app. I did not have time to fix the issue of removing plans in the checkout.

* Product Reviews

Users will be able to write a review and view reviews of products/plans. 


## Technologies Used

This project is primarily built using HTML5 semantic markup, CSS stylesheets, Javascript, Python, Django, SQLite and Heroku Postgres.

#### Python

The following Python modules were used on this project:

* asgiref==3.4.1
* backports.zoneinfo==0.2.1
* boto3==1.20.41
* botocore==1.23.41
* dj-database-url==0.5.0
* Django==3.2
* django-allauth==0.41.0
* django-countries==7.2.1
* django-crispy-forms==1.13.0
* django-storages==1.12.3
* gunicorn==20.1.0
* jmespath==0.10.0
* oauthlib==3.1.1
* Pillow==9.0.0
* psycopg2-binary==2.9.3
* python3-openid==3.2.0
* pytz==2021.3
* requests-oauthlib==1.3.0
* s3transfer==0.5.0
* sqlparse==0.4.2
* stripe==2.65.0

* Django was used as the main python framework in the building of this project.

* jQuery

This framework was used to create some of the site's interactive functions.

* Gitpod

This project was built using Gitpod as the IDE.

*Github

Github was used for online version control and storing files and documents.

* Heroku

Heroku was used as a cloud-based platform to deploy this site.

* Google fonts

The font styles used on this website were chosen from Google fonts.


* Fontawesome

The icons used on this page were found in Fontawesome.

* SQLite

SQLite was used as the database for the creation and development of this project.

* Heroku Postgres

Heroku was used as the database for this project in production mode after deployment to Heroku.

* Jinja

Jinja was used for templating.

* Stripe

Stripe payments were used to build the card payment system of this site.

* AWS-Amazon Web Services

AWS was used to store all media and static files of this site in production mode.

* Balsamiq

The wireframes for this project were created using Balsamiq.

* Am I Responsive

This was used to test the responsiveness of the site and also to create the mock-up image presented at the start of this document.


* Coolors.co

Coolors.co was used to create the project's color palette.

* StackOverflow

Stack Overflow was used as a general reference resource.

## Testing

Testing information can be seen here in a separate file - [TESTING.md File](https://github.com/BesnikShala/BeFitness-MS4/blob/main/testing/TESTING.md)

## Deployment

This project was developed using Gitpod IDE and pushed to Github using the in-built terminal. However, because Github can only host static websites it was necessary to deploy this project to Heroku because it is a compatible hosting platform for a back-end focused. The master branch of this repository is the most current version and has been used for the deployed version of the site.

The Code Institute student template was used to create this project.

Code Institute Full Template

This project was deployed using Heroku and stored in GitHub.

### Project and Repository Creation

* Navigate to Github.
* Create a new repository by first clicking the green button labeled new on the top left of the screen.
* Select the Code Institute template in the templates section.
* Give the repository a name, in this case BeFitness-MS4.
* Click the green 'Create Repository' button at the bottom of the page.
* Inside the repository click the green 'gitpod' button to initialize your repository.
* Future access to this workspace must be gained through gitpod workspaces, clicking the green button in gitpod again will initialize a new workspace.
* Use the git add . command to add all modified and new files to the staging area.
* Use the git commit -m command to commit a change to the local repository.
* Use the git push command to push all committed changes to github.
* Before deploying the website to Heroku, the following three must be followed to allow the app to work in Heroku:

* Create requirements.txt file that contains the names of packages being used in Python. It is important to update this file if other packages or * modules are installed during project development by using the following command:

* pip freeze --local > requirements.txt
* Create Procfile that contains the name of the application file so that Heroku knows what to run. If the Procfile has a blank line when it is created remove this as this may cause problems.

* Push these files to GitHub.

* Install psycopg2 and dj_datatbase_url in your workspace cli.

* Once those steps are done, the website can be deployed in Heroku using the steps listed below:


#### Deployment Steps


- Log into Heroku .

- Click the New button.

- Click the option to create a new app.

- Enter the app name in lowercase letters.

- Select the correct geographical region.

- Connect Heroku app to Github repository

- In heroku select the deploy tab.

- Click github button.

- Enter the repository name and click search.

- Select the relevant repository and click connect.

- Add Heroku Postgres Database

- Click the resources tab in heroku.

- Under Add-ons search for heroku postgres.

- Click on heroku postgres when it appears.

- Select the Hobby Dev-Free option in plans.

- Click submit order form.

- Setting up environment variables

- In the heroku settings click the reveal config vars button and set the following variables:

- AWS_ACCESS_KEY_ID

- AWS_SECRET_ACCESS_KEY

- DATABASE_URL

- EMAIL_HOST_PASS

- EMAIL_HOST_USER

- SECRET_KEY

- STRIPE_PRICE_ID

- STRIPE_PUBLIC_KEY

- STRIPE_SECRET_KEY

- STRIPE_WH_SECRET

- USE_AWS

- The values of these variables are secret and for security purposes will not be shared here.

- Setting up the AWS s3 bucket

- Create an Amazon AWS account

- Search for S3 and create a new bucket

- Allow public access

- Under Properties > Static website hosting

- Enable

- index.html as index.html

- save

- Under Permissions > CORS use the following:

[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]


- Under Permissions > Bucket Policy:

- Generate Bucket Policy and take note of Bucket ARN

- Chose S3 Bucket Policy as Type of Policy

- For Principal, enter *

- Enter ARN noted above

- Add Statement

- Generate Policy

- Copy Policy JSON Document

- Paste policy into Edit Bucket policy on the previous tab

- Save changes

- Under Access Control List (ACL):

- For Everyone (public access), tick List

- Accept that everyone in the world may access the Bucket

- Save changes

- AWS IAM (Identity and Access Management) setup


- From the IAM dashboard within AWS, select User Groups:

- Create a new group

- Click through and Create Group

- Select Policies:

- Create policy

- Under JSON tab, click Import managed policy

- Choose AmazongS3FullAccess

- Edit the resource to include the Bucket ARN noted earlier when creating the Bucket Policy

- Click next step and go to Review policy

- Give the policy a name and description of your choice

- Create policy

- Go back to User Groups and choose the group created earlier

- Under Permissions > Add permissions, choose Attach Policies and select the one just created

- Add permissions

- Under Users:

- Choose a user name

- Select Programmatic access as the Access type

- Click Next

- Add the user to the Group just created

- Click Next and Create User

- Download the .csv containing the access key and secret access key.

- THE .csv FILE IS ONLY AVAILABLE ONCE AND CANNOT BE DOWNLOADED AGAIN.

- Connecting Heroku to AWS S3

* Install boto3 and django-storages
* pip3 install boto3
* pip3 install django-storages
* pip3 freeze > requirements.txt
* Add the values from the .csv you downloaded to your Heroku Config Vars under Settings:
* Delete the DISABLE_COLLECTSTATIC variable from your Cvars and deploy your Heroku app
* With your S3 bucket now set up, you can create a new folder called media (at the same level as the newly added static folder) and upload any * required media files to it.
* PLEASE MAKE SURE media AND static FILES ARE PUBLICLY ACCESSIBLE UNDER PERMISSIONS
* Enable automatic deployment:
* Click the Deploy tab
* In the Automatic deploys section, choose the branch you want to deploy from then click Enable Automation Deploys.
* Connect app to Github Repository
* Click the deploy tab and connect to GitHub.
* Type the name of the repository into the search bar presented.
* Click the Code dropdown button next to the green Gitpod button.
* When the correct repository displays click the connect button.

#### Making a clone to run locally

* It is important to note that this project will not run locally unless an env.py file has been set up by the user which contains the IP, PORT, MONGO_DBNAME, MONGO_URI and SECRET_KEY which hav* e all been kept secret in keeping with best security practices.

* Log into GitHub.
* Select the respository.
* Click the Code dropdown button next to the green Gitpod button.
* Download ZIP file and unpackage locally and open with IDE. Alternatively copy the URL in the HTTPS box.
* Open the alternative editor and terminal window.
* Type 'git clone' and paste the copied URL.
* Press Enter. A local clone will be created.
* Once the project been loaded into the IDE it is necessary to install the necessary requirements which can be done by typing the following command.

* -pip install -r requirements.txt
* How to Fork the respository.
* Log into GitHub.
* In Github go to (https://github.com/BesnikShala/BeFitness-MS4).
* In the top right hand corner click "Fork".


## Credits

#### Media

* All fitness images of women and men came from [unsplash.com](https://unsplash.com/)

* Images of gym wraps and gloves came from [Alibaba](https://www.alibaba.com/)

* Images of clothing used from Boutique Ado Walkthrough Project 


## Content

The code displayed on this site has mainly come from the walkthrough project with small tweaks and modifications


## Acknowledgments

* I would like to say a big thank you to Tim Nelson my mentor who has been nothing but brilliant since our first session.

* Big thank you to tutor support for helping me in times of need. 

* The Slack community for being a pillar of support.





