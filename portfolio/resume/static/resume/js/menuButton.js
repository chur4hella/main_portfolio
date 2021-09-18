var menuButton = document.querySelector('.menu-button'),
    menu = document.querySelector('.menu');

menuButton.addEventListener('click', function () {
    this.classList.toggle('menu-button_active');
    menu.classList.toggle('menu_active');
});