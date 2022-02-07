let main = document.querySelector('.main'), mainFake = document.querySelector('.main__fake'),
    classifier = main.querySelectorAll('.menu-classifier__item'), infoButton = main.querySelector('.menu-head-info__button'),
    categories = main.querySelectorAll('.menu-categories__category'),
    menuHead = main.querySelector('.menu-head'), info = main.querySelector('.menu-head-info__content'),
    buttonClose = main.querySelector('.menu-head-info__content-close');


classifier.forEach(function (element) {
    element.addEventListener('click', function () {
        let item = this,
            category = main.querySelector('.menu-categories__category[data-id="' + item.getAttribute('data-id') + '"]'),
            subCategories = category.querySelectorAll('.menu-categories__side-item-title');

        classifier.forEach(function (i) {
            if (i != item){
                i.classList.remove('menu-classifier__item_active');
                i.classList.add('menu-classifier__item_inactive');
            }
        });

        categories.forEach(function (i) {
            if (i != category){
                i.classList.remove('menu-categories__category_active');
            }
        });

        item.classList.toggle('menu-classifier__item_active');
        category.classList.toggle('menu-categories__category_active');
        item.classList.remove('menu-classifier__item_inactive');

        if (!item.classList.contains('menu-classifier__item_active')){
            classifier.forEach(function (i) {
                i.classList.remove('menu-classifier__item_inactive');
            });
        }
        
        subCategories.forEach(function (subCategory) {
            subCategory.addEventListener('mouseover', function () {
                let item = this, sibling = item.nextElementSibling, widthWindow = window.innerWidth;

                if(widthWindow > 1000){
                    subCategories.forEach(function (i) {
                        if (i != item){
                            i.classList.add('menu-categories__side-item-title_inactive');
                            i.classList.remove('menu-categories__side-item-title_active');
                            i.nextElementSibling.classList.remove('menu-categories__dropdown_active');
                        }
                    });

                    item.classList.add('menu-categories__side-item-title_active');
                    item.classList.remove('menu-categories__side-item-title_inactive');
                    sibling.classList.add('menu-categories__dropdown_active');
                }
            });

            subCategory.addEventListener('click', function () {
                let item = this, sibling = item.nextElementSibling, widthWindow = window.innerWidth,
                    csf = main.querySelector('.menu-classifier');


                if(widthWindow <= 1000){
                    subCategories.forEach(function (i) {
                        if (i != item){
                            i.classList.add('menu-categories__side-item-title_inactive');
                            i.classList.remove('menu-categories__side-item-title_active');
                            i.nextElementSibling.classList.remove('menu-categories__dropdown_active');
                        }
                    });

                    csf.classList.toggle('menu-classifier_inactive');
                    item.classList.toggle('menu-categories__side-item-title_active');
                    item.classList.remove('menu-categories__side-item-title_inactive');
                    sibling.classList.add('menu-categories__dropdown_active');

                    if (!item.classList.contains('menu-categories__side-item-title_active')){
                        sibling.classList.remove('menu-categories__dropdown_active');
                        subCategories.forEach(function (i) {
                            i.classList.remove('menu-categories__side-item-title_inactive');
                        });
                    }
                }
            })
        });

        subCategories.forEach(function (i) {
            i.classList.remove('menu-categories__side-item-title_active', 'menu-categories__side-item-title_inactive');
            i.nextElementSibling.classList.remove('menu-categories__dropdown_active');
        });
    })
});
// to do click other area
// menuHead.addEventListener('click', function (e) {
//     main.querySelector('.menu-classifier').classList.remove('menu-classifier_inactive');
//     classifier.forEach(function (i) {
//         i.classList.remove('menu-classifier__item_active', 'menu-classifier__item_inactive')
//     });
//     content.classList.remove('content_inactive');
//     categories.forEach(function (i) {
//         i.classList.remove('menu-categories__category_active')
//     });
//     main.querySelectorAll('.menu-categories__side-item-title').forEach(function (i) {
//         i.classList.remove('menu-categories__side-item-title_inactive', 'menu-categories__side-item-title_active');
//         i.nextElementSibling.classList.remove('menu-categories__dropdown_active');
//     });
// });
// to do click other area

function closeInfo() {
    info.classList.remove('menu-head-info__content_active');
    mainFake.classList.remove('main__fake_active');
}

mainFake.addEventListener('click', closeInfo);

buttonClose.addEventListener('click', closeInfo);

infoButton.addEventListener('click', function () {
    info.classList.add('menu-head-info__content_active');
    mainFake.classList.add('main__fake_active');
});
