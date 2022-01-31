![Responsive](https://github.com/BesnikShala/BeFitness-MS4/blob/main/testing/media/responsive.jpeg?raw=true)


# BeFitness | Milestone Project 4

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

The user and admin will be notfied when using features around the site. If the checkout or bag is used a message will pop up via a toast from bootstrap. This notifies the user of any actions carrief out. It will also notfify of any errors.


## Features Left to Implement

* Remove Plans from checkout

There was a clash with two apps (products and plans) merging together to work with the bag app. I did not have time to fix the issue of removing plans in the checkout.

* Product Reviews

Users will be able to write a review and view reviews of products/plans. 

## Technologies

## Testing

## Deployment





