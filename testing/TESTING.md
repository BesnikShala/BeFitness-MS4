# Testing for BeFitness MS4

## User Stories Testing

### As a First Time User, I want to:

* View the site from all devices such as mobile, tablet and desktop.

Outcome: The site is fully responsive in regards to the images, text and functionality working within all viewports. One issue caught when testing on mobile/tablet is the burger Icon for the mobile nav is not rendering propperly. 

![]()

* Browse the products and content without having to create a profile.

Outcome: Users can freely browse products and plans using the navigation dropdown menus. All products are able to be viewed further to show details and add to cart. 

![]()

* Have a clear way of navigating between products and services.

Outcome: Navigating the site is easy and clear to follow. One exception being the mobile nav icon not rendering propperly for mobile and tablet view. 

![]()

* Be able to search for products/services by keywords.

Outcome: Searching for products is fully availble and easy to use. One issue is trying to search for plans as this clashed when trying to apply two django apps. Therefore only product searches are availble for this feature. 

![]()

* To have a reason to register an account with the site.

Outcome: At this moment in time unfortunately due to many issues Users would be able to save their profile details and list previous orders if they sign up. 

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

Outcome: Testing for this failed due to the crash between data being added from plans app and the products app. This is an issue which can be resolved however due to time constraints in this moment in time this failed. Users can see broef order history on their profile page however a confirmation window does not render.

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

![]()



