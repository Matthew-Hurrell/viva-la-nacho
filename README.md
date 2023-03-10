# **Viva La Nacho**

Viva La Nacho is a full stack web application that gives users a platform to view and share Mexican recipes. The intention of the site is to provide a simple, intuitive, visually appealing and user-friendly platform for users to share Mexican-inspired recipes and interact with the community. The intended target audience is anyone with an interest in cooking and Mexican food. The target audience will mostly span across men and women from young adults to older generations. 

The application impliments user authorisation and full CRUD functionality, allowing users to create, update, read and delete recipes stored in a relational database management system. Users can also like recipes to save them to their favourites list and interact with other users via recipe comments. 

The site also features a back-end admin dashboard that allows an administrator to review and approve user comments, as well as monitor and edit recipes. 

Link to the live site - [Viva La Nacho](https://viva-la-nacho.herokuapp.com/)

![Viva La Nacho Main Image](readme/assets/images/viva-la-nacho-responsive.png)

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
            * [All Recipes List](<#all-recipes-list>)
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

This project was created as a fourth portfolio project submission for [Code Institutes](https://codeinstitute.net/) Higher National Diploma in Full Stack Software Development. Amongst other assessment criteria, this project had to be built using HTML, CSS, JavaScript, Python and the Django framework, and feature full CRUD functionality and user authorisation. The project also had to be planned and designed using agile methodologies. 

As a fan of not just Mexican food, but also food in general, I decided to create a Mexican recipe sharing app as it appealed to my interests, and I believed I would enjoy creating the application. I also believed I would genuinely consider using it personally going forwards, as a personal cookbook to store my own recipes. 

Due in part to a tight timeline for the project, I decided to keep the scope concise and well-defined to aid in my goals, objectives and deliverables. I am a firm believer that it's better to do a good job at a few things rather than an average job at a lot of things. With this in mind, I focussed on implementing an MVP with the core features necessary, in order to provide an attractive experience for the user with limited unnecessary features.

Put in its simplest form, my overall objective with the Viva La Nacho project was this - to construct a full-stack online application that allows users to sign up and create, edit and share Mexican recipes and interact with the community. I then refined this objective into epics, user stories and then tasks using an agile methodology which provided me with a clear path to achieving my objective.

[Back to top](<#contents>)

## Site User Goal

Users of the Viva La Nacho application could have many goals. They may wish to gather and share knowledge related to Mexican food. They may want to interact and network with other users in the community who have shared interests. They may also want a platform to store their recipes, as well as gather and save new ones in a central location. Or it's possible they may just want to browse the recipes casually without signing up. To make the application appealing to a vast audience with differing goals, I have to try to create an application to cater to all of these potential user goals.

[Back to top](<#contents>)

## Site Owner Goal

As the site owner, the goal is to provide a stable and enjoyable user experience that encourages interaction and participation. The platform should be accessible, welcoming and appealing to new users. Content should be of a high quality and well structured. User interactions should be monitored to maintain community standards. 

[Back to top](<#contents>)

## Project Management

### GitHub Project Board

An agile methodology was used to structure the planning and design of the Viva La Nacho application. A large part of this planning was done via the [Viva La Nacho GitHub Project Board](https://github.com/users/Matthew-Hurrell/projects/2). User stories were created on GitHub and added to the board in the to-do section. They then moved across the board into in-progress when they were being actioned, and then into the done section when they were completed. This helped greatly in tracking progress and organising and allocating work.

![Viva La Nacho Project Board](readme/assets/images/viva-la-nacho-project-board.png)

[Back to top](<#contents>)

### Database Schema

Database schemas were drawn up using [App Diagrams.net](https://app.diagrams.net/). The schemas were used to plan the database models and fields. It also helped in displaying the relationships between the models and how they interact. Viva La Nacho consists of three models - Recipe, Comment and User.

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

In terms of project management, user stories are an integral part of the software development creative process. Viva La Nacho consists of 43 user stories, each broken down into acceptance criteria and tasks. Each user story was given a story points number relating to the time/difficulty of the tasks in relation to each other, and then was assigned a priority label of either 'must have', 'should have', 'could have' or 'won't have' to help organise work through iterations. User stories were created from 'Epics', which are larger over-arching features/concepts, then refined into smaller individual parts. Completed user stories were marked as closed. User stories were sorted into weekly iterations that were used to structure and allocate the work each week. Each iteration was planned to not include more than 60% must-have user stories.

A full list of user stories can be found in the [Viva La Nacho GitHub Project Board](https://github.com/users/Matthew-Hurrell/projects/2).

![Like A Recipe User Story](readme/assets/images/user-story-like-a-recipe.png)

![User Story Iteration](readme/assets/images/user-story-iteration.png)

[Back to top](<#contents>)

## Site Structure 

The Viva La Nacho app features a simple and user friendly site structure that users will be quite familiar with. However, some content is hidden / restricted to users who are not logged in. The main pages / templates of Viva La Nacho include - the home page, recipe full details, my favourites, my recipes, post recipe form, edit recipe form, all recipes and the signup, login and log out templates. Site users can freely and easily browse the various pages using the site navigation bar which is visible at the top and bottom of each page. The nav bar options automatically change depending on whether a user is signed in or not to allow for easy and intuitive site navigation.

![Header Nav Logged In](readme/assets/images/nav-bar-logged-in.png)

![Header Nav Not Logged In](readme/assets/images/nav-bar-not-logged-in.png)

![Footer Nav Logged In](readme/assets/images/footer-nav-logged-in.png)

![Footer Nav Not Logged In](readme/assets/images/footer-nav-not-logged-in.png)

[Back to top](<#contents>)

## Colour Scheme

The Viva La Nacho colour scheme was inspired by the [2016 WOW Fiesta Color Palette](https://www.color-hex.com/color-palette/17808) from [Color Hex](https://www.color-hex.com/). However, the actual colours used were from the selection of [Tailwind Colours](https://tailwindcss.com/docs/customizing-colors) from the [Tailwind Utility Framework](https://tailwindcss.com/) used to create the front-end of the site.

![Viva La Nacho Colour Palette](readme/assets/images/viva-la-nacho-colour-palette.png)

[Back to top](<#contents>)

## Typography 

Viva La Nacho uses [Google Fonts](https://fonts.google.com/) for the site typography. The specific fonts are [Port Lligat Slab](https://fonts.google.com/specimen/Port+Lligat+Slab?query=Port+Lligat+Slab) and [ASAP](https://fonts.google.com/specimen/Asap?query=asap). Port Lligat Slab is a display typeface. It is a playful font with clear but defined with a clear Mexican-inspired twist. It was chosen to add some character to the titles and links. Asap is a contemporary sans-serif font. It is modern looking and rounded, and it was used for the main bodies of text to make them easier to read. 

![Port Lligat Slab Typeface](readme/assets/images/port-lligat-slab.png)

![Asap Font](readme/assets/images/asap-font.png)

[Back to top](<#contents>)

# Features

## Existing Features

### Homepage

The homepage is the first page of the site that a user will see when they navigate to the [Viva La Nacho URL](https://viva-la-nacho.herokuapp.com/). It's designed to be eye catching to users and to quickly summarise the intention of the site. It is also a central location for all users to view recipes. 

![Viva La Nacho Main Image](readme/assets/images/viva-la-nacho.png)

[Back to top](<#contents>)

#### Navigation

Site navigation is present at all times on every page of the site in the form of footer and header nav bars. These navigational elements change depending on whether a user is logged in or not. Non logged in users only have access to the home page, recipe detail pages, view all recipe page and the login and signup page. These elements are also fully responsive and the header collapses to become a mobile menu on small screen sizes. The header nav features the site logo which is also a link back to the home page. It also features a post a recipe button which is distinctly different from the other nav menu items. This is to draw the user's eye and encourage them to sign up so that they can use this feature. All nav menu items feature a scale and underline hover effect. Navigation items are active on the current page and the underline remains in place as a visual aid to show the user where they are.

![Header Nav Logged In](readme/assets/images/nav-bar-logged-in.png)

![Header Nav Not Logged In](readme/assets/images/nav-bar-not-logged-in.png)

![Mobile Nav Menu](readme/assets/images/mobile-nav-menu.png)

![Footer Nav Logged In](readme/assets/images/footer-nav-logged-in.png)

![Footer Nav Not Logged In](readme/assets/images/footer-nav-not-logged-in.png)

[Back to top](<#contents>)

#### Hero

The homepage hero section is the large eye-catching section that is just beneath the navigation bar. The hero is only displayed on the homepage. It is used to catch the users attention, and to clearly showcase the general topic of the site. It features a large, colourful full screen background image and a centralised text box with the site title and tagline. The hero section also features the Mexican hat logo motif to reinforce the brand image.

![Hero Homepage](readme/assets/images/hero-homepage.png)

[Back to top](<#contents>)

#### Intro

The homepage intro section is a brief introductory text paragraph that explains the purpose of the site and how to use it to new users. This section also features a divider above and below to clearly define and separate the sections. These stylised dividers are used frequently throughout the site and help to solidify the Mexican theme. A lighter shade of the green theme colour is used as a background colour.

![Intro Homepage](readme/assets/images/homepage-intro.png)

[Back to top](<#contents>)

#### Featured Recipe

The featured recipe is the first recipe shown on the site homepage. This singular recipe has its own section and fills the entire width of the screen. The featured recipe can only be assigned by a site administrator. The general idea was that this would be cycled weekly/monthly for a new featured recipe. Unlike the other recipes on the page, the featured recipe displays the whole gallery of recipe images. It also displays information such as prep time, cooking time, difficulty, serving, the excerpt and the author username. There is a button link that takes the user to the full recipe details. There is also a like count displayed as a tag over the large recipe image. The background of the section is a colourful mexican wall full of torn posters but a gradient is used to fade the image so it doesn't distract from the recipe content.

![Featured Recipe](readme/assets/images/featured-recipe.png)

[Back to top](<#contents>)

#### Latest Recipes List

The latest recipe list is a dynamic list of the latest recipes that have been uploaded to the site. When a new recipe is published it will appear at the top of the list. Draft recipes do not appear in this list. Each recipe is displayed as a card, and each card has an image, like count tag, title, author, excerpt and a link to the full recipe page. The list displays a maximum of nine cards to avoid clutter. At the end of the section, there is also a button link to the all recipes page. This section is fully responsive, and cards stack on top of each other on smaller screens. 

![Latest Recipes](readme/assets/images/latest-recipes-1.png)

![Latest Recipes](readme/assets/images/latest-recipes-2.png)

[Back to top](<#contents>)

#### Most Popular Recipes List

The most popular recipes list is another list styled similarly to the previous list. This list is ordered by recipes with the most likes. The list has a max of nine just like the previous list. At the bottom of this section is another view all recipes button link which takes the user to the all recipes page.

![Most Popular Recipes](readme/assets/images/most-popular-recipes-1.png)

![Most Popular Recipes](readme/assets/images/most-popular-recipes-2.png)

[Back to top](<#contents>)

#### Footer

The Viva La Nacho footer is present on every page of the site. It features the same navigation menu as the header nav but styled differently. A deep green background colour is used, which contrasts well with the light background colours of the inner sections. Social media icon links feature coloured hover effects which match their individual social media colour palettes. There is also a repetition of the Viva La Nacho site name and tagline with the Mexican hat motif to finish the page. This footer is fully responsive, and navigation items stack vertically on smaller screens.

![Footer](readme/assets/images/viva-la-nacho-footer.png)

![Footer Responsive](readme/assets/images/viva-la-nacho-footer-responsive.png)

[Back to top](<#contents>)

### Authorisation

#### Sign Up

A user can navigate to the sign up page via the site navigation bars if they are not logged in. The Viva La Nacho sign up page is a template from the [Django Allauth Package](https://django-allauth.readthedocs.io/en/latest/installation.html). Allauth provides the basic functionality for the user authorisation used in Viva La Nacho. However, the basic allauth templates have been heavily customised and styled to match the site design. The sign up page features a title and a sign up form with user input fields. The form also features javascript validation to alert the user if the fields are incorrectly filled out. The page features another Mexican food-themed background image. The background image is filtered to lighten the colours and to prevent it from being too distracting to the user. Once a user submits the form correctly they are redirected back to the homepage as a logged-in user.

![Sign Up](readme/assets/images/sign-up.png)

[Back to top](<#contents>)

#### Log In

A user can navigate to the log in page via the site navigation bars if they are not already logged in. The styling of the log in page is very similar to the rest of the user authorisation pages. The colour scheme and background image are consistent, but the form and page heading are different. Once the log in form is submitted correctly the user is redirected to the homepage as a logged-in user.

![Log In](readme/assets/images/log-in.png)

[Back to top](<#contents>)

#### Log Out

A user can navigate to the log-out page via the site navigation bars if they are logged in. They are prompted on this page to confirm they wish to log out. Upon confirmation, the user is logged out and redirected to the homepage. If the user instead clicks the 'I'm still hungry' button they are just redirected back to the homepage but not logged out. The styling and background image is consistent with the other authorisation pages for coherence. 

![Log Out](readme/assets/images/log-out.png)

[Back to top](<#contents>)

### Full Recipe Details

The full recipe details page is a template used to display the full information of a recipe. Each published recipe has a recipe details page. Theses pages are available for all users to view, including non-logged-in users. The main purpose of the page is to display the full recipe method and ingredients. Users will generally navigate to a full recipe page by clicking the view recipe button on the recipe card either on the home page or the all recipes page. As the user has now shown a specific interest in the recipe, all the information about the recipe is displayed here. 

![Recipe Details](readme/assets/images/recipe-details-1.png)

#### Recipe Details

The first section of the recipe page features the recipe image. When there is more than one image, a gallery of images is displayed underneath the main image. Basic recipe details and information is displayed in the top section, such as cooking, prep time and allergens. There is also an icon on the image which allows the user to like the recipe. In the middle section there are two columns of text displaying the recipe ingredients and method. These fields are both summernote fields so they accept fully formatted and styled user text. Each section on the recipe details page is separated by a divider to clearly illustrate the different segments. 

![Recipe Details](readme/assets/images/recipe-details-2.png)

[Back to top](<#contents>)

#### Like / Unlike Recipe

A user can like and unlike a recipe from the recipes specific recipe page. Each recipe features a heart icon in the top right corner of the main recipe image that can be clicked to like a recipe. It can also be clicked again to unlike a recipe. When a recipe is liked by a user, the icon changes to a heart with a minus icon. Unregistered users cannot like a recipe as they do not have a username. A user who is not logged in only sees a heart icon with a minus symbol to suggest it is blocked. Clicking the icon is disabled for an unregistered user and has no effect. 

![Like Recipe](readme/assets/images/like-recipe.png)

![Unlike Recipe](readme/assets/images/unlike-recipe.png)

[Back to top](<#contents>)

#### Recipe Comments

At the bottom of each recipe details page there is a comments section for users to post comments. Logged in users can use the comment form to post a comment to that particular recipe. Comments need to be approved by an admin before they appear on the site. Comments are listed in the admin area as unapproved, and there is an action to approve comments in the admin actions menu. When comments are approved by the admin they immediately go live on the site and appear beneath the recipe. Comments are listed from the most recent at the top to the oldest at the bottom. The username of the comment author is displayed as well as the date and the body of the comment. 

![Recipe Comments](readme/assets/images/recipe-comments.png)

[Back to top](<#contents>)

#### Comment Form

The recipe comment form is what the user uses to post a comment on a recipe. This comment form is only visible to logged in users, as a username is required for successful submission. The comment form comprises of one text body field for the comment and a submit button. The author is assigned automatically as well as the created-on date.

![Comment Form](readme/assets/images/comment-form.png)

![Comment Form](readme/assets/images/log-in-to-post-comment.png)

[Back to top](<#contents>)

#### Comment Form Validation

Javascript is used to validate the comment form. The form body field is checked for empty space as well as whitespace. Javascript prevents the form from being submitted until the comment field passes the test. If the test fails, a pop-up notification appears on the user's screen to advise them about the failure. The user can then rectify their mistake and submit the form again. When the comment form is filled out correctly the form submits successfully and the page is refreshed.

![Comment Form Validation](readme/assets/images/comment-validation.png)

[Back to top](<#contents>)

#### Post Comment Notification

Upon the successful submission of the comment form, the page will refresh and a notification will appear at the top of the page. This notification advises the user that their comment has been successfully posted. The notification can be removed from view by clicking the x icon. If not manually hidden, the notification is automatically removed from view after three seconds. The form is also hidden from view in the comment section, and this is instead replaced by a short paragraph of text thanking the user for posting a comment. The text also advises the user that the comment will be visible after it has been approved. 

![Comment Notification](readme/assets/images/comment-notification.png)

![Comment Success](readme/assets/images/comment-success.png)

[Back to top](<#contents>)

### All Recipes

The all recipe page is a template that displays all the published recipes on the Viva La Nacho site. It was created later in production as there needed to be a single place for users to browse the full selection of recipes. This template has a maximum limit of nine recipes per page but features pagination to allow users to view more recipes. The page is styled very similarly to other pages and also includes the header nav and footer sections. 

![All Recipes](readme/assets/images/all-recipes-page.png)

![All Recipes](readme/assets/images/all-recipes-page-2.png)

#### All Recipes List

The recipes on the all recipes page are arranged as cards in columns of three on larger screens. The cards are responsive and stack on top of each other on smaller screens. The recipes are listed in chronological order.

![All Recipes List](readme/assets/images/all-recipes-list.png)

[Back to top](<#contents>)

#### Recipe Cards

Each recipe card includes a recipe image, recipe like count tag, title, author, excerpt and a button link to the full recipe. This makes it easy for a user to navigate to a recipe they are interested in. They can also see the like count to see if the recipe is popular. Cards are kept clean and are styled consistently with other recipe cards across the site.

![All Recipes Card](readme/assets/images/all-recipes-card.png)

[Back to top](<#contents>)

#### Pagination

A maximum of nine cards are visible on the all recipes page before page pagination occurs. The pagination menu is only visible if more than nine recipes exist on the Viva La Nacho site. Pagination is necessary to reduce load times, and to keep the page from being very large if a lot of recipes are published on the site. The user can click the next, previous, last or first buttons to navigate between the pages of recipes.

![All Recipes Pagination](readme/assets/images/all-recipes-pagination.png)

![All Recipes Pagination](readme/assets/images/all-recipes-pagination-2.png)

[Back to top](<#contents>)

### My Favourites

The my favourites page is a template which is only accessible via the navigation menu to users who are logged in. The purpose of the my favourites page is to display a list of the recipes on the site which have been liked by the user. This is so the user can use the like recipe functionality as a way of storing recipes to view at a later date, almost like putting a bookmark in a digital cookbook. Users can use this feature to keep their favourite recipes in one easy location without having to search for them manually on the all recipes page or home page.

![My Favourites](readme/assets/images/my-favourites.png)

#### My Favourites List

The my favourites recipe list displays published recipes that have been liked by the user. Recipes are displayed in cards which are styled consistently with recipe cards found throughout the site. The only difference is that they also feature a red cross icon button which is displayed on the top left corner of the recipe image.

![My Favourites List](readme/assets/images/my-favourites-list.png)

[Back to top](<#contents>)

#### Unlike Recipe

A user is able to quickly and easily unlike a recipe to remove it from the list on the my favourites page. The unlike button icon is on the top left corner of each recipe card. When a user clicks the unlike icon the content below the image is hidden and replace with a notification prompting the user to confirm their decision to unlike the recipe. This confirmation helps to avoid a user accidentally unliking a recipe. The user then has to confirm their decision by clicking the unlike button. Alternatively the user can click the cancel button to return the content to the recipe card and abort the process. Clicking the unlike button will remove the user like from the recipe and refresh the page with the recipe removed from the list.

![My Favourites Unlike Recipe](readme/assets/images/my-favourites-unlike-recipe.png)

[Back to top](<#contents>)

#### Unlike Recipe Notification

When a user unlikes a recipe from the my favourites page and the page is refreshed, and a notification is displayed to the user at the top of the page confirming that the recipe has been unliked. This can be hidden by the user by clicking the x icon button. If the notification is not manually exited it will automatically time out and be removed from view after three seconds. 

![My Favourites Unlike Notification](readme/assets/images/recipe-unliked-notification.png)

[Back to top](<#contents>)

#### No Favourites

If a user navigates to the my favourites page but has no liked recipes, a content box appears that informs the user that they have no liked recipes. It also explains the purpose of the my favourites section, incase the user is unaware. There is also a button link in the box which navigates the user back to the homepage.

![No Favourites Notification](readme/assets/images/no-favourites.png)

[Back to top](<#contents>)

### My Recipes

The purpose of the my recipes page is to display a list of the recipes that the current user has posted and is the author of. This list contains published and unpublished recipes and is only visible to the current logged-in user. This page is not present in the navigation bars to non logged in users and can't be navigated to using the site navigation. The user can use the my recipes page to keep track of their recipes easily in one place. They can freely edit and delete any of their recipes from this page.

![My Recipes](readme/assets/images/my-recipes.png)

#### My Recipes List

The my recipes list displays a list of recipes that have been created by the user. It displays both published and unpublished user recipes. Recipes are again displayed in cards which are similarly styled to the recipe cards throughout the site. Cards are organised in columns of three on large screens and stack responsively to one column on smaller screens.

![My Recipes List](readme/assets/images/my-recipes-list.png)

[Back to top](<#contents>)

#### My Recipe Cards

Recipe cards displayed on the my recipes page feature similar content to those seen throughout the rest of the site. They do however also include a drafted / published tag which displays to the user whether the recipe is drafted or not. They also contain edit, delete and view recipe buttons. Recipes which are drafted and unpublished do not contain the view recipe button as they do not have a full recipe template page until they are published.

![My Recipes Card](readme/assets/images/my-recipe-card.png)

[Back to top](<#contents>)

#### Delete Recipe

A user can delete their recipe easily from the my recipe page. If a user clicks the delete button on a recipe card the card content is hidden and a delete confirmation is displayed seeking confirmation from the user for recipe deletion. The user is also warned that the process cannot be undone. The user then has the option to cancel the delete by clicking the cancel button, or to confirm recipe deletion by clicking the delete button. The delete button is purposefully coloured red for warning. If the user clicks the cancel button the card content is returned to normal. If the user clicks the delete button the receipe is deleted from the database and the page is refreshed showing the recipe removed from the list.

![My Recipes Delete](readme/assets/images/my-recipes-delete.png)

[Back to top](<#contents>)

#### Delete Recipe Notification

If a user confirms the deletion of a recipe, a notification is displayed to the user at the top of the page on refresh. This notification confirms the deletion of the recipe. The user can hide this notification by clicking the x icon. If the notification isn't manually closed, the notification is automatically timed out and removed from view after three seconds. 

![Recipe Deleted Notification](readme/assets/images/recipe-deleted-notification.png)

[Back to top](<#contents>)

#### No Recipes

If a user navigates to the my recipes page but doesn't have any recipes, a box is displayed in the centre of the screen to advise the user that they have no recipes. They are encouraged to post their first recipe and given a button link to the post a recipe form. There is also a button link to return home if the user doesn't want to post a recipe.

![No Recipes](readme/assets/images/no-recipes.png)

[Back to top](<#contents>)

### Post A Recipe

The post a recipe page template is a page which features a recipe form to enable users to submit a recipe to the Viva La Nacho site. The page is viewable by unauthenticated users but the form is hidden unless a user is logged in. The page features similar styling to the rest of the site for consistency, and the header and footer nav menus are present for easy user navigation. 

![Post A Recipe Page](readme/assets/images/post-a-recipe-page.png)

![Post A Recipe Page](readme/assets/images/post-a-recipe-page-2.png)

#### Post Recipe Form

The recipe form is the main element of the post a recipe page. The form is contained in a centralised box and features a title, input fields and username display, as well as a submit button and cancel button. Form fields include text boxes, multiple checkboxes, number select fields, dropdown selects, image upload fields and WYSIWYG summernote fields. Required fields are marked with a red asterix. The form is fully responsive and the fields stack and become full screen on smaller screen sizes. There are a lot of fields required for a recipe post, so the fields are spaced out and organised to avoid confusion and clutter. 

![Recipe Form](readme/assets/images/recipe-form.png)

![Recipe Form](readme/assets/images/recipe-form-2.png)

[Back to top](<#contents>)

#### Post Recipe Form Validation

The recipe form user input is validated using javascript. A javascript event listener is used on the submit button to check all of the input fields for incorrect input. If any of the fields fail the tests, the form is prevented from being submitted using the javascript prevent default function. A pop-up notification is then displayed to the user that provides details of the field that failed and the error that occurred. The user then has the opportunity to rectify the error and submit the form again. The form will only successfully submit to the database when all the fields pass the tests. This validation helps to prevent failed database submissions. Tests include checking for whitespace and also empty fields. There are also tests for the number fields to check that the user value isn't above a certain value. The summernote fields were slightly harder to validate as empty user input could still show HTML tags, which would pass the javascript test even with no user input. So to effectively validate these fields the strip HTML javascript function was created to remove HTML tags from the fields before testing. Checkboxes were also tested for any checked checkboxes by using the :checked selector and the javascript length function to check that the length of checked checkboxes was over 1. 

![Recipe Form Validation](readme/assets/images/post-recipe-validation.png)

[Back to top](<#contents>)

#### Cancel Post Recipe Form

If a user clicks the cancel button on the post a recipe form at any point, the form content is hidden and a box containing a notification is displayed. The purpose of this notification is to get the user to confirm their choice to cancel the form. It is also explained that any form progress will be lost. If the user then clicks the home button they are redirected to the home page and the form progress is lost. If the user clicks the back button the box is hidden and the form is displayed with the current user input field values returned as previous. This process is to ensure that a user doesn't accidentally or unintentionally lose their form progress by navigating away from the page. This would be a bad user experience. 

![Cancel Recipe Form](readme/assets/images/cancel-recipe-form.png)

[Back to top](<#contents>)

#### Log In To Post Recipe

The post a recipe form page is available to both authorised and non-authorised users. The button link to the page is available on the main nav bar for all users. The reason this button is still visible to non logged in users is it can be used as an incentive to encourage users to sign up. If site users aren't aware they can post their own recipes they may not decide to sign up for an account. This is an intentional design choice to boost user sign ups. However, non authorised users will not see the recipe form if they navigate to the post a recipe page. Instead they will be presented with a centralised content box which contains some text and button links. The notification advises the user that they need to be logged in to post a recipe. The user is then presented with three button links - one to the log in page, one to the sign up page and one for the home page. The user can then decide which option they would prefer. The log in and sign up page button links are deliberately kept brightly coloured to further encourage user sign ups and interaction. 

![Non Authorised Post Recipe](readme/assets/images/non-logged-in-post-recipe.png)

[Back to top](<#contents>)

#### Post Recipe Notification

When a user submits a recipe successfully, the post a recipe page is refreshed and the form is hidden from view. A content box notification is displayed thanking the user for submitting their recipe. The box contains two button links - one to post another recipe, which refreshes the page and displays the recipe form again, and a home button which returns the user back to the home page. This process makes it easier for a user to post multiple recipes, as they can be returned back to the recipe form with just one click. 

![Recipe Submission Confirmation](readme/assets/images/recipe-submission-confirmation.png)

[Back to top](<#contents>)

### Edit Recipe

The edit recipe page is available to authorised users. The edit recipe page can be navigated to via the my recipes section. If a user has posted any recipes, the recipes will be available in the list on the my recipes section. Each of these recipes will feature an edit recipe button. When the edit recipe button is clicked the user is navigated to the edit recipe page. The page styling and content is exactly the same as the post a recipe page, including the recipe form. The only difference is the recipe form is pre-filled out with the content from the specific instance of the recipe post. The user can then use this form to edit the content of their recipe post and submit the amendments to overwrite the recipe content.

![Edit Recipe Page](readme/assets/images/edit-recipe-page.png)

![Edit Recipe Page](readme/assets/images/edit-recipe-page-2.png)

#### Edit Recipe Form

As previously mentioned, the edit recipe form fields are pre filled out with content from the specific recipe instance. These fields are the same fields that are present in the post a recipe form and they are styled exactly the same, so the user should be familiar with the layout from when they first submitted the recipe. All recipe content fields can be freely edited by the user. The user can also choose to draft or publish the recipe from this form. The form also contains a submit and cancel button.

![Edit Recipe Form](readme/assets/images/edit-recipe-form.png)

![Edit Recipe Form](readme/assets/images/edit-recipe-form-2.png)

[Back to top](<#contents>)

#### Edit Recipe Form Validation

The edit recipe form features exactly the same validation as the post recipe form, as the fields are identical. The original code was refactored to change the form variable to include the edit recipe form. It is important to still validate the edit recipe form, as although the user has already submitted the recipe and it passed the tests on the first submission, if the fields are edited and content is removed and it is now not valid, the form is likely to fail when it is submitted to the database again. This is why the edit recipe form is still validated with javascript. The fields are all tested individually and if a test fails, the form is prevented from submitting, and the user is presented with a pop-up notification that provides the user information on which field failed and why. When all the fields pass the tests, the form is submitted to the database and the page is refreshed.

![Edit Recipe Form Validation](readme/assets/images/edit-recipe-form-validation.png)

[Back to top](<#contents>)

#### Cancel Edit Recipe Form

If a user clicks the cancel button on the edit recipe form, the form is removed from view and a centralised content box is displayed to the user prompting them to confirm their decision to cancel the form submission. The notification is identical to the one found on the post recipe form. It is also explained to the user that they will lose their form progress if they confirm the cancellation. The user is presented with two button links - one takes the user to the my recipes page, and one that returns the user back to the form section. If a user clicks the cancel button, the notification is hidden and the form is returned with the user form fields still in progress.

![Edit Recipe Form Cancel](readme/assets/images/edit-recipe-form-cancel.png)

[Back to top](<#contents>)

#### Log In To Edit Recipe

During the process of creating the edit recipe page, it occurred to me that some site users may try to edit recipes by manually entering the URL of the recipe into their browser URL bar. To defend against this I created a notification that hides the recipe form and displays a notification to the user if they visit the edit recipe page but they are not logged in. This notification prompts the user to sign up or log in to edit a recipe. It also provides them with a link to the home page to navigate away from the edit page. 

![Edit Recipe Logged In](readme/assets/images/edit-recipe-logged-in.png)

[Back to top](<#contents>)

#### Edit Recipe Notification

If a user successfully submits the edit recipe form, the page is refreshed and the form is hidden. A centralised content box is displayed to the user which thanks them for editing their recipe and confirms the successful form submission. The user is then presented with a button link to the my recipes page and a button link to the home page for easy navigation away from the page.

![Edit Recipe Success](readme/assets/images/edit-recipe-success.png)

[Back to top](<#contents>)

### 404 Page

The 404 page is triggered when a user navigates to a site URL which doesn't exist. This could be because of a number of reasons, including a faulty link or an expired URL. Most users will not see this page, but it is there as a backup for users who encounter these rare errors. The purpose of the 404 page is to notify the user that there has been an error, and the page that they have tried to access cannot be found. The Viva La Nacho 404 page provides a button link to the homepage for the user to easily navigate back home.

![404 Page](readme/assets/images/404-page.png)

[Back to top](<#contents>)

## Future Features

I believe the Viva La Nacho site has a lot of potential for expansion in the future. The basic functionality is there for the MVP, but there are many features I would like to add in the future.

### Admin Area

I was advised by my mentor to add an admin area for administrators so they wouldn't have to log into the Django admin area. I would have liked to have implemented this prior to the project deadline, but unfortunately due to time constraints, I chose to prioritise other features. The basic concept would be to have an admin navigation option on the main site navigation bar that is only visible to users with admin privilages. Navigating to this page would open a dashboard for administrators to view the basic site stats like number of posts and comments and new users. They would also be able to execute basic tasks and actions like approving comments and adding a featured recipe. This page would have to be secured and hidden from other site users.

[Back to top](<#contents>)

### User Profile

Another feature that I believe would greatly improve on the site would be a customisable user profile section. In this section logged in / authorised users would be able to edit and update their profile details. They would also be able to add a profile picture / avatar for further profile customisation. This would greatly improve the social element of the app and the overall user experience. This was another feature I wanted to implement but it was delayed due to other features taking priority. 

[Back to top](<#contents>)

### User Change Password

One of the first new features I will impliment in the future will be a user password change option for users who forget or want to change their password. Currently a user has no way to retrieve their password / profile if they forget their log in details. This could result in the user losing access to their profile and recipes. This is a big problem and could lead to users abandoning the site in the future. Hence this feature is a priority moving forwards.

[Back to top](<#contents>)

### Sign Up Email Confirmation

Another future feature I would like to implement relating to authorisation is a user sign-up email confirmation. I would like a user sign-up form submission to trigger an automated email into the user inbox prompting them to confirm their email address. This would help to prevent spam profiles. Users who sign up but don't confirm their email can still view the site but have limited access to site functionality such as posting and commenting.

[Back to top](<#contents>)

### Recipe Categories

The Viva La Nacho site currently features recipe category fields which do not have any usable functionality. These fields were originally intended to group recipes together to be displayed in recipe category lists / sections. This is definitely a feature I would like to integrate in the future. I would also like for a user to be able to search the site for a food category and be presented with recipes that match that category.

[Back to top](<#contents>)

### Search Recipes

I did plan to have a search bar on the homepage in the original Viva La Nacho wireframe designs. Unfortunately this feature was delayed due to being a low priority in comparison to other features. In the future I would like a user to be able to use the search bar field on the homepage to search for specific recipes / categories. Submitting this field would then return a search template page with a list of any matching results. This would be a better experience for the user rather than having to manually search for a particular recipe.

[Back to top](<#contents>)

# Technologies Used

## Languages

* [HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML) - Provides the basic content and structure for the site.
* [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS) - Provides the styling for the site.
* [Python](https://www.python.org/) - Provides the functionality for the site.
* [JavaScript](https://www.javascript.com/) - Provides the interactivity and front end functionality for the site.
* [Git](https://git-scm.com/) - Provides the version control system for the site.

[Back to top](<#contents>)

## Frameworks

* [Tailwind](https://tailwindcss.com/) - A front end CSS utility framework for rapidly building websites.
* [Django](https://www.djangoproject.com/) - A high level Python web framework.

[Back to top](<#contents>)

## Software

* [Balsamiq](https://balsamiq.com/) - An online cloud based software used for creating the site wireframes.
* [GitHub](https://github.com/) - An internet hosting service used for version control. Used to host the Viva La Nacho repository and for the project board used for project management and user stories.
* [GitPod](https://www.gitpod.io/) - A cloud development environment used as the primary site code editor.
* [Heroku](https://dashboard.heroku.com/) - A cloud platform used to host the Viva La Nacho full stack application.
* [ElephantSQL](https://www.elephantsql.com/) - A free cloud based PostgreSQL database system used for the application database.
* [Cloudinary](https://cloudinary.com/?&utm_campaign=1329&utm_content=instapagelogocta-selfservetest) - A cloud based video and image management platform used to store the site images.
* [Slack](https://slack.com/intl/en-gb/) - An online instant messaging program used for site feedback and guidance from the [Code Institute](https://codeinstitute.net/) community.
* [Skype](https://www.skype.com/en/) - An online telecommunications application used for mentor sessions.
* [App Diagrams](https://app.diagrams.net/) - An online diagram software used for the database schemas.
* [Google Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) - A set of web developer tools built directly into the chrome browser. Used for responsiveness tests and further testing.
* [Google Fonts](https://fonts.google.com/) - A web based font service by Google used to supply the site typography.
* [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) - An open source automated testing tool used for site tests.
* [Responsive Design Checker](https://responsivedesignchecker.com/) - An online testing tool used for responsive site testing.
* [Am I Responsive](https://ui.dev/amiresponsive) - An online testing tool used for responsive site testing.
* [Wave Web Accessibility Evaluation Tool](https://wave.webaim.org/) - An online suite of evaluation tools use to test the site for accessibility.

[Back to top](<#contents>)

## Libraries

This is a list of the Python / Django libraries used in this project.

* [asgiref](https://github.com/django/asgiref) - A standard Python library to allow for asynchronous web apps and servers to communicate with each other. 
* [binaryornot](https://pypi.org/project/binaryornot/) - An ultra lightweight Python package to guess whether a file is binary or text.
* [chardet](https://pypi.org/project/chardet/) - A universal encoding detector for Python3.
* [click](https://click.palletsprojects.com/en/8.1.x/) - A Python package for creating beautiful command line interfaces in a composable way with as little code as possible.
* [cloudinary](https://pypi.org/project/cloudinary/) - A Python package allowing integration between the application and Cloudinary. 
* [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/) - A Python package used to create projects from project templates.
* [dj-database-url](https://pypi.org/project/dj-database-url/) - A Django utility to utilise the DATABASE_URL environment variable to configure the Django application. Used with PostgreSQL.
* [dj3-cloudinary-storage](https://pypi.org/project/dj3-cloudinary-storage/) - A Django package that facilitates integration with Cloudinary storage.
* [Django](https://www.djangoproject.com/) - A python package for the Django framework.
* [django-active-link](https://pypi.org/project/django-active-link/) - A Django package used to highlight an active link in the site navigation bars.
* [django-allauth](https://django-allauth.readthedocs.io/en/latest/) - An integrated set of Django applications addressing user authentication, registration and account management.
* [django-browser-reload](https://github.com/adamchainz/django-browser-reload) - A Django package to automatically refresh the browser during development.
* [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) - A Django package that provides tags and filters to control the rendering behaviour of Django forms.
* [django-summernote](https://pypi.org/project/django-summernote/) - A Django package to allow for the embedding of the summernote text editor into Django.
* [django-tailwind](https://django-tailwind.readthedocs.io/en/latest/installation.html) - A Django package to allow for the easy integration of the Tailwind CSS utility framework with Django.
* [gunicorn](https://gunicorn.org/) - A Python WSGI HTTP Server for UNIX.
* [jinja2-time](https://pypi.org/project/jinja2-time/) - A Jinja2 Python extension for dates and times.
* [oauthlib](https://github.com/oauthlib/oauthlib) - A generic, spec-compliant, thorough implementation of the OAuth request-signing logic for Python 3.6+.
* [psycopg2](https://pypi.org/project/psycopg2/) - A PostgreSQL database adapter for Python.
* [PyJWT](https://pyjwt.readthedocs.io/en/latest/) - A Python library that allows for encoding and decoding of JSON Web Tokens (JWT).
* [python-slugify](https://pypi.org/project/python-slugify/) - A Python application that generates slug fields from unicode strings.
* [python3-openid](https://pypi.org/project/python3-openid/) - A set of Python packages to support use of the OpenID decentralized identity system.
* [pytz](https://pypi.org/project/pytz/) - A Python package for world timezone definitions, modern and historical.
* [requests-oauthlib](https://pypi.org/project/requests-oauthlib/) - A Python package for OAuthlib authentication support for Requests.
* [sqlparse](https://pypi.org/project/sqlparse/) - A non-validating SQL parser for Python.
* [text-unidecode](https://pypi.org/project/text-unidecode/) - The most basic Text::Unidecode port for Python.

[Back to top](<#contents>)

# Testing

The Viva La Nacho site has been tested rigorously throughout the development process. This section will provide documentation on the tests carried out.

## User Story Tests

1. As a **user** I can **view a list of recipes I have liked** so that **I can easily review my favourites**

### Acceptance Criteria:
* Acceptance Criteria 1: A 'my favourites' link should appear in the site nav for a logged in user
* Acceptance Criteria 2: The link should open the 'my favourites' page which displays a list of all the current users liked recipes
* Acceptance Criteria 3: Each recipe should provide a link to the full recipe page

### Tasks:
- &check; Add MyFavourites class view with logic into views.py
- &check; Add URL path for the MyFavourites view in urls.py
- &check; Create template for my_favourites and add content, logic and styling
- &check; Add template URL link to base template nav menus
- &check; Test functionality

2. As a **user** I can **delete one or more of my recipes** so that **I can remove them from the site and from public view**

### Acceptance Criteria:
* Acceptance Criteria 1: When a user is logged in and has saved recipes, the 'my recipes' page should show a delete button beside all recipes
* Acceptance Criteria 2: When clicked by a user, the delete button should open a pop-up window asking the user to confirm their intention to delete their recipe. They should also be warned that this cannot be undone and the recipe will be lost. 
* Acceptance Criteria 3: The user should be presented with a go-back button and a confirm deletion button. Clicking the go back button should close the pop-up window and return the user to the original 'my recipes' view. 
* Acceptance Criteria 4: Clicking the confirm deletion button should delete the recipe, remove it from the home page and refresh the 'my recipes' page to show that the recipe is no longer on the list

### Tasks:
- &check; Add a DeleteRecipe view to views.py with logic 
- &check; Add the DeleteRecipe view path to urls.py 
- &check; Add the delete_recipe link url to the my_recipes template 
- &check; Test functionality

3. As a **user** I can **view a list of the recipes I have posted** so that **I can easily review them and edit them if necessary**

### Acceptance Criteria:
* Acceptance Criteria 1: A link called my recipes should appear in the site nav bar 
* Acceptance Criteria 2: The link should only appear to logged in users
* Acceptance Criteria 3: The link should navigate the user to a 'my recipes' page which displays the recipes the user has posted
* Acceptance Criteria 4: This page should display a message of 'sorry, you have no recipes yet' if the user doesn't have any posted recipes
* Acceptance Criteria 5: The page should also feature a 'post a recipe' button which navigates the user to the post a recipe page form

### Tasks:
- &check; Add MyRecipes class view with logic to views.py
- &check; Add URL path for MyRecipes class in urls.py
- &check; Create template for my_recipes and add logic, content and styling
- &check; Add URL link to my_recipes into base template navigation menus
- &check; Test functionality

4. As a **user** I can **edit my current recipes** so that **I can add amendments to the recipe or publish the recipe if it is a draft**

### Acceptance Criteria:
* Acceptance Criteria 1: When a user is logged in and has saved recipes, the 'my recipes' page should show an edit button beside all recipes
* Acceptance Criteria 2: The edit button should open the edit recipe page with a pre-populated form for the current recipe fields
* Acceptance Criteria 3: The user should be able to edit the content of the fields and click the submit button to overwrite the current form fields 
* Acceptance Criteria 4: A 'go back' button should also be displayed on the page to redirect the user back to the 'my recipes' page if they wish to cancel the amendments 
* Acceptance Criteria 5: Upon submission the user should be redirected back to the 'my recipes' page and a 'recipe successfully updated' alert should appear at the top of the screen to notify the user of the successful update

### Tasks:
- &check; Add an EditRecipe view class with logic to views.py 
- &check; Add a URL path for EditRecipe in urls.py 
- &check; Create edit_recipe template and add form and content to template
- &check; Add URL link to my_recipes template 
- &check; Test functionality

5. As a **user** I can **store my recipe post as a draft** so that **I can come back another time and add changes before publishing it online**

### Acceptance Criteria:
* Acceptance Criteria 1: The post a recipe form should feature a tick-box field that a user can tick to save the post as a draft
* Acceptance Criteria 2: On submission, the user should be redirected to the 'my recipes' page 
* Acceptance Criteria 3: The recipe should appear on the 'my recipes' page with a 'draft' label showing next to it

### Tasks:
- &check; Add logic to MyRecipes class view to include draft recipes
- &check; Add status field to RecipeForm class in forms.py
- &check; Style status field on post_recipe and edit_recipe templates
- &check; Add draft tag and logic to my_recipes template
- &check; Test functionality

6. As a **user** I can **post a recipe** so that **it can be shared online with the community**

### Acceptance Criteria:
* Acceptance Criteria 1: A 'post a recipe' link should appear in the site nav bar
* Acceptance Criteria 2: The 'post a recipe' link should only appear for logged in users
* Acceptance Criteria 3: The link should open the post a recipe page with the post a recipe form
* Acceptance Criteria 4: On submission, the recipe should be added to the 'my recipes' page and available to view on the home page and on the recipes full details page. The user should also be redirected to 'my recipes' page and a 'recipe successfully posted' alert should appear at the top of the page to notify the user of the successful posting

### Tasks:
- &check; Add RecipeForm class to forms.py 
- &check; Add PostRecipe class view to views.py and link form
- &check; Add URL path for PostRecipe to urls.py
- &check; Create post_recipe template with form, logic and content
- &check; Add post_recipe URL links to base template nav bars
- &check; Test functionality

7. As a **user** I can **like a recipe** so that **I can view that recipe in the recipe list on my 'my favourites' page at a later date**

### Acceptance Criteria:
* Acceptance Criteria 1: A heart icon should appear next to each recipe on the home page as well as on the individual recipe details pages
* Acceptance Criteria 2: The heart icon should only function if a user is logged in
* Acceptance Criteria 3: If a user clicks the heart icon when not logged in the icon doesn't change
* Acceptance Criteria 4: If a user clicks the heart icon when logged in the page should refresh and an alert should be displayed to the user that the recipe has been added to the 'my favourites' page
* Acceptance Criteria 5: When active, the heart icon should change colour to display that the recipe has been liked

### Tasks:
- &check; Add likes many-to-many field into Recipe model
- &check; Add RecipeLike view to views.py
- &check; Add URL for RecipeLike to urls.py
- &check; Add links to RecipeLike to recipe_details template
- &check; Test functionality

8. As a **user** I can **unlike a recipe** so that **I can remove the recipe list on the 'my favourites' page**

### Acceptance Criteria:
* Acceptance Criteria 1: A user should be able to unlike a recipe by clicking the heart icon next to the recipe
* Acceptance Criteria 2: This functionality should only be available to users who are logged in
* Acceptance Criteria 3: When a user clicks the heart icon of a recipe which is already liked, the current page should be refreshed and an alert should be displayed to the user that the recipe has been removed from the 'my favourites' page
* Acceptance Criteria 4: The icon should return back to its original colour to signify it is no longer liked
* Acceptance Criteria 5: This functionality should also be available from the 'my favourites' page

### Tasks:
- &check; Add UnlikeRecipe view with logic to views.py
- &check; Add path for UnlikeRecipe view in urls.py
- &check; Add links into my_favourites template
- &check; Test functionality

9. As a **user** I can **post a comment on a recipe** so that **I can interact with the author and community**

### Acceptance Criteria:
* Acceptance Criteria 1: A comment form should appear beneath each recipe on the individual recipe details pages
* Acceptance Criteria 2: The comment field should only appear to logged in users
* Acceptance Criteria 3: The comment form should feature a text area input field and a submit button
* Acceptance Criteria 4: Upon submitting the comment the page should refresh and an alert should be displayed to the user with the message 'comment submitted and awaiting approval'
* Acceptance Criteria 5: After admin approval the comment should appear on the recipe page

### Tasks:
- &check; Add CommentForm class to forms.py
- &check; Add post comment function to RecipeDetails view
- &check; Add comment form with logic and content to recipe_details template
- &check; Test functionality

10. As an **administrator** I can **delete a user account** so that **I can remove users that are violating the community standards**

### Acceptance Criteria:
* Acceptance Criteria 1: The administrator should be able to log into the site admin area and view a list of current users
* Acceptance Criteria 2: Each user should feature an 'x' icon or delete button next to their username or email address
* Acceptance Criteria 3: Upon clicking the delete button a pop-up window should open asking for the administrator to confirm their decision to delete the user. The window should display a message warning that the action cannot be undone.
* Acceptance Criteria 4: A cancel button should be available for the administrator to cancel the action and return to the unedited list
* Acceptance Criteria 5: Upon clicking the window delete button the user should be deleted along with all their comments and recipes. The admin area should be refreshed showing the updated user list with the deleted user removed

### Tasks:
- &check; Set up allauth with django
- &check; Add users to database
- &check; Test functionality

11. As a **user** I can **log into my account** so that **I can access my recipes and interact with the community**

### Acceptance Criteria:
* Acceptance Criteria 1: A login link should appear in the site nav bar
* Acceptance Criteria 2: The link should only appear to users who aren't logged in
* Acceptance Criteria 3: The link should lead to a login page and redirect back to the homepage after the user logs in

### Tasks:
- &check; Install allauth package to django
- &check; Add allauth settings into settings.py
- &check; Copy login allauth template and add content and custom styling
- &check; Add URL to login template to base template navigation menus
- &check; Test functionality

12. As a **user** I can **sign out of my account** so that **I can close the application and navigate away from the page**

### Acceptance Criteria:
* Acceptance Criteria 1: A log out link should appear in the site nav bar
* Acceptance Criteria 2: The link should only appear to users who are logged in 
* Acceptance Criteria 3: When clicked the link should log the user out and redirect them to the home page

### Tasks:
- &check; Implement allauth account_logout functionality
- &check; Add custom styling to logout template
- &check; Add URL link to logout template to base template navigation menus
- &check; Test logout functionality

13. As a **user** I can **register my details** so that **I can create an account and access all the app features**

### Acceptance Criteria:
* Acceptance Criteria 1: A sign up link should appear in the site nav bar
* Acceptance Criteria 2: The link should open the create an account page with a form for a user to enter their email and password
* Acceptance Criteria 3: Upon submission the user should be automatically logged in and redirected to the home page

### Tasks:
- &check; Add python allauth package
- &check; Add allauth settings into settings.py 
- &check; All allauth URL path into urls.py
- &check; Test register functionality
- &check; Copy template files into templates directory and add custom content and styling
- &check; Add register URL links to base template navigation menus

14. As a **user** I can **view at least one image of the recipe** so that **I can see what the finished recipe looks like**

### Acceptance Criteria:
* Acceptance Criteria 1: Post a recipe forms should have a required featured image input field and three optional extra image fields
* Acceptance Criteria 2: The featured image for each recipe should display on the home page 
* Acceptance Criteria 3: The featured image and any further images should display on the full recipe page
* Acceptance Criteria 4: Gallery images on the recipe page should be clickable to display the full-size image

### Tasks:
- &check; Install cloudinary
- &check; Add cloudinary settings into settings.py
- &check; Import cloudinary into models.py
- &check; Add featured image and three gallery image fields to Recipe model using cloudinary fields
- &check; Add image fields to RecipeForm in forms.py
- &check; Add recipe image tags to recipe_details template 
- &check; Add content and styling for recipe images to recipe_details template along with logic for a placeholder if an image isn't used
- &check; Test functionality

15. As a **user** I can **see the preparation and approximate cooking times for all recipes** so that **I can asses what recipes are right for me and plan my cooking time**

### Acceptance Criteria:
* Acceptance Criteria 1: Post a recipe forms should have required preparation and approximate cooking time number fields 
* Acceptance Criteria 2: Preparation and approximate cooking times should display on the full recipe page details 
* Acceptance Criteria 3: The cooking and preparation times should display as coloured badges 

### Tasks:
- &check; Add prep_time field and cooking_time field to Recipe model
- &check; Add fields to RecipeForm in forms.py
- &check; Add recipe prep time and cooking time tags to recipe_details template 
- &check; Add content and styling for recipe prep time and cooking time to recipe_details template
- &check; Test functionality

16. As a **user** I can **see a difficulty rating for each recipe** so that **I can quickly tell if a recipe is too difficult for me**

### Acceptance Criteria:
* Acceptance Criteria 1: Post a recipe forms should display required select fields for easy, medium, hard or expert
* Acceptance Criteria 2: The difficulty rating should appear on every recipe as a coloured label
* Acceptance Criteria 3: Difficulty ratings should appear on all recipes on the home page as well as the individual recipe details pages

### Tasks:
- &check; Add difficulty field to Recipe model
- &check; Add custom difficulties choices to field options
- &check; Add difficulty field to RecipeForm in forms.py
- &check; Add recipe difficulty tag to recipe_details template with logic
- &check; Add content and styling for recipe difficulty to recipe_details template
- &check; Test functionality

17. As a **user** I can **see the approximate amount of people that the recipes can serve** so that **I can easily adjust the ingredient amounts to match the number of people I am cooking for**

### Acceptance Criteria:
* Acceptance Criteria 1: The post a recipe form should have a required serving number field
* Acceptance Criteria 2: The serving number should appear on the details page for every recipe
* Acceptance Criteria 3: The serving number should appear in a coloured label 

### Tasks:
- &check; Add serves field to Recipe model
- &check; Add serves field to RecipeForm in forms.py
- &check; Add recipe serves tag to recipe_details template 
- &check; Add content and styling for recipe serves to recipe_details template
- &check; Test functionality

18. As a **user** I can **see a list of allergens for the recipes** so that **I can avoid any recipes that contain certain allergens**

### Acceptance Criteria:
* Acceptance Criteria 1: The post a recipe form should contain a required tick-box field for allergens
* Acceptance Criteria 2: The allergens for each recipe should be displayed on the individual recipe full details pages
* Acceptance Criteria 3: The allergens should all be displayed in an easy to view list format which is clearly displayed

### Tasks:
- &check; Add allergens array field to Recipe model
- &check; Add model method string_of_allergens to return a string of the allergens array field 
- &check; Add custom array field class to allow multiple checkbox inputs
- &check; Add allergens field to RecipeForm in forms.py
- &check; Add recipe allergens tag to recipe_details template 
- &check; Add content and styling for recipe allergens to recipe_details template
- &check; Test functionality

19. As a **user** I can **see a summarised list of ingredients for each recipe** so that **I can quickly and easily read through the ingredients to get an idea of the amounts required**

### Acceptance Criteria:
* Acceptance Criteria 1: Post a recipe forms should have a required text field for an unordered list of ingredients and amounts with visual instructions on how to format the text
* Acceptance Criteria 2: Full ingredient lists should be displayed on each recipe's full details page
* Acceptance Criteria 3: The ingredients should be displayed as an unordered list with nicely formatted spacing and margins to make them easy to read

### Tasks:
- &check; Add ingredients field to Recipe model
- &check; Add ingredients field to RecipeForm in forms.py
- &check; Import summernote to RecipeForm and add widget to field
- &check; Add recipe ingredients tag to recipe_details template 
- &check; Add content and styling for recipe ingredients to recipe_details template
- &check; Test functionality

20. As a **user** I can **see a numbered list of steps to follow for the recipe methods** so that **I can easily follow the instructions one by one**

### Acceptance Criteria:
* Acceptance Criteria 1: Post a recipe forms should feature a required recipe method text input field. 
* Acceptance Criteria 2: Recipe methods should be displayed on each recipes full details page in a numbered list of steps
* Acceptance Criteria 3: Steps should be easy to read and formatted well with spacing and margins 

### Tasks:
- &check; Add method field to Recipe model
- &check; Add method field to RecipeForm in forms.py
- &check; Import summernote to RecipeForm and add widget to field
- &check; Add recipe method tag to recipe_details template 
- &check; Add content and styling for recipe method to recipe_details template
- &check; Test functionality

21. As a **user** I can **click on a recipe link on the home page and be directed to a full page for the recipe** so that **I can see the full recipe details and find out more information**

### Acceptance Criteria:
* Acceptance Criteria 1: A user should be able to click on any recipe displayed on the home page and be redirected to that recipes full page recipe details
* Acceptance Criteria 2: The page should feature the recipes full details as well as a back button to navigate the user back to the home page

### Tasks:
- &check; Add RecipeDetails class view with logic to views.py
- &check; Add URL path RecipeDetails in urls.py 
- &check; Create recipe_details template with content and logic 
- &check; Add URL links to recipe_details to each recipe on the index template, as well as the my_favourites template and all recipes that are published on the my_recipes template
- &check; Test functionality

22. As a **user** I can **view comments on a recipe** so that **I can see what members of the community have said about the recipe**

### Acceptance Criteria:
* Acceptance Criteria 1: Any comments posted by users and approved by admin should appear as an ordered list arranged by date posted
* Acceptance Criteria 2: Comments should appear at the bottom of each recipes full details page
* Acceptance Criteria 3: Each comment should display the comment text body, date posted and author

### Tasks:
- &check; Import Comments model into views.py
- &check; Add comments queryset with logic to RecipeDetails view
- &check; Add comments loop and logic into recipe_details template
- &check; Test functionality

23. As a **user** I can **view a list of the most popular recipes on the home page** so that **I can look at an ordered list of the most popular recipes within the community**

### Acceptance Criteria:
* Acceptance Criteria 1: A list of the most liked recipes should appear on the home page
* Acceptance Criteria 2: The list should be arranged and ordered by most liked
* Acceptance Criteria 3: The list should display a maximum of six recipes

### Tasks:
- &check; Amend RecipeList class view to add queryset for most liked recipes
- &check; Add most popular recipes section with loop logic, content and styling to index template
- &check; Test functionality

24. As an **administrator** I can **post a recipe in the admin area** so that **I can add my own recipe posts**

### Acceptance Criteria:
* Acceptance Criteria 1: The administrator should be able to log into the admin area and view a list of current recipes saved in the database
* Acceptance Criteria 2: There should be an 'add' button which opens a new page with a recipe form
* Acceptance Criteria 3: The administrator should be able to fill out the form and click the save button to add a recipe
* Acceptance Criteria 4: The recipe should appear in the recipe list in the admin area when the page refreshes 

### Tasks:
- &check; Add admin URLS in urls.py
- &check; Configure settings in settings.py
- &check; Import models to admin.py and add classes for each model
- &check; Test functionality

25. As an **administrator** I can **approve a user comment** so that **it can be posted online**

### Acceptance Criteria:
* Acceptance Criteria 1: All comments should first appear as notifications in the site admin area before going live
* Acceptance Criteria 2: The administrator should be able to log into the admin area and review comments listed in order of date posted
* Acceptance Criteria 3: Each comment should feature an approve button which approves the comment and posts the comment live
* Acceptance Criteria 4: Upon approval the comment should be removed from the admin comment approval list 

### Tasks:
- &check; Add approve_comments action to commentadmin class in admin.py
- &check; Add approve_coments function to update comment approved field to true
- &check; Test functionality

26. As an **administrator** I can **disapprove a comment** so that **it is deleted and doesn't go live on the site if it violates the community standards**

### Acceptance Criteria:
* Acceptance Criteria 1: All comments should first appear as notifications in the site admin area before going live
* Acceptance Criteria 2: The administrator should be able to log into the admin area and review comments listed in order of date posted
* Acceptance Criteria 3: Each comment should feature a disapprove button which deletes the comment before it is posted 
* Acceptance Criteria 4: Upon disapproval the comment should be deleted and removed from the admin comment approval list

### Tasks:
- &check; Add approve_comments action to commentadmin class in admin.py
- &check; Add approve_coments function to update comment approved field to true 
- &check; Test functionality

27. As a **user** I can **view recipes on the home page** so that **I can browse through them and find any that interest me**

### Acceptance Criteria:
* Acceptance Criteria 1: The recipes should display as a list on the home page
* Acceptance Criteria 2: The recipes should provide a picture and basic summary of the recipe
* Acceptance Criteria 3: The recipes should be styled displayed in an appealing way 

### Tasks:
- &check; Add RecipeList class view to views.py with logic and queryset for recipes
- &check; Add URL path for the RecipeList view to urls.py
- &check; Create index/homepage template with content, logic and styling
- &check; Create base template with header and footer navigation
- &check; Add links to homepage in base template navigation menus
- &check; Test functionality

28. As a **user** I can **view the featured recipe on the home page** so that **I can see what the recommended recipe of the week is**

### Acceptance Criteria:
* Acceptance Criteria 1: A featured recipe should be available to view at the top of the home page
* Acceptance Criteria 2: The recipe should include a large picture and summary and look eye-catching

### Tasks:
- &check; Amend RecipeList class view in views.py to include a queryset for the featured recipe
- &check; Add featured recipe tags, logic and styling into the index/homepage template
- &check; Test functionality

29. As a **user** I can **view a list of the latest recipes on the home page** so that **I can see if there's anything new that I have missed**

### Acceptance Criteria:
* Acceptance Criteria 1: A list of the latest recipes should display on the home page in a separate category section
* Acceptance Criteria 2: The list should be arranged by date posted 
* Acceptance Criteria 3: The list should display a maximum of six recipes

### Tasks:
- &check; Add created_on date field to Recipe model in models.py
- &check; Add RecipeList class view with queryset logic for latest recipes
- &check; Add URL path for RecipeList to urls.py 
- &check; Create template for home page called index 
- &check; Add extends base and block content tags into template
- &check; Add URL links to the index page into the navigation menus in the base template
- &check; Add latest recipes section with loop logic, content and styling into the home template
- &check; Test functionality

30. As an **administrator** I can **edit user recipes** so that **I can correct grammar or styling issues**

### Acceptance Criteria:
* Acceptance Criteria 1: The administrator should be able to log into the admin area and see a list of all the current recipes
* Acceptance Criteria 2: Each recipe should have an edit button or a pencil icon 
* Acceptance Criteria 3: Upon clicking the edit button or pencil icon the fields for that recipe post should be displayed with the pre-populated field contents
* Acceptance Criteria 4: Contents on the recipe fields should be editable, and clicking the submit button after making field changes should alter the recipe content on the live site on the home page and on the full recipe details page
* Acceptance Criteria 5: It should be possible to cancel the edit action by clicking a cancel or back button on the edit form to return the administrator back to the list without editing the recipe content

### Tasks:
- &check; Import models into admin.py
- &check; Add admin classes for each database model
- &check; Test functionality

31. As an **administrator** I can **delete user recipes** so that **I can remove them from the site if they do against the community standards**

### Acceptance Criteria:
* Acceptance Criteria 1: The administrator should be able to log into the admin area and see a list of all the current recipes
* Acceptance Criteria 2: Each recipe in the list should have an delete button or an 'x' icon
* Acceptance Criteria 3: Upon clicking the delete button or 'x' icon a pop-up window should display on the screen asking the administrator to confirm their intention to delete the recipe. The window should contain text content to inform the administrator that the delete action cannot be undone.
* Acceptance Criteria 4: A cancel button should be available on the window to return the administrator to the unedited list if clicked
* Acceptance Criteria 5: Clicking the confirm/delete button should delete the recipe and remove it from the site completely. The pop-up window should be closed and the window refreshed to show an updated list of recipes with the deleted recipe removed

### Tasks:
- &check; Import models to admin.py
- &check; Add admin classes for each database model
- &check; Test functionality

32. As an **admin** I can **make a recipe featured** so that **the recipe can be viewed as the featured recipe on the home page**

### Acceptance Criteria:
* Acceptance Criteria 1: Admin should be able to log into the admin area and view the list of current recipes
* Acceptance Criteria 2: The admin dashboard should feature an action to add/remove featured
* Acceptance Criteria 3: Admin should be able to tick a recipe and turn the featured field on/off 
* Acceptance Criteria 4: This recipe should then appear on the index page as a featured recipe

### Tasks:
- &check; Add featured field to Recipe model in models.py
- &check; Add add_featured and remove_featured actions and methods into the RecipeAdmin class in admin.py
- &check; Add featured field into RecipeAdmin list display
- &check; Test functionality

33. As a **user** I can **view all the recipes on one page** so that **I can browse all the recipes in one list**

### Acceptance Criteria:
* Acceptance Criteria 1: A 'view all recipes' button link should appear after each recipe list on the index page
* Acceptance Criteria 2: When clicked, the link should open the 'all recipes' page
* Acceptance Criteria 3: All recipes should be displayed as cards in a paginated list 

### Tasks:
- &check; Create AllRecipes class view in views.py
- &check; Add the URL path for the AllRecipes view in urls.py
- &check; Create the all_recipes template with content, styling and logic
- &check; Add URL links from the index template to the all_recipes template
- &check; Test functionality

[Back to top](<#contents>)

## Validator Tests

### W3C (HTML)

When the Viva La Nacho site was first tested with the [W3C HTML Markup Validation Service](https://validator.w3.org/), it showed one error and some warnings. The error was a stray unordered list closing tag and the warnings were due to aria labels being used on non-interactive icon elements. After I fixed these issues the test showed no errors or warnings.

![HTML Validation Test](readme/assets/images/html-validation.png)

[Back to top](<#contents>)

### W3C (CSS)

The Viva La Nacho CSS stylesheet has been tested using the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) by direct input. Unfortunately there were some errors shown for the @tailwind selectors at the top of the CSS file. These selectors are for the tailwind utility framework that Viva La Nacho uses for styling. However, with these selectors commented out the CSS test passed with no errors or warnings.

![CSS Validation Errors](readme/assets/images/css-validation-errors.png)

![CSS Validation Test](readme/assets/images/css-validation.png)

[Back to top](<#contents>)

### PEP8 (PYTHON)

Due to the closure of the PEP8 Python Validation online site, I used the new [Code Institute Python Linter](https://pep8ci.herokuapp.com/) to test all of the Viva La Nacho python code files. No errors were found. 

#### admin.py
![Admin Python Test](readme/assets/images/admin-python-test.png)

#### settings.py
![Settings Python Test](readme/assets/images/settings-python-test.png)

#### forms.py
![Forms Python Test](readme/assets/images/forms-python-test.png)

#### models.py
![Models Python Test](readme/assets/images/models-python-test.png)

#### urls.py
![URLs Python Test](readme/assets/images/urls-python-test.png)

#### views.py
![Views Python Test](readme/assets/images/views-python-test.png)

[Back to top](<#contents>)

### JSHint (JavaScript)

When the Viva La Nacho javascript file script.js was first passed into the [JSHint Javascript Validation Tool](https://jshint.com/) it showed a few errors mainly due to missing semicolons. After the errors were rectified the code passed with no errors or warnings.

![JavaScript Test](readme/assets/images/javascript-test.png)

[Back to top](<#contents>)

## Input Validation Tests

All forms on the Viva La Nacho site have been thoroughly tested for input validation. All the forms on the site use javascript to validate user input. Manual tests have also been conducted on each form field to check for any errors.

### Post Recipe Form Tests

| Status | **Post A Recipe Form**
|:-------:|:--------|
| &check; | Form cannot be submitted with blank title field 
| &check; | Title field cannot be submitted with just whitespace
| &check; | Form cannot be submitted without at least one category selected
| &check; | Form cannot be submitted without prep time being entered
| &check; | Prep time cannot be any character other than a number
| &check; | Prep time cannot be above 600 or below 0
| &check; | Form cannot be submitted without cooking time being entered
| &check; | Cooking time cannot be any character other than a number
| &check; | Cooking time cannot be above 600 or below 0
| &check; | Form cannot be submitted without serving being entered
| &check; | Serving cannot be above 10
| &check; | Form cannot be submitted without difficulty being entered
| &check; | Form cannot be submitted with blank excerpt
| &check; | Excerpt cannot be just whitespace
| &check; | Excerpt character length cannot be greater than 250
| &check; | Form cannot be submitted without at least one allergen selected
| &check; | Form cannot be submitted with blank ingredients field
| &check; | Ingredients field cannot contain just whitespace
| &check; | Form cannot be submitted with blank method field
| &check; | Method field cannot contain just whitespace
| &check; | Form cannot be submitted without uploading one image to the first image field
| &check; | Form cannot be submitted by a non logged in user

[Back to top](<#contents>)

### Edit Recipe Form Tests

| Status | **Edit Recipe Form**
|:-------:|:--------|
| &check; | Form cannot be submitted with blank title field 
| &check; | Title field cannot be submitted with just whitespace
| &check; | Form cannot be submitted without at least one category selected
| &check; | Form cannot be submitted without prep time being entered
| &check; | Prep time cannot be any character other than a number
| &check; | Prep time cannot be above 600 or below 0
| &check; | Form cannot be submitted without cooking time being entered
| &check; | Cooking time cannot be any character other than a number
| &check; | Cooking time cannot be above 600 or below 0
| &check; | Form cannot be submitted without serving being entered
| &check; | Serving cannot be above 10
| &check; | Form cannot be submitted without difficulty being entered
| &check; | Form cannot be submitted with blank excerpt
| &check; | Excerpt cannot be just whitespace
| &check; | Excerpt character length cannot be greater than 250
| &check; | Form cannot be submitted without at least one allergen selected
| &check; | Form cannot be submitted with blank ingredients field
| &check; | Ingredients field cannot contain just whitespace
| &check; | Form cannot be submitted with blank method field
| &check; | Method field cannot contain just whitespace
| &check; | Form cannot be submitted without uploading one image to the first image field
| &check; | Form cannot be submitted by a non logged in user

[Back to top](<#contents>)

### Comment Form Tests

| Status | **Comment Form**
|:-------:|:--------|
| &check; | Form cannot be submitted with blank body field
| &check; | Body field cannot be submitted with just whitespace
| &check; | Form cannot be submitted by a non logged in user

[Back to top](<#contents>)

## Additional Tests

### Manual Tests

There has been extensive manual testing completed on all features of the Viva La Nacho site.

| Status | **Navigation**
|:-------:|:--------|
| &check; | My recipes and my favourites are hidden from a non authorised site user on the header and footer navigation bars
| &check; | Logging in displays the log out navigation link and hides the log in and sign up menu items
| &check; | Log out navigation menu item is not displayed to users who are not signed in
| &check; | Home URL link in header and footer sends user to homepage
| &check; | My favourites URL link in header and footer sends user to my favourites page
| &check; | My recipes URL link in header and footer sends user to my recipes page
| &check; | Login URL link in header and footer sends user to login page
| &check; | Logout URL link in header and footer sends user to logout page
| &check; | Sign up URL link in header and footer sends user to signup page
| &check; | Post a recipe button URL link in header and footer sends user to post recipe page
| &check; | Viva La Nacho logo URL link in header sends user to the homepage
| &check; | Facebook social media icon in footer sends user to https://www.facebook.com and opens in a new tab
| &check; | Instagram social media icon in footer sends user to https://www.instagram.com and opens in a new tab
| &check; | Twitter social media icon in footer sends user to https://www.twitter.com and opens in a new tab
| &check; | Tiktok social media icon in footer sends user to https://www.tiktok.com and opens in a new tab
| &check; | Header and footer are present on all pages of the site
| &check; | Header and footer menus are reponsive on smaller screens
| &check; | Header menu collapses to mobile menu on smaller screens and the menu opens and closes with the menu button

| Status | **Homepage**
|:-------:|:--------|
| &check; | All sections are fully responsive
| &check; | Featured recipe view recipe button sends user to recipe full details
| &check; | All view recipe buttons in latest recipes section cards send user to full recipes
| &check; | View all recipe button in latest recipes section sends user to all recipes page
| &check; | All view recipe buttons in most popular recipes section cards send user to full recipes
| &check; | View all recipe button in most popular recipes section sends user to all recipes page

| Status | **Recipe Details Page**
|:-------:|:--------|
| &check; | All sections are fully responsive
| &check; | Like / unlike recipe icon button is disabled for unauthorised users
| &check; | Authorised users can like / unlike a recipe
| &check; | Number of recipe likes are reflected in the recipe like counter
| &check; | Comment form is hidden for unauthorised users
| &check; | Recipe comments are displayed in comments section after admin approval
| &check; | Page is refreshed and notification is displayed to the user upon successful comment form submission
| &check; | Comment form is hidden on page refresh after a successful comment form submission

| Status | **All Recipes Page**
|:-------:|:--------|
| &check; | All sections are fully responsive
| &check; | All view recipe buttons on recipe cards send user to full recipes
| &check; | Page pagination is hidden when less than nine recipes are published on the site
| &check; | Page pagination is displayed when more than nine recipes are published on the site
| &check; | Page pagination next button takes user to next page of recipes
| &check; | Page pagination last button takes user to last page of recipes
| &check; | Page pagination previous button takes user to previous page of recipes
| &check; | Page pagination first button takes user to first page of recipes

| Status | **Log In Page**
|:-------:|:--------|
| &check; | Form is fully responsive
| &check; | Link to sign up page takes user to sign up page
| &check; | Lets cook button submits log in form
| &check; | Remember me tickbox functionality works
| &check; | Form will not submit with blank username field
| &check; | Form will not submit with blank password field
| &check; | Log in form functionality works

| Status | **Log Out Page**
|:-------:|:--------|
| &check; | Form is fully responsive
| &check; | Log out button link successfully logs user out and redirects them to the homepage
| &check; | Cancel button link cancels user log out and redirects them to the homepage 

| Status | **Sign Up Page**
|:-------:|:--------|
| &check; | Form is fully responsive
| &check; | Link to log in page takes user to log in page
| &check; | Lets cook button submits sign up form
| &check; | Form will not successfully submit with blank username field
| &check; | Form will not successfully submit with blank password field
| &check; | Form will not successfully submit with a password field value below 8 characters
| &check; | Form will not successfully submit while the passworld fields don't match
| &check; | Form will not successfully submit while the email address matches another user email
| &check; | Form will not successfully submit while the username matches another username
| &check; | Sign up form functionality works and a new user is created with a successful form submission
| &check; | Upon a successful form submission the user is redirected to the homepage as an authorised user

| Status | **Post Recipe Page**
|:-------:|:--------|
| &check; | Form is fully responsive
| &check; | Form is hidden to non authorised users and log in content box is displayed
| &check; | Log in button in log in box sends user to log in page
| &check; | Sign up button in log in box sends user to sign up page
| &check; | Home button in log in box sends user to homepage
| &check; | Form is dispayed to authorised users
| &check; | Form submit button submits form 
| &check; | Form cancel button hides form and displays are you sure you want to cancel notification
| &check; | Are you sure you want to cancel home button redirects user to homepage
| &check; | Are you sure you want to cancel no / cancel button returns to form with fields returned with in progress content
| &check; | JavaScript functionality prevents form from being submitted until all fields pass JavaScript tests
| &check; | Selecting draft recipe on form field drafts a recipe that doesn't appear publicly on the site
| &check; | All fields successfully submit and are stored in the database
| &check; | Cloudinary image fields save the images to cloudinary
| &check; | Summernote fields return formatted text
| &check; | Category and allergen fields are saved as an array
| &check; | On successful form submission a new recipe instance is created
| &check; | On successful form submission the page is refreshed, the form is hidden and the thank you for posting a recipe notification is displayed
| &check; | The thank you for posting a recipe post another recipe button link refreshes the page and displays the form
| &check; | The thank you for posting a recipe home button link sends the user to the home page

| Status | **Edit Recipe Page**
|:-------:|:--------|
| &check; | Form is fully responsive
| &check; | Form is hidden to non authorised users and log in content box is displayed
| &check; | Log in button in log in box sends user to log in page
| &check; | Sign up button in log in box sends user to sign up page
| &check; | Home button in log in box sends user to homepage
| &check; | Form is dispayed to authorised users
| &check; | Form submit button submits form 
| &check; | Form fields are automatically filled in with recipe instance content
| &check; | Form cancel button hides form and displays are you sure you want to cancel notification
| &check; | Are you sure you want to cancel home button redirects user to homepage
| &check; | Are you sure you want to cancel no / cancel button returns to form with fields returned with in progress content
| &check; | JavaScript functionality prevents form from being submitted until all fields pass JavaScript tests
| &check; | On successful form submission the recipe is successfully amended
| &check; | All fields successfully submit and are stored in the database
| &check; | On successful form submission the page is refreshed, the form is hidden and the thank you for editing your recipe notification is displayed
| &check; | The thank you for editing your recipe my recipes button link takes the user to the my recipes page
| &check; | The thank you for editing your recipe home button link takes the user to the homepage

| Status | **My Favourites Page**
|:-------:|:--------|
| &check; | The page is fully responsive
| &check; | Authorised users see a list of all the recipes they have currently liked on the my favourites page
| &check; | All view recipe buttons on recipe cards send the user to the full recipes 
| &check; | All cards feature the correct information for each recipe
| &check; | Clicking the unlike button hides the recipe content and displays the unlike confirmation notification
| &check; | Clicking the cancel button on the unlike recipe notification hides the noitification and shows the recipe content
| &check; | Clicking the unlike button on the unlike recipe notification refreshes the page and displays the recipe unlike notification with the recipe removed from the page
| &check; | User unliking a recipe functionality works and removes user from recipe likes
| &check; | The unlike recipe notification is dismissed automatically in three seconds
| &check; | The unlike recipe notification is dismissed by clicking the x icon button on the notification
| &check; | When a user has no liked recipes the no liked recipes notification displays
| &check; | The home button link on the no liked recipes notification returns the user to the home page

| Status | **My Recipes Page**
|:-------:|:--------|
| &check; | The page is fully responsive
| &check; | Authorised users see a list of all the recipes they currently submitted into the site
| &check; | All view recipe buttons on recipe cards send the user to the full recipes 
| &check; | All cards feature the correct information for each recipe
| &check; | The view recipe button doesn't appear on recipes that are drafted and not published
| &check; | The published tag shows on published recipes and the drafted tag shows on drafted recipes
| &check; | The view recipe button doesn't appear on recipes that are drafted and not published
| &check; | Each recipe edit button link takes the user to the edit recipe form page with fields filled out with the correct recipe instance content
| &check; | Clicking the delete button hides the recipe content and displays the delete recipe confirmation notification
| &check; | Clicking the cancel button hides the delete recipe confirmation notification and displays the recipe content
| &check; | Clicking the delete button on the recipe confirmation notification refreshes the page and displays the recipe deleted notification with the recipe removed from the recipe list
| &check; | User delete recipe functionality works and removes recipe from site and database
| &check; | The recipe deleted notification is dismissed automatically in three seconds
| &check; | The recipe deleted notification is dismissed by clicking the x icon button on the notification
| &check; | When a user has no recipes the no recipes notification is displayed
| &check; | The post a recipe button link on the no recipes notification takes the user to the post a recipe form page
| &check; | The home button link on the no recipes notification takes the user to the homepage

| Status | **404 Page**
|:-------:|:--------|
| &check; | The page is fully responsive
| &check; | The 404 page is triggered and displayed when a user navigates to a site URL that doesn't exist
| &check; | The home button link on the 404 page notification takes the user back to the homepage

[Back to top](<#contents>)

### Automated Tests

Due to unfortunate and unexpected compatibility issues between the Viva La Nacho models and the databases, automated tests were unable to be carried out fully. Sadly the ElephantSQL database does not support test databases being created for testing, and the local sqlite3 database does not support the array fields used in the Viva La Nacho Recipe model. Code Institute tutors advised it would be quite difficult to rectify the situation, so given the time constraints and deadline for the fourth project submission, it was decided to attempt to remedy this with rigorous and extensive manual testing. With a greater timescale, more work would have been done to rectify this problem. I did however write some example model tests in the test_models.py file to show some examples of what I would have done.

![Automated Test Examples](readme/assets/images/automated-test-example.png)

[Back to top](<#contents>)

### Responsive Tests

Viva La Nacho has been tested on a diverse range of different devices and screen sizes to test for style and layout issues. Manual responsive tests were carried out using [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/), [Responsive Design Checker](https://responsivedesignchecker.com/) and [Am I Responsive](https://ui.dev/amiresponsive) as well as on a number of physical devices. All device screen sizes were tested on Chrome Dev Tools as well as Responsive Design Checker and no issues were found.

| Status | **Chrome Dev Tools**
|:-------:|:--------|
| &check; | iPhone SE
| &check; | iPhone XR
| &check; | iPhone 12 Pro
| &check; | Pixel 5
| &check; | Samsung Galaxy S8+
| &check; | Samsung Galaxy S20 Ultra
| &check; | iPad Air
| &check; | iPad Mini
| &check; | Surface Pro 7
| &check; | Surface Duo
| &check; | Galaxy Fold
| &check; | Samsung Galaxy A51/71
| &check; | Nest Hub
| &check; | Nest Hub Max
| &check; | iPhone 6/7/8
| &check; | Responsive mode

| Status | **Responsive Design Checker**
|:-------:|:--------|
| &check; | 24" Desktop
| &check; | 23" Desktop
| &check; | 22" Desktop
| &check; | 20" Desktop
| &check; | 19" Desktop
| &check; | 15" Desktop
| &check; | 13" Notebook
| &check; | 10" Notebook
| &check; | Apple iPad Mini
| &check; | Apple iPad Retina
| &check; | Apple iPad Pro
| &check; | Amazon Kindle Fire
| &check; | Amazon Kindle Fire HD
| &check; | Asus Eee 1000
| &check; | Nexus 7
| &check; | Nexus 9
| &check; | Samsung Galaxy Tab 10
| &check; | Apple iPhone 3/4/4s
| &check; | Apple iPhone 5/5s
| &check; | Apple iPhone 6/6s/7
| &check; | Apple iPhone 6s Plus/7 Plus
| &check; | Samsung Galaxy S5/S6/S7
| &check; | Sony Xperia Z2/Z3
| &check; | Google Pixel
| &check; | Nexus 4
| &check; | Nexus 5
| &check; | Nexus 6

![Viva La Nacho Responsive Screens](readme/assets/images/viva-la-nacho-responsive.png)

[Back to top](<#contents>)

### Browser Tests

The Viva La Nacho site has been tested on Google Chrome, Apple Safari, Microsoft Edge and Brave with no errors found in style, layout or functionality.  

[Back to top](<#contents>)

### Lighthouse Tests

Viva La Nacho has been tested using the [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) [Lighthouse Tester](https://developer.chrome.com/docs/lighthouse/overview/) and has returned good results. Performance on the first tests was lower due to large images. This was resolved by resizing and compressing the images. The final page test results can be seen below.

#### Homepage Lighthouse Test
![Homepage Lighthouse Test](readme/assets/images/homepage-lighthouse.png)

#### Recipe Details Lighthouse Test
![Recipe Details Lighthouse Test](readme/assets/images/recipe-details-lighthouse.png)

#### All Recipes Lighthouse Test
![All Recipes Lighthouse Test](readme/assets/images/all-recipes-lighthouse.png)

#### Post A Recipe Lighthouse Test
![Post A Recipe Lighthouse Test](readme/assets/images/post-recipe-lighthouse.png)

#### My Recipes Lighthouse Test
![My Recipes Lighthouse Test](readme/assets/images/my-recipes-lighthouse.png)

#### My Favourites Lighthouse Test
![My Favourites Lighthouse Test](readme/assets/images/my-favourites-lighthouse.png)

#### Signup Lighthouse Test
![Sign Up Lighthouse Test](readme/assets/images/sign-up-lighthouse.png)

#### Log In Lighthouse Test
![Log In Lighthouse Test](readme/assets/images/log-in-lighthouse.png)

#### Log Out Lighthouse Test
![Log Out Lighthouse Test](readme/assets/images/log-out-lighthouse.png)

#### Edit Recipe Lighthouse Test
![Edit Recipe Lighthouse Test](readme/assets/images/edit-recipe-lighthouse.png)

[Back to top](<#contents>)

### Wave Accessibility Tests

Viva La Nacho has been manually checked for accessibility issues but has also been tested through the [Wave Accessibility Evaluation Tool](https://wave.webaim.org/). No errors or contrast issues were found.

![Wave Accessibility Evaluation Tool](readme/assets/images/viva-la-nacho-wave-accessibility.png)

[Back to top](<#contents>)

## Bugs

A number of bugs presented themselves during the Viva La Nacho development process. Most of these bugs were resolved, but unfortunately, due to time constraints, some of them weren't.

### Resolved 

* In the early stages of development, I couldn't get the Tailwind CSS framework working on Heroku. Styling was showing on the development environment but not on the live site. This was resolved by removing the disable collect static environment variable from the Heroku config vars, to allow for the CSS and JS files to be loaded.
* When work first began on the post a recipe form, the form images were not being uploaded to cloudinary on submission and consequently weren't being submitted. This resulted in every user submitted recipe showing the placeholder image. To resolve this issue, I added the cloudinary tag to the post a recipe template and added request.FILES into the view post request. I also added enctype="multipart/form-data" to the HTML form in the template. 
* When JavaScript validation was first written to validate form input, there was a bug on safari where the failed input notifications weren't being shown and the form wasn't submitting. This was due to the javascript function throwing an error. This was resolved by rewriting the javascript function to remove the errors and using the preventdefault function on the submit button.

[Back to top](<#contents>)

### Unresolved

* There is currently a database-related error in Viva La Nacho that relates to testing. This error resulted in not being able to run working automated tests on either the local or the online database. The online PostgreSQL database doesn't support creating a test database, and the local database doesn't support the array fields that are used in the Viva La Nacho models. Unfortunately, this created an issue running tests, as I couldn't use either of the databases to run the tests. I didn't want to have to change my models, database or dramatically change my Django settings just to enable a test database, so I combatted this by doing increased manual testing on all features. I did contact tutor support and consult the slack community for guidance, and they agreed it was not an easy problem to solve. Given more time I would have attempted to create a local PostgreSQL database purely for testing.
* At the beginning of the project I accidentally committed a secret key variable inside the settings.py file to the git repository. I didn't notice this mistake until later in the project. I have now changed the secret key and placed the new one inside an environment variable, but the original secret key still remains in the git commit history. I did do some research into how to remove this, but at this stage I didn't want to risk changing the repository history, and as I have changed the secret key, this shouldn't pose a security risk going forwards.

[Back to top](<#contents>)

# Deployment

## Project Deployment via Heroku

This is a guide on how to deploy a full stack web application via [Heroku](https://www.heroku.com).

1. **Open your project in a code editor e.g [GitPod](https://www.gitpod.io/) or [VS Code](https://code.visualstudio.com/) and make sure it is connected to a GitHub repo.**

2. **Install Django and supporting libraries** 
* In the terminal type pip3 install 'django<4' gunicorn
* In the terminal type pip3 install dj_database_url psycopg2
* In the terminal type pip3 install dj3-cloudinary-storage

3. **Create a requirements file**
* type pip3 freeze --local > requirements.txt

4. **Create a Django project** 
* In the terminal type django-admin startproject 'project_name' - project_name is desired project name

5. **Create app**
* In the terminal type python3 manage.py startapp 'app_name' - app_name is desired app name

6. **Add the new app into settings.py**
* In settings.py add the app name into the installed apps array variable and save the file

7. **Migrate Changes**
* In the terminal type python3 manage.py migrate
* In the terminal type python3 manage.py runserver

8. **Create a new external database**
* Log into [ElephantSQL](https://www.elephantsql.com/) or create new account.
* Click to create new instance
* Set up the plan by giving it a name and select the tiny turtle plan (which is free)
* Select a region (data center) nearest to your location
* Click review, check that the details are correct and then click to create instance
* Return to ElephantSQL dashboard and click on the database instance name for the project
* Copy the ElephantSQL database URL using the copy icon. It begins with 'postgres://'

9. **Create the Heroku App**
* Log into [Heroku](https://www.heroku.com/) or create an account.
* Click to create new heroku app. Give the app an app name and select Europe as the region
* Open the app settings tab
* Click to reveal the config vars
* Add a config var called DATABASE_URL and paste in the ElephantSQL database URL

10. **Attach the database**
* In your code editor create a new env.py file on the top level of the project directory
* In the env.py file add import os at the top of the file
* Set environment variables inside the env file by adding - os.environ["DATABASE_URL"] = and then paste in the ElephantSQL database URL
* Set secret key variable inside the env file by adding - os.environ["SECRET_KEY"] = and then add your own secret key here
* In Heroku add the secret key variable value to the application config vars

11. **Prepare the environment and settings.py file**
* In settings.py reference and import the env.py by adding the following code to the file - 
from pathlib import Path
import os
import dj_database_url
if os.path.isfile("env.py"):
    import env
* Remove the hardcoded secret key and replace with links to the secret key variable in the env.py and in the heroku config vars by adding the following code - 
SECRET_KEY = os.environ.get('SECRET_KEY')
* Comment out the old DATABASES object variable and add a new databases variable by adding the following code - 
DATABASES = {
    'default':
    dj_database_url.parse(os.environ.get("DATABASE_URL"))
}

12. **Save all files and make migrations**
* In the terminal type python3 manage.py migrate
* Save all files

13. **Get static and media files stored on Cloudinary**
* Log in or sign up for an account on [Cloudinary](https://cloudinary.com/).
* Copy cloundinary URL API environment variable from Cloudinary dashboard
* Add cloudinary URL to env.py file by adding the following code - os.environ["CLOUDINARY_URL"] = and then paste in the Cloudinary URL
* In Heroku add in the Cloudinary URL into the application config vars on the app settings. The key should be CLOUDINARY_URL and the value should be the Cloudinary URL
* Add DISABLE_COLLECTSTATIC to Heroku config vars with a value of 1. This is a temporary step that will be removed on deployment
* Add Cloudinary libraries into installed apps in settings.py. To do this add the following code into the INSTALLED_APPS array variable - 'cloudinary_storage', 'cloudinary'. Cloudinary storage needs to be before django.contrib.staticfiles. Cloudinary needs to be after django.contrib.staticfiles.
* Tell Django to use Cloudinary to store media and static files by adding the following code into the settings.py file -
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/' 
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
* Link file to the templates directory in Heroku. Add the following code into the settings.py file under the BASE_DIR variable - 
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
* Change the templates directory to templates_dir. To do this add the following code inside the templates array variable -
'DIRS':[TEMPLATES_DIR],
* Add Heroku hostname to allowed_hosts by adding the following code into the allowed hosts variable - ["project_name.herokuapp.com", "localhost"] - project_name is the project name
* Create three new folders in top level of project directory - media, static and templates

14. **Create Procfile**
* Create a file called Procfile on the top level of the project directory
* Add the following code into the procfile - web: gunicorn project_name.wsgi - project_name is the project name
* Save all files

15. **Add, commit and push to repo**
* In the terminal type the following commands to push to the GitHub repo -
git add
git commit -m "Deployment commit"
git push

16. **Deploy the project to Heroku from the GitHub repo**
* On the Heroku project add another config var - the key should be PORT and the value should be 8000
* Under the project deploy tab, for the deployment method select GitHub. Search for the repository name and click connect. Once the project is connected scroll down to the manual deployment section and click deploy branch. Make sure you have the main branch selected

[Back to top](<#contents>)

# Credits

## Content

* Recipe content for Viva La Nacho was sourced from [BBC Good Food Mexican Recipes](https://www.bbcgoodfood.com/recipes/collection/mexican-recipes)

[Back to top](<#contents>)

## Media

* SVG icons for Viva La Nacho were obtained from [Font Awesome](https://fontawesome.com/)
* The Viva La Nacho hero image was downloaded from [iStock](https://www.istockphoto.com/)
* The accounts and featured recipe background images were downloaded from [Unsplash](https://unsplash.com/)
* Recipe images were obtained from recipes featured on [BBC Good Food Mexican Recipes](https://www.bbcgoodfood.com/recipes/collection/mexican-recipes)

[Back to top](<#contents>)

## Code 

* The ModifiedArrayField model class to return an array field with front-end checkboxes was sourced from [Rogulski.it](https://rogulski.it/django-multiselect-choice-admin/)
* [Django Docs](https://docs.djangoproject.com/en/4.1/) was used as an invaluable source of information on the Django framework.

[Back to top](<#contents>)

# Acknowledgements

The Viva La Nacho project was created as a portfolio project #4 for the Higher National Diploma in Full Stack Software Development at [Code Institute](https://codeinstitute.net/). This has certainly been the most challenging project so far, but I have learnt a lot from this experience and I am eternally grateful for the support I have had from my family, friends, work colleagues and fellow students. I would like to personally thank my Code Institute mentor [Precious Ijege](https://www.linkedin.com/in/precious-ijege-908a00168/) for all his help and guidance. Also a big thank you to the Code Institute tutors who helped me sort out some tricky bugs during development. I am very excited to move on to my final portfolio project with Code Institute and continuing my learning journey as a software developer.

Onwards and upwards!

Happy coding to all!

Matthew Hobbs-Hurrell

[Back to top](<#contents>)