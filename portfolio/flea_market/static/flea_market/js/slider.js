let imagesWrap = document.querySelector('.product__images-wrap'),
    arrowLeft = imagesWrap.querySelector('.product__image-arrow-left'),
    arrowRight = imagesWrap.querySelector('.product__image-arrow-right'),
    allImages = imagesWrap.querySelector('.product__images');


arrowLeft.addEventListener('click', function () {
    let image_display = allImages.querySelector('.product__image_display');
    image_display.classList.remove('product__image_display');
    if(image_display.previousElementSibling){
        image_display.previousElementSibling.classList.add('product__image_display');
    }else{
        allImages.lastElementChild.classList.add('product__image_display');
    }
});
arrowRight.addEventListener('click', function () {
    let image_display = allImages.querySelector('.product__image_display');
    image_display.classList.remove('product__image_display');
    if(image_display.nextElementSibling){
        image_display.nextElementSibling.classList.add('product__image_display');
    }else{
        allImages.firstElementChild.classList.add('product__image_display');
    }
});