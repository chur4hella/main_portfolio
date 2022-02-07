let imageField = document.querySelector('#id_photo'), label = document.querySelector('label[for="id_photo"]');

label.innerText = 'Нажмите, чтобы выбрать фотографии';
imageField.addEventListener('change', function () {
    label.innerText = 'Выбрано фото: ' + imageField.files.length;
});