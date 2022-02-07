let imageLinks = document.querySelectorAll('.content-col-item__image-wrap'),
    titleLinks = document.querySelectorAll('.content-col-item__title');

for(let link of imageLinks){
    link.addEventListener('click', function (e) {
        e.preventDefault();
        console.log(link);
    });
}
for(let link of titleLinks){
    link.addEventListener('click', function (e) {
        e.preventDefault();
        console.log(link);
    });
}