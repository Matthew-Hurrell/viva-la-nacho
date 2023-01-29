// Toggle Nav Icons
const nav_button = document.querySelector('#main-nav-mobile-button');
const burger_icon = nav_button.querySelector('.burger-menu');
const exit_icon = nav_button.querySelector('.exit-menu');
const mobile_menu = document.querySelector('.mobile-menu');

nav_button.addEventListener('click', () => {
    burger_icon.classList.toggle('hidden');
    exit_icon.classList.toggle('hidden');
    mobile_menu.classList.toggle('hidden');
})

// Cancel Buttons
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