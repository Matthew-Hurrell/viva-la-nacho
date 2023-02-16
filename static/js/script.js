// Toggle Nav Icons Functionality 
const nav_button = document.querySelector('#main-nav-mobile-button');
const burger_icon = nav_button.querySelector('.burger-menu');
const exit_icon = nav_button.querySelector('.exit-menu');
const mobile_menu = document.querySelector('.mobile-menu');

nav_button.addEventListener('click', () => {
    burger_icon.classList.toggle('hidden');
    exit_icon.classList.toggle('hidden');
    mobile_menu.classList.toggle('hidden');
})

// Cancel Button Functionality
if ( document.getElementsByClassName('cancel').length > 0 ) {
    const cancel_buttons = document.getElementsByClassName('cancel');
    const form = document.querySelector('.form-content');
    const pop_up = document.querySelector('.pop-up-confirmation');

    for (let button of cancel_buttons) {
        button.addEventListener('click', () => {
            form.classList.toggle('hidden');
            pop_up.classList.toggle('hidden');
        })
    }
}

// Recipe Delete Functionality
if ( document.getElementsByClassName('my-recipe-card-content').length > 0 ) {
    const my_recipe_cards = document.getElementsByClassName('my-recipe-card-content');
    
    for (let recipe of my_recipe_cards) {
        const recipe_text_content = recipe.querySelector('.recipe-text-content');
        const delete_recipe_notification = recipe.querySelector('.delete-recipe-notification');
        const delete_button = recipe_text_content.querySelector('.delete-button');
        const cancel_button = delete_recipe_notification.querySelector('.cancel-delete');

        delete_button.addEventListener('click', () => {
            recipe_text_content.classList.toggle('hidden');
            delete_recipe_notification.classList.toggle('hidden');
        })

        cancel_button.addEventListener('click', () => {
            recipe_text_content.classList.toggle('hidden');
            delete_recipe_notification.classList.toggle('hidden');
        })
    }
}

// Recipe Unlike Functionality
if ( document.getElementsByClassName('my-favourites-card-content').length > 0 ) {
    const my_favourites_cards = document.getElementsByClassName('my-favourites-card-content');
    
    for (let recipe of my_favourites_cards) {
        const recipe_text_content = recipe.querySelector('.recipe-text-content');
        const unlike_recipe_notification = recipe.querySelector('.unlike-recipe-notification');
        const unlike_button = recipe.querySelector('.unlike-button');
        const cancel_button = unlike_recipe_notification.querySelector('.cancel-unlike');

        unlike_button.addEventListener('click', () => {
            recipe_text_content.classList.toggle('hidden');
            unlike_recipe_notification.classList.toggle('hidden');
        })

        cancel_button.addEventListener('click', () => {
            recipe_text_content.classList.toggle('hidden');
            unlike_recipe_notification.classList.toggle('hidden');
        })
    }
}

// Recipe Unlike Notification Close Button
if ( document.getElementsByClassName('notification-close-button').length > 0 ) { 
    const close_button = document.querySelector('.notification-close-button');
    const notification = document.querySelector('.notification-message');

    close_button.addEventListener('click', () => {
        notification.classList.add('hidden');
    })

    setTimeout(function() {
        notification.classList.add('hidden');
    }, 5000);
}

// Form Validation
// if ( ( document.getElementsByClassName('post-recipe').length > 0 ) || ( document.getElementsByClassName('edit-recipe').length > 0 ) ) {
//     let recipe_form;

    // Assign recipe form variable to whatever form is being displayed
    // if ( document.getElementsByClassName('post-recipe').length > 0 ) {
    //     recipe_form = document.forms["post-recipe"];
    // } else if ( document.getElementsByClassName('edit-recipe').length > 0 ) {
    //     recipe_form = document.forms["edit-recipe"];
    // }

    // Click submit button function
    // function buttonclick(){
    //     let submit_button = document.querySelector(".recipe-submit-button");
    //     submit_button.click();
    // }

    // Strip HTML from summernote fields function
    // function stripHTML(html){
    //     let doc = new DOMParser().parseFromString(html, 'text/html');
    //     return doc.body.textContent || "";
    // }

    // Validate form function
//     function validateRecipeForm() {

//         let title = recipe_form["title"].value;
//         let category_checkboxes = document.querySelector('#div_id_category').querySelectorAll('input[type="checkbox"]:checked');
//         let prep_time = recipe_form["prep_time"].value;
//         let cooking_time = recipe_form["cooking_time"].value;
//         let serves = recipe_form["serves"].value;
//         let difficulty = recipe_form["difficulty"].value;
//         let excerpt = recipe_form["excerpt"].value;
//         let allergen_checkboxes = document.querySelector('#div_id_allergens').querySelectorAll('input[type="checkbox"]:checked');
//         let ingredients = recipe_form["ingredients"].value;
//         let method = recipe_form["method"].value;
//         let featured_image = recipe_form["featured_image"].value;
//         let featured_image_has_current = document.querySelector('#div_id_featured_image').getElementsByTagName('a');

