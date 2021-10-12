let doc = document,  classifier = doc.querySelectorAll('.menu-classifier__item'),
    categories = doc.querySelectorAll('.menu-categories__category'), content = doc.querySelector('.content');

classifier.forEach(function (element) {
    element.addEventListener('click', function () {
        let item = this,
            category = doc.querySelector('.menu-categories__category[data-id="' + item.getAttribute('data-id') + '"]'),
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
        content.classList.add('content_inactive');

        if (!item.classList.contains('menu-classifier__item_active')){
            content.classList.remove('content_inactive');
            classifier.forEach(function (i) {
                i.classList.remove('menu-classifier__item_inactive');
            });

        }
        
        subCategories.forEach(function (subCategory) {
            subCategory.addEventListener('mouseover', function () {
                let item = this, sibling = item.nextElementSibling;

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
            })
        });

        subCategories.forEach(function (i) {
            i.classList.remove('menu-categories__side-item-title_active', 'menu-categories__side-item-title_inactive');
            i.nextElementSibling.classList.remove('menu-categories__dropdown_active');
        });
    })
});

