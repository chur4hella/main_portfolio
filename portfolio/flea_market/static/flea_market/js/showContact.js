let contactButton = document.querySelector('.product__contact-button'),
    contactBlock = document.querySelector('.product__contact');

contactButton.addEventListener('click', function () {
    contactBlock.classList.toggle('product__contact_display');
    fake.classList.toggle('main__fake_active');
});

//доделат исчезнование окна