//         if ( ( title.innerText == "" ) || ( title.trim().length == 0 ) ) {
//             alert("Form error - Title must be filled out");
//             return false;
//         }
//         if ( category_checkboxes.length == 0 ) {
//             alert("Form error - Please select a category");
//             return false;
//         }
//         if ( prep_time == "" ) {
//             alert("Form error - Prep time must be filled out");
//             return false;
//         }
//         if ( prep_time >= 600 ) {
//             alert("Form error - Prep time is too large");
//             return false;
//         }
//         if ( cooking_time == "" ) {
//             alert("Form error - Cooking time must be filled out");
//             return false;
//         }
//         if ( cooking_time >= 600 ) {
//             alert("Form error - Cooking time is too large");
//             return false;
//         }
//         if ( serves == "" ) {
//             alert("Form error - Serves must be filled out");
//             return false;
//         }
//         if ( serves > 10 ) {
//             alert("Form error - Serving is too large");
//             return false;
//         }
//         if ( difficulty == "" ) {
//             alert("Form error - Difficulty must be filled out");
//             return false;
//         }
//         if ( ( excerpt == "" ) || ( excerpt.trim().length == 0 ) ) {
//             alert("Form error - Excerpt must be filled out");
//             return false;
//         }
//         if ( excerpt.length >= 250 ) {
//             alert("Form error - Excerpt is too long. Limit is 250 characters");
//             return false;
//         }
//         if ( allergen_checkboxes.length == 0 ) {
//             alert("Form error - Please select an allergen, or select 'none' for no allergens");
//             return false;
//         }
//         if ( ( ingredients == "" ) || ( stripHTML(ingredients).trim().length == 0 ) ) {
//             alert("Form error - Ingredients must be filled out");
//             return false;
//         }
//         if ( ( method == "" ) || ( stripHTML(method).trim().length == 0 ) ) {
//             alert("Form error - Method must be filled out");
//             return false;
//         }
//         if ( ( featured_image_has_current.length == 0 ) && ( featured_image == "" ) ) {
//             alert("Form error - Please upload at least one image using the first image field");
//             return false;
//         }
//         if ( ! false ) {
//             buttonclick();
//         }
//     }
// }

// 

// Comment Form Validation

// if ( document.getElementsByClassName('comment-form').length > 0 ) {
//     let comment_form = document.forms["comment-form"];

    // Click submit button function
    // function buttonclick(){
    //     let submit_button = document.querySelector(".comment-submit-button");
    //     submit_button.click();
    // }

    // Validate form function
//     function validateCommentForm() {

//         let body = comment_form["body"].value;

//         if ( ( body.innerText == "" ) || ( body.trim().length == 0 ) ) {
//             alert("Form error - Comment body must be filled out");
//             return false;
//         }
//         if ( ! false ) {
//             buttonclick();
//         }
//     }
// }

// Recipe Form Validation

if ( ( document.getElementsByClassName('post-recipe').length > 0 ) || ( document.getElementsByClassName('edit-recipe').length > 0 ) ) {

    let form;

    // Assign recipe form variable to whatever form is being displayed
    if ( document.getElementsByClassName('post-recipe').length > 0 ) {
        form = document.forms["post-recipe"];
    } else if ( document.getElementsByClassName('edit-recipe').length > 0 ) {
        form = document.forms["edit-recipe"];
    }


    function stripHTML(html){
        let doc = new DOMParser().parseFromString(html, 'text/html');
        return doc.body.textContent || "";
    }

    form.addEventListener('submit', event => {

        let title = form["title"].value;
        let category_checkboxes = document.getElementById('div_id_category').querySelectorAll('input[type="checkbox"]:checked');
        let prep_time = form["prep_time"].value;
        let cooking_time = form["cooking_time"].value;
        let serves = form["serves"].value;
        let difficulty = form["difficulty"].value;
        let excerpt = form["excerpt"].value;
        let allergen_checkboxes = document.querySelector('#div_id_allergens').querySelectorAll('input[type="checkbox"]:checked');
        let ingredients = form["ingredients"].value;
        let method = form["method"].value;
        let featured_image = form["featured_image"].value;
        let featured_image_has_current = document.querySelector('#div_id_featured_image').getElementsByTagName('a');

        if ( ( title == "" ) || ( title.trim().length == 0 ) ) {
            event.preventDefault();
            alert('Form error - Please enter a valid title.');
        }
        else if ( category_checkboxes.length == 0 ) {
            event.preventDefault();
            alert("Form error - Please select a category");
        }
        else if ( prep_time == "" ) {
            event.preventDefault();
            alert("Form error - Prep time must be filled out");
        }
        else if ( prep_time >= 600 ) {
            event.preventDefault();
            alert("Form error - Prep time is too large");
        }
        else if ( cooking_time == "" ) {
            event.preventDefault();
            alert("Form error - Cooking time must be filled out");
        }
        else if ( cooking_time >= 600 ) {
            event.preventDefault();
            alert("Form error - Cooking time is too large");
        }
        else if ( serves == "" ) {
            event.preventDefault();
            alert("Form error - Serves must be filled out");
        }
        else if ( serves > 10 ) {
            event.preventDefault();
            alert("Form error - Serving is too large");
        }
        else if ( difficulty == "" ) {
            event.preventDefault();
            alert("Form error - Difficulty must be filled out");
        }
        else if ( ( excerpt == "" ) || ( excerpt.trim().length == 0 ) ) {
            event.preventDefault();
            alert("Form error - Excerpt must be filled out");
        }
        else if ( excerpt.length >= 250 ) {
            event.preventDefault();
            alert("Form error - Excerpt is too long. Limit is 250 characters");
        }
        else if ( allergen_checkboxes.length == 0 ) {
            event.preventDefault();
            alert("Form error - Please select an allergen, or select 'none' for no allergens");
        }
        else if ( ( ingredients == "" ) || ( stripHTML(ingredients).trim().length == 0 ) ) {
            event.preventDefault();
            alert("Form error - Ingredients must be filled out");
        }
        else if ( ( method == "" ) || ( stripHTML(method).trim().length == 0 ) ) {
            event.preventDefault();
            alert("Form error - Method must be filled out");
        }
        else if ( ( featured_image_has_current.length == 0 ) && ( featured_image == "" ) ) {
            event.preventDefault();
            alert("Form error - Please upload at least one image using the first image field");
        }
    });
}