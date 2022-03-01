# Testing for BeFitness MS4

## User Stories Testing

### As a First Time User, I want to:

* View the site from all devices such as mobile, tablet and desktop.

Outcome: The site is fully responsive in regards to the images, text and functionality working within all viewports.

![responsive](https://github.com/BesnikShala/BeFitness-MS4/blob/main/testing/media/responsive.jpeg?raw=true)

* Browse the products and content without having to create a profile.

Outcome: Users can freely browse products and plans using the navigation dropdown menus. All products are able to be viewed further to show details and add to cart. 

![Browse](https://github.com/BesnikShala/BeFitness-MS4/blob/main/testing/media/viewproduct.jpeg?raw=true)

* Have a clear way of navigating between products and services.

Outcome: Navigating the site is easy and clear to follow. 

![navigate]()

* Be able to search for products/services by keywords.

Outcome: Searching for products is fully availble and easy to use. One issue is trying to search for plans as this clashed when trying to apply two django apps. Therefore only product searches are availble for this feature. 

![search]()

* To have a reason to register an account with the site.

Outcome: Users need to sign up so they can purchase products/plans. They are then able to save their profile details and list previous orders if they sign up. 

![Sign Up](https://raw.githubusercontent.com/BesnikShala/BeFitness-MS4/main/testing/media/42334AD3-D8F0-4048-92F8-DADFDB68BE6D.jpeg)

* Have enough range of products and services to suit my needs.

Outcome: There are 6 different categories for two different services of products and plans. There were many additions I would have liked to add but due to time constraints from continuous issues this was not possible.

![range](https://raw.githubusercontent.com/BesnikShala/BeFitness-MS4/main/testing/media/21EA0974-B163-44A2-9FB4-47DE88D8A12E.jpeg)

* Sort through different products.

Outcome: Sorting through products and plans is available and functions well. This feature has been made optional on larger devices due to the navigation and search capabilities being available on smaller devices. This allows for a cleaner look.

![Sort Products](https://raw.githubusercontent.com/BesnikShala/BeFitness-MS4/main/testing/media/FFFF6E43-962A-49E2-9418-94C8F536097C.jpeg)

### As a Returning User, I want to:

* Securely log into my account.

Outcome: With Django-Allauth users can safely log in as there is a salt hash algorithm which secures users details.

![signin](https://raw.githubusercontent.com/BesnikShala/BeFitness-MS4/main/testing/media/181D812F-6C01-4AB2-806B-701E22CCAB10_4_5005_c.jpeg)

* Securely be able to checkout and pay for products.

Outcome: Stripe payment system is one of the most secure on the market. Therefore the user can safely checkout as all sensitive data is encrypted.

![checkout](https://raw.githubusercontent.com/BesnikShala/BeFitness-MS4/main/testing/media/20480456-D6B1-4C63-8D4F-1B73244636B2.jpeg)

* View my order history.

Outcome: Testing for this passed, users are able to check their previous orders on their profile page.

![history](https://raw.githubusercontent.com/BesnikShala/BeFitness-MS4/main/testing/media/25395CB3-CCF9-40CD-8F2B-F7B5BCE41DBC.jpeg)

![history](https://raw.githubusercontent.com/BesnikShala/BeFitness-MS4/main/testing/media/85FF7392-8691-4BC6-9FC8-2016542BE2EC_4_5005_c.jpeg))


* Edit my profile delivery information.

Outcome: This passed and users can edit their details via their profile page.

![Edit Profile Info](https://raw.githubusercontent.com/BesnikShala/BeFitness-MS4/main/testing/media/C0D78936-2EB7-4DE7-8A2D-8D98B789EACF.jpeg)

* Receive Sign Up confirmation email. 

Outcome: This passed as users will receive confirmation email when signing up.

![Sign Up Confirmation](https://raw.githubusercontent.com/BesnikShala/BeFitness-MS4/main/testing/media/AC3A34B6-5ACD-4EB6-ADE4-C59E814FE6EF_4_5005_c.jpeg)

![Confirm](https://raw.githubusercontent.com/BesnikShala/BeFitness-MS4/main/testing/media/27E9894F-5BB5-4BFD-B666-596DEFA4D130.jpeg)


### As a Site Owner, I want to:

* Be able to add, edit or delete products/services.

Outcome: Admin is able to create, edit and delete products. 

![Edit Product](https://raw.githubusercontent.com/BesnikShala/BeFitness-MS4/main/testing/media/16BC1FCE-CE60-4355-8222-BF3CDC017C18.jpeg)

![Delete Product](https://raw.githubusercontent.com/BesnikShala/BeFitness-MS4/main/testing/media/69BB57F9-B40A-4A78-A941-A718BD23A779.jpeg)

![Add Product](https://raw.githubusercontent.com/BesnikShala/BeFitness-MS4/main/testing/media/8752CE34-5E42-4682-8D27-07C3AE10580A.jpeg)

* Be able to encourage users to sign up to the site.

Outcome: Users will need to register to complete a payment. They will have access to save their contact information and past orders.

![Sign Up](https://raw.githubusercontent.com/BesnikShala/BeFitness-MS4/main/testing/media/42334AD3-D8F0-4048-92F8-DADFDB68BE6D.jpeg)

* Allow users to rate or share their thoughts on the products/services.

Outcome: This feature was not implemented and is in the features left to add due to time contraints.

## User Stories Testing

## Features

* Navigation

Users are able to easily navigate the site via navbar. They also have the use of back buttons when viewing products/plans or in the checkout services. 

Outcome: Passed navigation works well.

![Navigation](https://raw.githubusercontent.com/BesnikShala/BeFitness-MS4/main/testing/media/94E99A9F-8A2B-4CCC-B023-F4318C145511_4_5005_c.jpeg)

* View Products

Users are able to view products within categories. They have the option to expand the product to view product details. At this point they can view product information and have more options to add to bag or return to view other products.

Outcome: All testing for this feature passed as users are able to view all product information and images.

![products](https://raw.githubusercontent.com/BesnikShala/BeFitness-MS4/main/testing/media/5B7ED4CA-32E3-4DAF-A4A4-87607667EC3F.jpeg)

* View Fitness Plans

Users are able to view the plans within categories just as products. They can also expand the plans to show a different layout as the plans will hold more information than the products. 

Outcome: This passed testing and users are able to view plans in the main page and in the plans detail page.

![plans](https://raw.githubusercontent.com/BesnikShala/BeFitness-MS4/main/testing/media/15E29158-7F71-48F0-9E7A-088BEF968056.jpeg)

* Select Quantity

Users can specify the quantity of the products/plans they want to purchase. 

Outcome: Testing passed as users are able to select the quantity they want to add to the bag.

![update](https://raw.githubusercontent.com/BesnikShala/BeFitness-MS4/main/testing/media/4FF3D9A4-E66A-4E00-80A8-CE6A911134B0.jpeg)

* Update Quantity in the Bag

Users can alter the quantity in the bag as they please. 

Outcome: Testing passed as users are able to update the quantity of plans and products.

![update](https://raw.githubusercontent.com/BesnikShala/BeFitness-MS4/main/testing/media/4FF3D9A4-E66A-4E00-80A8-CE6A911134B0.jpeg)

* Remove Products/Plans in the Bag

Users can remove products/plans as they please. 

Outcome: Testing passed users are able to remove any product or plan from the bag.

![remove](https://raw.githubusercontent.com/BesnikShala/BeFitness-MS4/main/testing/media/8C45CFFD-0B20-4ED0-8B9B-E3EF68DD33F6.jpeg)
 

* Sorting Products/Plans

Users can sort products to display and sort by price, category, rating or name. They can view from high to low or low to high. This provides a niche section to make it easier for users to find what they are looking for. 

Outcome: Testing Passed and all products and plans sorting is fully functional.

![Sort Products](https://raw.githubusercontent.com/BesnikShala/BeFitness-MS4/main/testing/media/FFFF6E43-962A-49E2-9418-94C8F536097C.jpeg)

* Search Products

Users are able to search products by key words from the navbar. A responsive search input can sort and find all products that match a key word. This gives the user easy access to find exactly what they are looking for or to sort more specifically by keywords.

Outcome: This passed as users are able to search for all product keywords. This feature is not available for plans on the same input field due to only one url action being available.

![Search](https://raw.githubusercontent.com/BesnikShala/BeFitness-MS4/main/testing/media/searchproductglove.jpeg)

![Search Glove](https://raw.githubusercontent.com/BesnikShala/BeFitness-MS4/main/testing/media/searchproduct.jpeg)

* Checkout / Purchase

Users are able to complete a payment via stripe. They will need to create an account if they want to save order details to their profile or to save products to their cart. 

Outcome: This passed as payments with stripe were successful. 

![Checkout](https://raw.githubusercontent.com/BesnikShala/BeFitness-MS4/main/testing/media/20480456-D6B1-4C63-8D4F-1B73244636B2.jpeg)

* Real Email Confirmation

Users will receive a confirmation of their order with the details they provided. The email will come from Gmail.com, which is the platform used for this service. 

Outcome: Testing passed, real email is sent to email used.

![Order Confirmation](https://raw.githubusercontent.com/BesnikShala/BeFitness-MS4/main/testing/media/72BAD2CD-C5DC-4535-B477-CF8BB5F5B8D0.jpeg)

* Create a Profile / Register

Users are able to create a profile. They are able to save order information and billing/delivery details.

Outcome: This passed. Users are able to successfully create a profile and save their information. 

![Sign Up](https://raw.githubusercontent.com/BesnikShala/BeFitness-MS4/main/testing/media/42334AD3-D8F0-4048-92F8-DADFDB68BE6D.jpeg)
![Edit Profile Info](https://raw.githubusercontent.com/BesnikShala/BeFitness-MS4/main/testing/media/C0D78936-2EB7-4DE7-8A2D-8D98B789EACF.jpeg)

* Add / Edit / Delete Products

The admin will be able to add, edit and delete products and plans.

Outcome: Add, Delete and edit features worked for products and plans (admin user only). 

![Admin](https://raw.githubusercontent.com/BesnikShala/BeFitness-MS4/main/testing/media/admincontrol.jpeg)

* Validate on Delete

The admin may accidentally press the delete button, if so there will be a prompt to confirm if the item selected is to be deleted. The confirmation link will trigger the view to delete the item. Another will redirect back to the main page. 

Outcome: This passed tests for both products and plans. 

![Delete Product](https://raw.githubusercontent.com/BesnikShala/BeFitness-MS4/main/testing/media/69BB57F9-B40A-4A78-A941-A718BD23A779.jpeg)

* Plans 

Users can view and purchase different plans to suit their fitness needs. The users will be able to view plan details and add to cart to purchase.

* Toast Messages

The user and admin will be notfied when using features around the site. If the checkout or bag is used a message will pop up via a toast from bootstrap. This notifies the user of any actions carried out. It will also notfify of any errors.

Outcome: This passed as toasts pop up when a view is triggered. 

![Toast](https://raw.githubusercontent.com/BesnikShala/BeFitness-MS4/main/testing/media/addplantoast.jpeg)


## Validators

* Homepage
![Home](https://raw.githubusercontent.com/BesnikShala/BeFitness-MS4/main/testing/media/7B1A983A-8EEF-456B-9FE1-7C60D41221EB.jpeg)
* Products Page
![Products](https://raw.githubusercontent.com/BesnikShala/BeFitness-MS4/main/testing/media/98980EB6-898E-431D-A5AB-F859E4577AAB.jpeg)
* Plans Page
![Plans](https://raw.githubusercontent.com/BesnikShala/BeFitness-MS4/main/testing/media/FB80F3E2-B877-4441-8551-DD62EE6C91B0.jpeg)
* Sign Up
![Sign up](https://raw.githubusercontent.com/BesnikShala/BeFitness-MS4/main/testing/media/A5118C60-AB76-468A-ADEC-4A8E67F1540C.jpeg)
* Log in
![Login](https://raw.githubusercontent.com/BesnikShala/BeFitness-MS4/main/testing/media/1F79272B-1375-40B6-8CC9-639AE60B3EC2.jpeg)
* Bag
![Bag](https://raw.githubusercontent.com/BesnikShala/BeFitness-MS4/main/testing/media/12F6F154-3CD7-4EC5-B9FD-581CD934B1D2.jpeg)
* Checkout
![Checkout](https://raw.githubusercontent.com/BesnikShala/BeFitness-MS4/main/testing/media/D79F66E0-E74A-418A-82EA-03C53A1DE88D.jpeg)

* CSS
![CSS](https://raw.githubusercontent.com/BesnikShala/BeFitness-MS4/main/testing/media/3949B300-05FA-4CF4-92B5-A3F38C3D2840.jpeg)

* JSHint

![JS](https://raw.githubusercontent.com/BesnikShala/BeFitness-MS4/main/testing/media/BCE457B2-6130-4F2E-8456-BC2D936F18D4.jpeg)

Passed All Validation








