const bigContainer = document.querySelector('.bigContainer');
let counter = 0;

function left() {
    if (counter === 0) {
        counter = bigContainer.children.length - 1;
    } else {
        counter--;
    }
    scroll();
}

function right() {
    if (counter === bigContainer.children.length - 1) {
        counter = 0;
    } else {
        counter++;
    }
    scroll();
}

function scroll() {
    const itemWidth = bigContainer.children[0].clientWidth;
    bigContainer.style.transform = `translateX(-${counter * itemWidth}px)`;
}
