let types = document.querySelectorAll('#id_type_ad label');


for (let type of types){
    if(type.querySelector('input').hasAttribute('checked')){
        type.classList.add('label_active')
    }
    type.addEventListener('click', function () {
        types.forEach(function (i) {
            i.classList.remove('label_active')
        });
        type.classList.add('label_active')
    })
}