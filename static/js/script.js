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
