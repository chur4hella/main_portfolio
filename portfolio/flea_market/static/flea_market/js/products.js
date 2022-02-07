//filter and pagination
let form = document.querySelector('.form'), inputs = form.querySelectorAll('input'),
    types = form.querySelectorAll('#id_type_ad input'), orderBlock = document.querySelector('.content-order'),
    orderField = orderBlock.querySelector('.content-order__selected'),
    orderDropdown = orderBlock.querySelector('.content-order-dropdown'),
    orderItems = orderBlock.querySelectorAll('.content-order-dropdown__item');


form.querySelector('#id_type_ad input').removeAttribute('checked');
types.forEach(function (i){
    i.addEventListener('change', function () {
        i.parentNode.classList.toggle('label_active');
    })
});

let searchParams = new URLSearchParams(document.location.search);

for(let param of searchParams.keys()){
    if(param == 'price_from'){
        form.querySelector('input[name=price_from]').value = searchParams.get(param);
    }else if(param == 'price_to'){
        form.querySelector('input[name=price_to]').value = searchParams.get(param);
    }else if(param == 'type_ad'){
        for(let typeAd of searchParams.getAll(param)){
            let inputType = form.querySelector('input[name=' + param + '][value=' + typeAd + ']');

            inputType.checked = true;
            inputType.parentNode.classList.add('label_active');
        }
    }else if(param == 'bargain'){
        form.querySelector('input[name=' + param + ']').checked = true;
    }
}

function ajaxRequest(url) {
    let httpRequest = new XMLHttpRequest();
    httpRequest.onload = function () {
            if(httpRequest.status == 200){
                let response = httpRequest.response, contentCol = document.querySelector('.content-col-items');

                contentCol.innerText = '';
                contentCol.insertAdjacentHTML('afterbegin', response['html']);
                pagination();
            }
        };

        httpRequest.open('GET', url);
        httpRequest.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
        httpRequest.responseType = 'json';
        httpRequest.send();
}

function pagination() {
    let pageButtons = document.querySelectorAll('.pagination__steps-link');

    pageButtons.forEach(function (pageButton) {
    pageButton.addEventListener('click', function (e) {
        e.preventDefault();
        let newUrl = pageButton.getAttribute('href'),
            searchParams = new URLSearchParams(document.location.search);

        searchParams.delete('page');
        newUrl += '&' + searchParams;
        history.pushState(null, null, newUrl);

        ajaxRequest(newUrl);
    })
});
}

for(let input of inputs){
    input.addEventListener('change', function () {
        let newUrl = document.location.pathname,
            newParams = new URLSearchParams();

        inputs.forEach(function (item) {
                if ((item.getAttribute('type') != 'checkbox' && item.value) || item.checked){
                    newParams.append(item.getAttribute('name'), item.value);
                }
            });

        newUrl += '?' + newParams;
        history.pushState(null, null, newUrl);

        ajaxRequest(newUrl);
    })
}

pagination();

orderField.innerText = document.querySelector('.content-order-dropdown__item_active').innerText;
orderField.addEventListener('click', function () {
    orderDropdown.classList.toggle('content-order-dropdown_active');
});

for(let orderItem of orderItems){
    orderItem.addEventListener('click', function () {
        let newUrl = document.location.pathname, newParams = new URLSearchParams(document.location.search);
        console.log(orderItem.getAttribute('data-order'));
        newParams.append('order', orderItem.getAttribute('data-order'));
        newUrl += '?' + newParams;
        history.pushState(null, null, newUrl);

        ajaxRequest(newUrl);

        orderDropdown.querySelector('.content-order-dropdown__item_active').classList.remove('content-order-dropdown__item_active');
        orderItem.classList.add('content-order-dropdown__item_active');
        orderField.innerText = orderItem.innerText;
        orderDropdown.classList.remove('content-order-dropdown_active');

    })
}

// сделать ajax переход к product
// window.addEventListener('popstate', function () {
//     console.log(document.location.href);
// });
//to do доделать отображение активного select сортировки после перезагрузки страны, как в случае с элементами фильтра



// bookmark
function bookmarkAction() {
    let bookmark = document.querySelector('.content-col-item__bookmark');
    console.log(bookmark.getAttribute('data-bookmark-saved'));
    console.log(document.querySelector('input[name=csrfmiddlewaretoken]').value);

    bookmark.addEventListener('click', function () {
        let url = new URL('http://127.0.0.1:8000/flea_market/profile/bookmark-create'), request = new XMLHttpRequest(), data={
            'id_product': bookmark.getAttribute('data-id-product'),
            'created': bookmark.getAttribute('data-bookmark-saved')
        };

        request.onload = function () {
            if (request.status == 200){
                let response = request.response;

                console.log(response);
            }
        };

            request.open('POST', url);
            request.setRequestHeader('X-CSRFToken', document.querySelector('input[name=csrfmiddlewaretoken]').value);
            request.setRequestHeader('X-Requested-With', 'XMLHttpRequest');

            request.responseType = 'json';
            request.send(data);
    });
}

bookmarkAction();