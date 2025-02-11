# Flavour On Fire

<p align="center">
| <a href="https://flavour-on-fire-1bb1fc2c2e8e.herokuapp.com/" target="_blank">Flavour On Fire Project</a> |
</p>


## Introduction
Flavour On Fire is an engaging and vibrant online platform designed for culinary enthusiasts, home cooks, and professional chefs to share, explore and celebrate the art of cooking. Whether you’re a seasoned chef or someone experimenting in the kitchen for the first time, Flavour On Fire brings together a diverse community passionate about food from all cultures and traditions.

At its core, the project allows users to share their unique recipes, discover chef’s specials and connect with culinary creators around the globe. The platform offers an intuitive interface for uploading detailed recipes, including ingredients, step-by-step instructions and captivating images of culinary creations. Users can also browse and get inspired by dishes from fellow food lovers, participate in discussions and view recipes from their favorite chefs.

![Responsive Mockup](static\readme_images\am_i_responsive.PNG)


## Table of Contents

- [Flavour On Fire](#flavour-on-fire)
  - [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
- [UX - User Experience](#ux---user-experience)
  - [Design Inspiration](#design-inspiration)
    - [Wireframes](#wireframes)
    - [Colour Scheme](#colour-scheme)
    - [Font](#font)
- [Project Planning](#project-planning)
  - [Strategy Plane](#strategy-plane)
    - [Site Goals](#site-goals)
- [Agile Methodologies - Project Management](#agile-methodologies---project-management)
    - [MoSCoW Prioritization](#moscow-prioritization)
    - [User Stories](#user-stories) 
- [Surface Planes](#surface-planes)
    - [Website Features](#website-features)
    - [Database Schema - Entity Relationship Diagram](#database-schema---entity-relationship-diagram)
    - [Security](#security)
- [Features](#features)
  - [User View - Registered/Unregistered](#user-view---registeredunregistered)
  - [CRUD Functionality](#crud-functionality)
  - [Future Features](#future-features)
- [Technologies \& Languages Used](#technologies--languages-used)
  - [Libraries \& Frameworks](#libraries--frameworks)
  - [Tools \& Programs](#tools--programs)
- [Testing](#testing)
- [Deployment](#deployment)
  - [Connecting to GitHub](#connecting-to-github)
  - [Django Project Setup](#django-project-setup)
  - [Cloudinary API](#cloudinary-api)
  - [Elephant SQL](#elephant-sql)
  - [Heroku deployment](#heroku-deployment)
- [AI Assistance in Development ](#ai-assistance-in-dvelopment)
- [Credits](#credits)
  - [Code](#code)
  - [Media](#media)
    - [Additional reading/tutorials/books/blogs](#additional-readingtutorialsbooksblogs)
  - [Acknowledgements](#acknowledgements)



# UX - User Experience

## Design Inspiration
The design inspiration for Flavour On Fire stems from the vibrant aesthetics of food culture and the dynamic experience of cooking itself. The warm color palette reflects the rich tones of natural ingredients and the heat of the kitchen, creating an inviting atmosphere. High-quality imagery, clean typography, and intuitive layouts were influenced by the visual appeal and storytelling commonly found in culinary spaces. The balance between a modern, minimalistic design and a cozy, home-like feel ensures the platform is both professional and approachable. Overall, the design captures the passion, creativity, and community spirit that define the culinary world.

### Wireframes

[Balsamiq](https://balsamiq.com/) wireframes were used during the design phase of Flavour On Fire to quickly sketch and plan the layout of the website. This tool allowed me to create low-fidelity mockups of the user interface, focusing on the structure and functionality rather than visual details. Using Balsamiq, I was able to efficiently map out key features and navigation flows, helping to clarify how users would interact with the site. The simple, hand-drawn style of the wireframes made it easier to iterate quickly, gather feedback and refine the design before moving into more detailed stages of development. This approach facilitated better collaboration and ensured that the design met the core user needs early in the process.

#### Large Screen View:
![Window View](static\readme_images\wireframes\window.PNG)

#### Tablet View:
![Tablet View](static\readme_images\wireframes\tablet.PNG)

#### Mobile View:
![Mobile View](static\readme_images\wireframes\mobile.PNG)

### Colour Scheme
![Colour Pallete](static\readme_images\color_pallete.PNG)

### Font
The fonts used in Flavour On Fire are carefully selected to ensure a balance between readability, elegance, and personality. For the main body text and overall website structure, the website utilizes Google’s default font, sans-serif font known for its clean and modern appearance. Its simple yet professional style ensures that the content is easy to read across all devices and screen sizes, making it perfect for presenting recipe instructions, ingredient lists, and general text.

For the video carousel captions, we’ve chosen Courgette, a stylish script font that adds a personal, handwritten touch.

<hr>

# Project Planning

## Strategy Plane
Initially, the project focused on establishing a community-driven platform where users can easily share and discover recipes, as well as interact with chefs and other food enthusiasts. The design phase concentrated on creating an appealing and user-friendly interface, with an emphasis on visual storytelling and intuitive navigation. Once the design was finalized, the technical development phase involved implementing features such as recipe submission forms, search capabilities, and secure user accounts. After the launch, a continuous feedback loop was established to improve and iterate the platform based on real user input, ensuring it remains relevant and dynamic.

### Site Goals
- Recipe Sharing and Exploration.
- Community Engagement.
- Showcase Chef Expertise.
- User-Friendly Experience.
- Content Creation and Interaction.
- Sustainability and Growth.

<hr>

# Agile Methodologies - Project Management

THE project followS Agile planning methods. The project board I created [Github Project Board](https://github.com/users/PrajaktaSarnaik/projects/9) helped track tasksand prioritize features. As the project progressed, I added more user stories and refined to better capture evolving needs and feedback. I’m confident that with the experience gained, the process will be more smooth and efficient next time.

### MoSCoW Prioritization

- **Must Haves**: the 'required', critical components of the project. Completing my 'Must Haves' helped me to reach the MVP (Minimum Viable Product) for this project early, allowing me to develop the project further than originally planned.
  
- **Should Haves**: the components that are valuable to the project but not absolutely 'vital' at the MVP stage. The 'Must Haves' must receive priority over the 'Should Haves'.
- **Could Haves**: these are the features that are a 'bonus' to the project, it would be nice to have them in this phase, but only if the most important issues have been completed first and time allows.

![MoSCoW](static\readme_images\project_board_MoSCoW.PNG)

### User Stories

| User Story | Priority |
|----------------------------------------------------------------------------------------------------------------------------|---------------|
| As a **user**, I can **register for an account** so that **I can log in and access features like reviewing, rating, and sharing recipes.** | **MUST HAVE** |
| As a **user**, I can **log in to my account** so that **I can use all the features of the website.** | **MUST HAVE** |
| As a **user**, I can **view recipes on the website** so that I can **explore new dishes to try.** | **MUST HAVE** |
| As a **logged-in user**, I can **review and rate a recipe so that I can share my feedback and help others decide which recipes to try.** | **MUST HAVE** |
| As a **logged-in user**, I can **edit my reviews** so that **I can update my feedback if needed.** | **MUST HAVE** |
| As a **logged-in user**, I can **delete my reviews** so that **I can remove feedback I no longer wish to share.** | **MUST HAVE** |
| As an **admin**, I can **approve or delete user reviews and recipes** so that **only appropriate content is published on the website.** | **MUST HAVE** |
| As a **visitor**, I am **prompted to log in or register if I try to review, rate, or submit a recipe** so that **unauthorized actions are prevented.** | **MUST HAVE** |
| As a **logged-in user**, I can **submit my own recipes** so that **I can share them with the community.** | **SHOULD HAVE** |
| As a **registered user**, I can **log in to access the Chef's Special page,** so that **I can view exclusive special recipes that are not available on the public index page.** | **SHOULD HAVE** |
| As a **As a user**, I want to **print a story from the application**, so that **I can have a physical copy for offline reading or sharing.** | **COULD HAVE** |
| As a **logged-in user**, I am **notified when my review or recipe is approved or rejected** so that **I am aware of its status.** | **COULD HAVE** |
<hr>

# Surface Planes

## Website Features

### Navbar
- The navigation bar is displayed at the top of the page. 
- It includes the logo and title, which redirect to the homepage when clicked. 
- The navbar links direct the user to the relevant pages when clicked.

![Navbar](static\readme_images\website_features\navbar.PNG)

### Homepage
- The homepage displays all recipes. 
- Each recipe is displayed with a title, image, description and diet.

![Homepage](static\readme_images\website_features\homepage.PNG)

### Recipe Details
- The recipe details page displays the title, image, description, ingredients, instructions, reviews and rating of a recipe. 
- Logged-in users can review and rate the recipe. Users can also edit or delete their reviews.
- Users can directly access reviews section by clicking on comments icon.

![Recipe Details](static\readme_images\website_features\recipe_detail.PNG)

### Register
- Unregistered users can register for an account by providing a username, email, and password. 
- Passwords are hashed for security. 
- The text boxes validate the user's input to ensure data is in the correct format. 

![Register](static\readme_images\website_features\sign_up.PNG)

### Log In
- Users can log in to their account using their username and password. 
- Passwords are hashed for security. 
- The text boxes validate the user's input to ensure data is in the correct format. 

![Log In](static\readme_images\website_features\sign_in.PNG)

### Log Out
- Users can log out of their account. 
- They are redirected to the homepage after logging out.

![Log Out](static\readme_images\website_features\sign_out.PNG)

### Review a Recipe
- Logged-in users can review and rate a recipe. 
- They can provide a review text and a rating from 1 to 5 stars.

![Review](static\readme_images\website_features\review.PNG)

### Edit Review
- Logged-in users can edit their reviews. 
- They can update the review text and rating.

![Edit Review](static\readme_images\website_features\review_edit.PNG)

### Delete Review
- Logged-in users can delete their reviews. 
- They are prompted to confirm the deletion.

![Delete Review](static\readme_images\website_features\delete_review.PNG)

### Print Recipe
- Logged-in users can print a recipe from the application to have a physical copy for offline reading or sharing.

![Print Recipe](static\readme_images\website_features\print_recipe.PNG)

### Our Chef
- Users can access the Our Chefs page to view information about the chef, including a bio and image. 

![Our Chef](static\readme_images\website_features\our_chef.PNG)

### Chef's Special
- Logged-in users can access the Chef's Special page to view exclusive special recipes that are not available on the public index page.
![Chef's Special](static\readme_images\website_features\chef_special.PNG)

### Share a Recipe
- Logged-in users can submit their own recipes. 
- They must provide a title, image, description, ingredients, instructions and diet.
![Share Recipe](static\readme_images\website_features\share_recipe.PNG)

**Admin Panel**

Through Django's built-in Administration Panel, the Admin has full access over the data submitted to the website by registered Users. To access the Admin panel the Admin user adds '/admin/' to the end of the URL to display [https://flavour-on-fire-1bb1fc2c2e8e.herokuapp.com/admin/](https://flavour-on-fire-1bb1fc2c2e8e.herokuapp.com/admin/). A username and password is requested. For Flavor On Fire, Admin approval is needed for articles and comments to keep the site on topic and to prevent spamming. Registered, logged-in users' have instant access to make a booking and upload images.

![Admin Panel](static\readme_images\website_features\admin_panel.PNG)
*Django Admin panel view for Flavor On Fire Administrator - content selection menu on left hand side*  

Users recipes and reviews require approval by the Admin of Flavor On Fire to keep the website content on topic. 

#### Dropdown menu allowing Admin to 'publish' a users article, 'Save' button must be clicked to confirm
![Screenshot of published recipe](static\readme_images\website_features\admin_recipe_publish.PNG)
*Admin can change the status of recipes from 'Draft' to 'Published'.*
 
#### Checkbox for allowing Admin to 'approve' a users comment, 'Save' must be clicked to confirm
![Screenshot of comment approval](static\readme_images\website_features\admin_comment_approval.PNG) 
*Admin can approve the reviews.*
 
## Database Schema - Entity Relationship Diagram 

The database schema for the Flavour On Fire project was designed using an Entity Relationship Diagram (ERD). This diagram visually represents the database structure, including the tables, fields and relationships between entities. The ERD for Flavour On Fire includes the following entities: User, Recipe, Review,  and Author(Chef). Each entity has specific attributes and relationships to other entities, forming a coherent and organized database schema. The ERD provides a clear overview of the database structure, facilitating the development and maintenance of the project.

![ERD](static\readme_images\erd1.PNG)

## Security

A number of security steps were taken in this project in order to protect the user's submitted data. Unlike a strictly informative website, Flavour on Fire allows the user to become part of the community and to write reviews and share recipes. To meet the strict internet standards of protecting a user's data, the following processes were included in the project's development.

**AllAuth**  

Django AllAuth is an installable framework that takes care of the user registration and authentication process. Authentication was needed to determine when a user was registered or unregistered and it controlled what content was accessible on Flavour on Fire. The setup of AllAuth included:

- installing it to my workspace dependencies
- adding it to my INSTALLED_APPS in my settings.py
- sourcing the AUTHENTICATION_BACKENDS from the AllAuth docs for my settings.py
- adding its URL to my projects 'urls.py'
- run database migrations to create the tables needed for AllAuth

- **User Authentication**: Users can register for an account, log in, log out, and reset their password. Passwords are hashed using Django's built-in hashing library.
- **Permissions**: Users can only edit or delete their own reviews and recipes. Admins can approve or delete reviews and recipes.
- **Cross-Site Request Forgery (CSRF) Protection**: CSRF tokens are used in forms to prevent unauthorized requests.

**Defensive Design**  

Flavour on Fire was developed to ensure a smooth user experience, to the best of my current learning experience with Django. 

- Input validation and error messages provide feedback to the user to guide them towards the desired outcome. 
- Unregistered users are diverted to the Sign Up page from restricted access pages. 
- Authentication processes control edit/delete icons to reveal them to the content author only. 
- Deletion of data is confirmed through an additional modal, double-checking with the user.
- Testing and validation of features completes the process.

<hr>

# Features

## User View - Registered/Unregistered

From the very beginning, it was important that Flavour On Fire be accessible to unregistered users in meaningful ways. The goal was to engage new visitors quickly by allowing them to explore community-driven content such as recipes, print feature and enticing them to become part of the platform. By offering valuable information upfront, the site aims to foster interest and encourage user registration for deeper interaction. Below is a breakdown of the site's accessibility for both registered and unregistered users:

| **Feature**       | **Unregistered User**                                                                 | **Registered, Logged-In User**                                              |
|-------------------|--------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| **Home Page**     | Visible                                                                              | Visible                                                                     |
| **Recipes**       | Visible but not interactable via 'Rating/Reviews' | Visible with full feature interaction, including the ability to Rate, Review, Edit and Delete own reviews |
| **Recipe Details**       | Visible and shows full recipe in detail with the facility of printing the recipe | Visible and shows full recipe in detail with the facility of printing the recipe |
| **Recipe Share**       | Visible but not interactable to share their own recipes on the website | Visible with full feature interaction, including the ability to share their own recipes |
| **Chef's Special**| Not visible until logged in                       | Visible all the chef's exclusive recipes with full feature interaction available                             |
| **Our Chefs**       | Visible with all the details                             | Visible with all the details                              |   


## CRUD Functionality

The CRUD (Create, Read, Update, Delete) functionality is a core feature of Flavour On Fire, allowing users to interact with the platform in a dynamic and engaging way. Users can create, view, edit and delete content, such as rating, reviews, to share their feedback with the community. The CRUD functionality enhances user participation and collaboration, enabling users to contribute to the platform's content and engage with other food enthusiasts. Below is a summary of the CRUD features available on Flavour On Fire:

| **Feature**       | **Create** | **Read** | **Update** | **Delete** |
|-------------------|------------|----------|------------|------------|
| **Ratings**       | Yes- Created upon registration or login        | Yes      | Yes- Created upon registration or login        | Yes        |
| **Reviews**       | Yes- Created upon registration or login        | Yes      | Yes-Created upon registration or login        | Full review deletion is available upon registration and login, the comments dashboard clears the review automatically if a user deletes the review       |



