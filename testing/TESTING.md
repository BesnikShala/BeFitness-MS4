# Testing for BeFitness MS4

## User Stories Testing

### As a First Time User, I want to:

* View the site from all devices such as mobile, tablet and desktop.

Outcome: The site is fully responsive in regards to the images, text and functionality working within all viewports. One issue caught when testing on mobile/tablet is the burger Icon for the mobile nav is not rendering propperly. 

![responsive](https://github.com/BesnikShala/BeFitness-MS4/blob/main/testing/media/responsive.jpeg?raw=true)

* Browse the products and content without having to create a profile.

Outcome: Users can freely browse products and plans using the navigation dropdown menus. All products are able to be viewed further to show details and add to cart. 

![Browse](https://github.com/BesnikShala/BeFitness-MS4/blob/main/testing/media/viewproduct.jpeg?raw=true)

* Have a clear way of navigating between products and services.

Outcome: Navigating the site is easy and clear to follow. One exception being the mobile nav icon not rendering propperly for mobile and tablet view. 

![navigate](https://github.com/BesnikShala/BeFitness-MS4/blob/main/testing/media/productnav.jpeg?raw=true)

* Be able to search for products/services by keywords.

Outcome: Searching for products is fully availble and easy to use. One issue is trying to search for plans as this clashed when trying to apply two django apps. Therefore only product searches are availble for this feature. 

![search](https://github.com/BesnikShala/BeFitness-MS4/blob/main/testing/media/searchproductglove.jpeg?raw=true)

* To have a reason to register an account with the site.

Outcome: At this moment in time unfortunately due to many issues there are not many incentives for users to sign up apart from they would be able to save their profile details and list previous orders if they sign up. 

![]()

* Have enough range of products and services to suit my needs.

Outcome: There are 6 different categories for two different services of products and plans. There were many additions I would have liked to add but due to time constraints from continuous issues this was not possible.

![]()

* Sort through different products.

Outcome: Sorting through products and plans is available and functions well. This feature has been made optional on larger devices due to the navigation and search capabilities being available on smaller devices. This allows for a cleaner look.

![]()

### As a Returning User, I want to:

* Securely log into my account.

Outcome: With Django-Allauth users can safely log in as there is a salt hash algorithm which secures users details.

![]()

* Securely be able to checkout and pay for products.

Outcome: Stripe payment system is one of the most secure on the market. Therefore the user can safely checkout as all sensitive data is encrypted.

![]()

* View my order history.

Outcome: Testing for this passed, users are able to check their previous orders on their profile page.

![]()

* Edit my profile delivery information.

Outcome: This passed and users can edit their details via their profile page.

![]()

* Select product sizes where applicable.

Outcome: This is a feature which is only on products with sizes so this does work along with quantity. One testing issue is this is not rendering on the checkout bag when placing an order. 

![]()

* Receive email confirmation of orders. 

Outcome: This failed again due to the clash in information going through from the plan app. Email confirmation when registering render but the order confirmation doesnt. The orders log to the profile and the toast notifications notofy the user that the order was successful and they are presented with a order number confirmation.

![]()

### As a Site Owner, I want to:

* Be able to add, edit or delete products/services.

Outcome: Admin is able to create, edit and delete products. However editing plans failed when testing.

![]()

* Be able to encourage users to sign up to the site.
s
Outcome: Users will need to register to complete a payment. They will have access to save their contact information and past orders.

* Allow users to rate or share their thoughts on the products/services.

Outcome: This feature was not implemented and is in the features left to add due to time contraints.

## User Stories Testing

## Features

* Navigation

Users are able to easily navigate the site via navbar. They also have the use of back buttons when viewing products/plans or in the checkout services. 

Outcome: As mentioned previously all navigations work apart from a visual issue with the burger mobile icon.

![]()

* View Products

Users are able to view products within categories. They have the option to expand the product to view product details. At this point they can view product information and have more options to add to bag or return to view other products.

Outcome: All testing for this feature passed as users are able to view all product information and images.

![]()

* View Fitness Plans

Users are able to view the plans within categories just as products. They can also expand the plans to show a different layout as the plans will hold more information than the products. 

Outcome: This passed testing and users are able to view plans in the main page and in the plans detail page.

![]()

* Select Quantity

Users can specify the quantity of the products/plans they want to purchase. 

Outcome: The testing for this passed with one issue of the sizes not being able to adjust it in the checkout section. This is due to a clash between the data from products and plans meeting in the same checkout app. 

![]()
 

* Sorting Products/Plans

Users can sort products to display and sort by price, category, rating or name. They can view from high to low or low to high. This provides a niche section to make it easier for users to find what they are looking for. 

Outcome: Testing Passed and all products and plans sorting is fully functional.

![]()

* Search Products

Users are able to search products by key words from the navbar. A responsive search input can sort and find all products that match a key word. This gives the user easy access to find exactly what they are looking for or to sort more specifically by keywords.

Outcome: This passed as users are able to search for all product keywords. This feature is not available for plans on the same input field due to only one url action being available.

![]()

* Checkout / Purchase

Users are able to complete a payment via stripe. They will need to create an account if they want to save order details to their profile or to save products to their cart. 

Outcome: This passed as payments with stripe were successful. 

![]()

* Real Email Confirmation

Users will receive a confirmation of their order with the details they provided. The email will come from Gmail.com, which is the platform used for this service. 

Outcome: Fail. This feature was fully functional until the integration between product app and plan app. The mix in information meant many errors occuring which were not forseen.

![]()

* Select Size

Users can choose sizes and quantity on products which have sizes. They can also alter the quantity within the checkout cart before payment. 

Outcome: The testing for this passed with one issue of the sizes not rendering on the checkout page. This is due to a clash between the data from products and plans meeting in the same checkout app. 

* Create a Profile / Register

Users are able to create a profile. They are able to save order information and billing/delivery details.

Outcome: This passed. Users are able to successfully create a profile and save their information. 

![]()

* Add / Edit / Delete Products

The admin will be able to add new products, amend any product or even delete anything from the site including other posts.

Outcome: Add, Delete and edit features worked for products (admin users) Editing plans failed testing due to unknown error. No error message rendered. This was fully functional prior to the integration of plans and products with the checkout app. 

![]()

* Validate on Delete

The admin may accidentally press the delete button, if so there will be a prompt to confirm if the item selected is to be deleted. The confirmation link will trigger the view to delete the item. Another will redirect back to the main page. 

Outcome: This passed tests for both products and plans. 

![]()

* Plans 

Users can view and purchase different plans to suit their fitness needs. The users will be able to view plan details and add to cart to purchase.

* Toast Messages

The user and admin will be notfied when using features around the site. If the checkout or bag is used a message will pop up via a toast from bootstrap. This notifies the user of any actions carrief out. It will also notfify of any errors.

Outcome: This passed as toasts pop up when a view is triggered. 


## Validators

### HTML

* Passed all Html Validators

### CSS

* Passed CSS Validator

### JS

* Passed all Js Validator

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

## Deployment

This project was developed using Gitpod IDE and pushed to Github using the in-built terminal. However, because Github can only host static websites it was necessary to deploy this project to Heroku because it is a compatible hosting platform for a back-end focused site like Joyce English School. The master branch of this repository is the most current version and has been used for the deployed version of the site.

The Code Institute student template was used to create this project.

Code Institute Full Template

This project was deployed using Heroku and stored in GitHub.

### Project and Repository Creation

* Navigate to Github.
* Create a new repository by first clicking the green button labeled new on the top left of the screen.
* Select the Code Institute template in the templates section.
* Give the repository a name, in this case Joyce-English-School-MS4.
* Click the green 'Create Repository' button at the bottom of the page.
* Inside the repository click the green 'gitpod' button to initialize your repository.
* Future access to this workspace must be gained through gitpod workspaces, clicking the green button in gitpod again will initialize a new workspace.
* Use the git add . command to add all modified and new files to the staging area.
* Use the git commit -m command to commit a change to the local repository.
Use the git push command to push all committed changes to github.
* Before deploying the website to Heroku, the following three must be followed to allow the app to work in Heroku:

* Create requirements.txt file that contains the names of packages being used in Python. It is important to update this file if other packages or * modules are installed during project development by using the following command:

* pip freeze --local > requirements.txt
* Create Procfile that contains the name of the application file so that Heroku knows what to run. If the Procfile has a blank line when it is created remove this as this may cause problems.

* Push these files to GitHub.

* Install psycopg2 and dj_datatbase_url in your workspace cli.

* Once those steps are done, the website can be deployed in Heroku using the steps listed below:

* Deployment Steps
Log into Heroku .
Click the New button.
Click the option to create a new app.
Enter the app name in lowercase letters.
Select the correct geographical region.
Connect Heroku app to Github repository
In heroku select the deploy tab.
Click github button.
Enter the repository name and click search.
Select the relevant repository and click connect.
Add Heroku Postgres Database
Click the resources tab in heroku.
Under Add-ons search for heroku postgres.
Click on heroku postgres when it appears.
Select the Hobby Dev-Free option in plans.
Click submit order form.
Setting up environment variables
In the heroku settings click the reveal config vars button and set the following variables:
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
DATABASE_URL
EMAIL_HOST_PASS
EMAIL_HOST_USER
SECRET_KEY
STRIPE_PRICE_ID
STRIPE_PUBLIC_KEY
STRIPE_SECRET_KEY
STRIPE_WH_SECRET
USE_AWS
The values of these variables are secret and for security purposes will not be shared here.
Setting up the AWS s3 bucket
Create an Amazon AWS account
Search for S3 and create a new bucket
Allow public access
Under Properties > Static website hosting
Enable
index.html as index.html
save
Under Permissions > CORS use the following:
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
Under Permissions > Bucket Policy:
Generate Bucket Policy and take note of Bucket ARN
Chose S3 Bucket Policy as Type of Policy
For Principal, enter *
Enter ARN noted above
Add Statement
Generate Policy
Copy Policy JSON Document
Paste policy into Edit Bucket policy on the previous tab
Save changes
Under Access Control List (ACL):
For Everyone (public access), tick List
Accept that everyone in the world may access the Bucket
Save changes
AWS IAM (Identity and Access Management) setup

From the IAM dashboard within AWS, select User Groups:
Create a new group
Click through and Create Group
Select Policies:
Create policy
Under JSON tab, click Import managed policy
Choose AmazongS3FullAccess
Edit the resource to include the Bucket ARN noted earlier when creating the Bucket Policy
Click next step and go to Review policy
Give the policy a name and description of your choice
Create policy
Go back to User Groups and choose the group created earlier
Under Permissions > Add permissions, choose Attach Policies and select the one just created
Add permissions
Under Users:
Choose a user name
Select Programmatic access as the Access type
Click Next
Add the user to the Group just created
Click Next and Create User
Download the .csv containing the access key and secret access key.
THE .csv FILE IS ONLY AVAILABLE ONCE AND CANNOT BE DOWNLOADED AGAIN.
Connecting Heroku to AWS S3

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
* In Github go to (https://github.com/AideenM12/Joyce-English-School-MS4).
* In the top right hand corner click "Fork".


## Credits

#### Media

* All fitness images of women and men came from [unsplash.com](https://unsplash.com/)

* Images of gym wraps and gloves came from [Alibaba](https://www.alibaba.com/)

* Images of clothing used from Boutique Ado Walkthrough Project 


## Content

The code displayed on this site has mainly come from the walkthrough project with small tweaks and modifications

The many ongoing issues with the two product and plan app which I decided to implement near the end of the project completely crashed and caused many errors. I would like to appologise for the lack of quality in both the end result of the site and the README.md

## Acknowledgments

* I would like to say a big thank you to Tim Nelson my mentor who has been nothing but brilliant since our first session. 

* I would like to say a big thank you to the tutor support team who I have only gotten to interact with at the end of the course for their help. A special shout out to Sean_ci and Igor_ci of whom which went out of their way to help me even when they did not need to. 




