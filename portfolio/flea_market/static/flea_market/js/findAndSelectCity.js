let city = document.querySelector('.form__row-city'),
    help = document.querySelector('.form__row-help');


city.addEventListener('input', function () {
    if(city.value.length > 0) {
        let url = document.location.pathname + '?city=' + city.value, httpRequest = new XMLHttpRequest();

        help.innerText = '';
        httpRequest.onload = function () {
            if (httpRequest.status == 200){
                let response = httpRequest.response;

                for (let text of response){
                    let helpItem = document.createElement('li');

                    helpItem.className = 'form__row-help-item';
                    helpItem.innerText = text;
                    helpItem.addEventListener('click', function () {
                        city.value = helpItem.innerText.split(', ')[0];
                        help.innerText = '';
                    });
                    help.append(helpItem);
                }
            }
        };

        httpRequest.open('GET', url);
        httpRequest.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
        httpRequest.responseType = 'json';
        httpRequest.send();
    }else{
        help.innerText = '';
    }
});