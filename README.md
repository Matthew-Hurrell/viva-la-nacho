# **Viva La Nacho**

Viva La Nacho is a full stack web application that gives users a platform to view and share Mexican recipes. The intention of the site is to provide a simple, intuitive, visually appealing and user friendly platform for users to share Mexican inspired recipes and interact with the community. The intended target audience is anyone with an interest in cooking and Mexican food. The target audience will mostly span across men and women from young adults to older generations. 

The application impliments user authorisation and full CRUD functionality, allowing users to create, update, read and delete recipes stored in a relational database management system. Users can also like recipes to save them to their favourites list and interact with other users via recipe comments. 

The site also features a back end admin dashboard that allows an administrator to review and approve user comments, as well as monitor and edit recipes and users. 

Link to the live site - [Viva La Nacho](https://viva-la-nacho.herokuapp.com/)

![Viva La Nacho Main Image](readme/assets/images/viva-la-nacho.png)

# Contents

* [**Project**](<#project>)
    * [Objective](<#objective>)
    * [Site User Goal](<#site-user-goal>)
    * [Site Owner Goal](<#site-owner-goal>)
    * [**Project Management**](<#project-management>)
        * [GitHub Project Board](<#github-project-board>)
        * [Database Schema](<#database-schema>)
* [**User Experience UX**](<#user-experience-ux>)
    * [Wireframes](<#wireframes>)
    * [User Stories](<#user-stories>)
    * [Site Structure](<#site-structure>)
    * [Colour Scheme](<#colour-scheme>)
    * [Typography](<#typography>)
* [**Features**](<#features>)
    * [**Existing Features**](<#existing-features>)
        * [**Homepage**](<#homepage>)
            * [Navigation](<#navigation>)
            * [Hero](<#hero>)
            * [Intro](<#intro>)
            * [Featured Recipe](<#featured-recipe>)
            * [Latest Recipes List](<#latest-recipes-list>)
            * [Most Popular Recipes List](<#most-popular-recipes-list>)
            * [Footer](<#footer>)
        * [**Authorisation**](<#authorisation>)
            * [Sign Up](<#sign-up>)
            * [Log In](<#log-in>)
            * [Log Out](<#log-out>)
        * [**Full Recipe Details**](<#full-recipe-details>)
            * [Recipe Details](<#recipe-details>)
            * [Like/Unlike Recipe](<#like-/-unlike-recipe>)
            * [Recipe Comments](<#recipe-comments>)
            * [Comment Form](<#comment-form>)
            * [Comment Form Validation](<#comment-form-validation>)
            * [Post Comment Notification](<#post-comment-notification>)
        * [**All Recipes**](<#all-recipes>)
            * [All Recipes List](<#all-recipes-list>)`
            * [Recipe Cards](<#recipe-cards>)
            * [Pagination](<#pagination>)
        * [**My Favourites**](<#my-favourites>)
            * [My Favourites List](<#my-favourites-list>)
            * [Unlike Recipe](<#unlike-recipe>)
            * [Unlike Recipe Notification](<#unlike-recipe-notification>)
            * [No Favourites](<#no-favourites>)
        * [**My Recipes**](<#my-recipes>)
            * [My Recipes List](<#my-recipes-list>)
            * [My Recipe Cards](<#my-recipe-cards>)
            * [Delete Recipe](<#delete-recipe>)
            * [Delete Recipe Notification](<#delete-recipe-notification>)
            * [No Recipes](<#no-recipes>)
        * [**Post A Recipe**](<#post-a-recipe>)
            * [Post Recipe Form](<#post-recipe-form>)
            * [Post Recipe Form Validation](<#post-recipe-form-validation>)
            * [Cancel Post Recipe Form](<#cancel-post-recipe-form>)
            * [Log In To Post Recipe](<#log-in-to-post-recipe>)
            * [Post Recipe Notification](<#post-recipe-notification>)
        * [**Edit Recipe**](<#edit-recipe>)
            * [Edit Recipe Form](<#edit-recipe-form>)
            * [Edit Recipe Form Validation](<#edit-recipe-form-validation>)
            * [Cancel Edit Recipe Form](<#cancel-edit-recipe-form>)
            * [Log In To Edit Recipe](<#log-in-to-edit-recipe>)
            * [Edit Recipe Notification](<#edit-recipe-notification>)
        * [**404 Page**](<#404-page>)
    * [**Future Features**](<#future-features>)
        * [Admin Area](<#admin-area>)
        * [User Profile](<#user-profile>)
        * [User Change Password](<#user-change-password>)
        * [Sign Up Email Confirmation](<#sign-up-email-confirmation>)
        * [Recipe Categories](<#recipe-categories>)
        * [Search Recipes](<#search-recipes>)
* [**Technologies Used**](<#technologies-used>)
    * [Languages](<#languages>)
    * [Frameworks](<#frameworks>)
    * [Software](<#software>)
    * [Libraries](<#libraries>)
* [**Testing**](<#testing>)
    * [**User Story Tests**](<#user-story-tests>)
    * [**Validator Tests**](<#validator-tests>)
        * [W3C (HTML)](<#w3c-html>)
        * [W3C (CSS)](<#w3c-css>)
        * [PEP8 (Python)](<#pep8-python>)
        * [JSHint (JavaScript)](<#jshint-javascript>)
    * [**Input Validation Tests**](<#input-validation-tests>)
        * [Post Recipe Form Tests](<#post-recipe-form-tests>)
        * [Edit Recipe Form Tests](<#edit-recipe-form-tests>)
        * [Comment Form Tests](<#comment-form-tests>)
    * [**Additional Tests**](<#additional-tests>)
        * [Manual Tests](<#manual-tests>)
        * [Automated Tests](<#automated-tests>)
        * [Responsive Tests](<#responsive-tests>)
        * [Browser Tests](<#browser-tests>)
        * [Lighthouse Tests](<#lighthouse-tests>)
        * [Wave Accessibility Tests](<#wave-accessibility-tests>)
    * [**Bugs**](<#bugs>)
        * [Resolved](<#resolved>)
        * [Unresolved](<#unresolved>)
* [**Deployment**](<#deployment>)
    * [**Project Deployment Via Heroku**](<#project-deployment-via-heroku>)
* [**Credits**](<#credits>)
    * [**Content**](<#content>)
    * [**Media**](<#media>)
    * [**Code**](<#code>)
*  [**Acknowledgements**](<#acknowledgements>)

# Project 

## Objective

This project was created as a fourth portfolio project submission for the Full Stack Software Development Higher National Diploma at [Code Institute](https://codeinstitute.net/). Amoungst other assessment criteria, the project had to be built using HTML, CSS, JavaScript, Python and Django and feature full CRUD functionality and user authorisation. The project had to also be planned and designed using agile methodologies. 

As a fan of not just Mexican food, but also food in general, I decided to create a Mexican recipe sharing app as it appealed to my interests, and I believed I would enjoy creating the application. I also believed I would genuinely consider using it personally going forwards, as a personal cookbook to store my own recipes. 

Due in part to a tight timeline for the project, I decided to keep the scope concise and well defined to aid in my goals, objectives and deliverables. I am a firm believer that it's better to do a good job at a few things rather than an average job at a lot of things. With this in mind, I focussed on implimenting an MVP with the core features necessary, in order to provide an attractive experience for the user with limited unnecessary features.

Put in its simplest form, the overall project objective of Viva La Nacho was this - create a full stack online application which allows users to sign up and create, edit and share Mexican recipes and interact with the community. I then refined this objective into epics, user stories and tasks using an agile methodology which provided me with a clear path to achieving my objective.

[Back to top](<#contents>)

## Site User Goal

Users of the Viva La Nacho application could have many goals. They may wish to gather and share knowledge related to Mexican food. They might want to interact and network with other users in the community who have shared interests. They could also want a platform to store their recipes, as well as gather and save new ones in a central location. Or it's possible they just want to browse the recipes casually without signing up. To make the application appealing to a vast audience, I have to try to create an application to cater to all of these potential user goals.

[Back to top](<#contents>)

## Site Owner Goal

As the site owner, the goal is to provide a stable and enjoyable user experience that encourages interaction and participation. The platform should be accessibile, welcoming and appealing to new users. Content should be high quality and well structured. User interactions should be monitored to maintain community standards. 

[Back to top](<#contents>)

## Project Management

### Github Project Board

An agile methodology was used to plan and design the Viva La Nacho application. A large part of this planning was done via the [Viva La Nacho GitHub Project Board](https://github.com/users/Matthew-Hurrell/projects/2). User stories were created on GitHub and added to the board in the todo section. They then moved across the board into in progress when they were being actioned, and then into the done section when they were completed. This helped greatly in tracking progress and organising and allocating work.

![Viva La Nacho Project Board](readme/assets/images/viva-la-nacho-project-board.png)

[Back to top](<#contents>)

### Database Schema

Database schemas were drawn up using [App Diagrams.net](https://app.diagrams.net/). The schemas were used to plan the database models and fields. It also helps to display the relationships between the models and how they interact. Viva La Nacho consists of three models - Recipe, Comment and User.

![Viva La Nacho Database Schemas](readme/assets/images/viva-la-nacho-database-schemas.png)

[Back to top](<#contents>)

# User Experience UX

## Wireframes

Wireframes were created using [Balsamiq](https://balsamiq.com/) to plan content flow and styling for Viva La Nacho. Some differences can be seen between the original wireframes and the finished product, and this is due to design choices made during the creative process.

### Home Page 
![Home Page Wireframe](readme/assets/images/home-page-wireframe.png)

### Recipe Details
![Recipe Details Wireframe](readme/assets/images/recipe-details-wireframe.png)

### Create Account
![Create Account Wireframe](readme/assets/images/create-account-wireframe.png)

### Log In
![Log In Wireframe](readme/assets/images/log-in-wireframe.png)

### Log Out
![Log Out Wireframe](readme/assets/images/log-out-wireframe.png)

### My Recipes
![My Recipes Wireframe](readme/assets/images/my-recipes-wireframe.png)

### My Favourites
![My Favourites Wireframe](readme/assets/images/my-favourites-wireframe.png)

### Post A Recipe
![Post A Recipe Wireframe](readme/assets/images/post-a-recipe-wireframe.png)

### Edit Recipe
![Edit Recipe Wireframe](readme/assets/images/edit-recipe-wireframe.png)

[Back to top](<#contents>)

## User Stories

In terms of project management, user stories are an integral part of the software development creative process. Viva La Nacho consists of 43 user stories, each broken down into acceptance criteria and tasks. Each user story is also given a story points number relating to time/difficulty of the tasks and then is assigned a priority label of either 'must have', 'should have', 'could have' or 'wont have' to help organise work through iterations. User stories were created from 'Epics' which are larger over-arching features/concepts which are then refined down into smaller individual parts. Completed user stories were marked as closed. 

A full list of user stories can be found in the [Viva La Nacho GitHub Project Board](https://github.com/users/Matthew-Hurrell/projects/2).

![Like A Recipe User Story](readme/assets/images/user-story-like-a-recipe.png)

[Back to top](<#contents>)

## Site Structure 

The Viva La Nacho app features a simple and user friendly site structure that users will be quite familiar with. However, some content is hidden / restricted to users who are not logged in. The main pages / templates of Viva La Nacho include - the home page, recipe full details, my favourites, my recipes, post recipe form, edit recipe form, all recipes and the sign up, log in and log out templates. Site users can freely and easily browse the various pages using the site navigation bar which is visible at the top and bottom of each page. The nav bar options automatically change depending on whether a user is signed in or not to allow for easy and intuitive site navigation.

![Header Nav Logged In](readme/assets/images/nav-bar-logged-in.png)

![Header Nav Not Logged In](readme/assets/images/nav-bar-not-logged-in.png)

![Footer Nav Logged In](readme/assets/images/footer-nav-logged-in.png)

![Header Nav Not Logged In](readme/assets/images/footer-nav-not-logged-in.png)


[Back to top](<#contents>)

## Colour Scheme

The Viva La Nacho colour scheme was inspired by the [2016 WOW Fiesta Color Palette](https://www.color-hex.com/color-palette/17808) from [Color Hex](https://www.color-hex.com/). However, the actual colours used were from the selection of [Tailwind Colours](https://tailwindcss.com/docs/customizing-colors) from the [Tailwind Utility Framework](https://tailwindcss.com/) used to create the front-end of the site.

![Viva La Nacho Colour Palette](readme/assets/images/viva-la-nacho-colour-palette.png)

[Back to top](<#contents>)

## Typography 

Viva La Nacho uses [Google Fonts](https://fonts.google.com/) for the site typography. The specific fonts are [Port Lligat Slab](https://fonts.google.com/specimen/Port+Lligat+Slab?query=Port+Lligat+Slab) and [ASAP](https://fonts.google.com/specimen/Asap?query=asap). Port Lligat Slab is a display typeface. It is clear but defined with a clear Mexican inspired twist. It was chosen to add some character to the titles and links. It is a playful font and matches the theme well. Asap is a contemporary sans-serif font. It's modern looking and rounded, and it was used for the main bodies of text to make them easier to read. 

![Port Lligat Slab Typeface](readme/assets/images/port-lligat-slab.png)

![Asap Font](readme/assets/images/asap-font.png)

[Back to top](<#contents>)

# Features

## Existing Features

### Homepage

[Back to top](<#contents>)

#### Navigation

[Back to top](<#contents>)

#### Hero

[Back to top](<#contents>)

#### Intro

[Back to top](<#contents>)

#### Featured Recipe

[Back to top](<#contents>)

#### Latest Recipes List

[Back to top](<#contents>)

#### Most Popular Recipes List

[Back to top](<#contents>)

#### Footer

[Back to top](<#contents>)

### Authorisation

#### Sign Up

[Back to top](<#contents>)

#### Log In

[Back to top](<#contents>)

#### Log Out

[Back to top](<#contents>)

### Full Recipe Details

#### Recipe Details

[Back to top](<#contents>)

#### Like / Unlike Recipe

[Back to top](<#contents>)

#### Recipe Comments

[Back to top](<#contents>)

#### Comment Form

[Back to top](<#contents>)

#### Comment Form Validation

[Back to top](<#contents>)

#### Post Comment Notification

[Back to top](<#contents>)

### All Recipes

#### All Recipes List

[Back to top](<#contents>)

#### Recipe Cards

[Back to top](<#contents>)

#### Pagination

[Back to top](<#contents>)

### My Favourites

#### My Favourites List

[Back to top](<#contents>)

#### Unlike Recipe

[Back to top](<#contents>)

#### Unlike Recipe Notification

[Back to top](<#contents>)

#### No Favourites

[Back to top](<#contents>)

### My Recipes

#### My Recipes List

[Back to top](<#contents>)

#### My Recipe Cards

[Back to top](<#contents>)

#### Delete Recipe

[Back to top](<#contents>)

#### Delete Recipe Notification

[Back to top](<#contents>)

#### No Recipes

[Back to top](<#contents>)

### Post A Recipe

#### Post Recipe Form

[Back to top](<#contents>)

#### Post Recipe Form Validation

[Back to top](<#contents>)

#### Cancel Post Recipe Form

[Back to top](<#contents>)

#### Log In To Post Recipe

[Back to top](<#contents>)

#### Post Recipe Notification

[Back to top](<#contents>)

### Edit Recipe

#### Edit Recipe Form

[Back to top](<#contents>)

#### Edit Recipe Form Validation

[Back to top](<#contents>)

#### Cancel Edit Recipe Form

[Back to top](<#contents>)

#### Log In To Edit Recipe

[Back to top](<#contents>)

#### Edit Recipe Notification

[Back to top](<#contents>)

### 404 Page

[Back to top](<#contents>)

## Future Features

### Admin Area

[Back to top](<#contents>)

### User Profile

[Back to top](<#contents>)

### User Change Password

[Back to top](<#contents>)

### Sign Up Email Confirmation

[Back to top](<#contents>)

### Recipe Categories

[Back to top](<#contents>)

### Search Recipes

[Back to top](<#contents>)

# Technologies Used

## Languages

[Back to top](<#contents>)

## Frameworks

[Back to top](<#contents>)

## Software

[Back to top](<#contents>)

## Libraries

[Back to top](<#contents>)

# Testing

## User Story Tests

[Back to top](<#contents>)

## Validator Tests

### W3C (HTML)

[Back to top](<#contents>)

### W3C (CSS)

[Back to top](<#contents>)

### PEP8 (PYTHON)

[Back to top](<#contents>)

### JSHint (JavaScript)

[Back to top](<#contents>)

## Input Validation Tests

### Post Recipe Form Tests

[Back to top](<#contents>)

### Edit Recipe Form Tests

[Back to top](<#contents>)

### Comment Form Tests

[Back to top](<#contents>)

## Additional Tests

### Manual Tests

[Back to top](<#contents>)

### Automated Tests

[Back to top](<#contents>)

### Responsive Tests

[Back to top](<#contents>)

### Browser Tests

[Back to top](<#contents>)

### Lighthouse Tests

[Back to top](<#contents>)

### Wave Accessibility Tests

[Back to top](<#contents>)

## Bugs

### Resolved 

[Back to top](<#contents>)

### Unresolved

[Back to top](<#contents>)

# Deployment

## Project Deployment via Heroku

This is a guide on how to deploy a project via [Heroku](https://www.heroku.com).

[Back to top](<#contents>)

# Credits

## Content

[Back to top](<#contents>)

## Media

[Back to top](<#contents>)

## Code 

[Back to top](<#contents>)

# Acknowledgements

[Back to top](<#contents>)