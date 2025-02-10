// encontrar todas as imagens sem texto alternativo
// e deixa-las com uma borda vermelha
function process() {
    var images = document.getElementsByTagName('img');
    for (var i = 0; i < images.length; i++) {
        if (!images[i].alt) {
            images[i].style.border = '5px solid red';
        }
    }
}