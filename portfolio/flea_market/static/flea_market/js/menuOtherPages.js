let allSectionsButton = document.querySelector('.menu__activation-button'),
    menuClassifier = document.querySelector('.menu-classifier'), content = document.querySelector('.content'),
    menuClassifierItems = menuClassifier.querySelectorAll('.menu-classifier__item'),
    buttonDisplayForm = document.querySelector('.button-display-form');


allSectionsButton.addEventListener('click', function () {
    allSectionsButton.classList.toggle('menu__activation-button_active');
    if(allSectionsButton.classList.contains('menu__activation-button_active')){
        menuClassifier.classList.add('menu-classifier_active');
        content.classList.add('content_inactive');
    }else{
        menuClassifier.classList.remove('menu-classifier_active');
        content.classList.remove('content_inactive');
    }
});
menuClassifierItems.forEach(function (item) {
    item.addEventListener('click', function () {
        allSectionsButton.classList.toggle('menu__activation-button_display-none');
    });
});

buttonDisplayForm.addEventListener('click', function () {
    buttonDisplayForm.classList.toggle('button-display-form_active');
    form.classList.toggle('form_display');
});