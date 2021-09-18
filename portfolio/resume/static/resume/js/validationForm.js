var email = document.querySelector('input[name=email]'),
    message = document.querySelector('textarea[name=message]');

email.addEventListener('input', function () {
    var reg = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
    if (reg.test(this.value)){
        this.classList.remove('form__field_required');
    }else {
        this.classList.add('form__field_required');
    }
});
message.addEventListener('input', function () {
    if (this.value){
        this.classList.remove('form__field_required');
    }else {
        this.classList.add('form__field_required');
    }
});