let blockSearch = document.querySelector('.menu-head__search'),
    fieldSearch = blockSearch.querySelector('.menu-head__search-field'),
    itemsBlockSearch = blockSearch.querySelector('.menu-head__search-items'),
    fake = document.querySelector('.main__fake');

fieldSearch.addEventListener('input', function () {
    if(fieldSearch.value){
        let url = '/flea_market/search/?title=' + fieldSearch.value, httpRequest = new XMLHttpRequest();


        httpRequest.onload = function () {
            if(httpRequest.status == 200){
                let response = httpRequest.response;

                itemsBlockSearch.innerText = '';
                itemsBlockSearch.insertAdjacentHTML('afterbegin', response['html']);
            }
        };

        httpRequest.open('GET', url);
        httpRequest.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
        httpRequest.responseType = 'json';
        httpRequest.send();

        blockSearch.classList.add('menu-head__search_active');
        fake.classList.add('main__fake_active');
    }else{
        itemsBlockSearch.innerText = '';
        blockSearch.classList.remove('menu-head__search_active');
        fake.classList.remove('main__fake_active');
    }
});