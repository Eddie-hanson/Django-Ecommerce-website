// const bigContainer = document.querySelector('.bigContainer');
// let counter = 0;

// function left() {
//     if (counter === 0) {
//         counter = bigContainer.children.length - 1;
//     } else {
//         counter--;
//     }
//     scroll();
// }

// function right() {
//     if (counter === bigContainer.children.length - 1) {
//         counter = 0;
//     } else {
//         counter++;
//     }
//     scroll();
// }

// function scroll() {
//     const itemWidth = bigContainer.children[0].clientWidth;
//     bigContainer.style.transform = `translateX(-${counter * itemWidth}px)`;
// }

var swiper = new Swiper(".bigContainerWrapper", {
  slidesPerView: 3,
  spaceBetween: 25,
  loop: true,
  centerSlide: "true",
  fade: "true",
  grabCursor: "true",
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
    dynamicBullets: true,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  breakpoints: {
    0: {
      slidesPerView: 1,
    },
    520: {
      slidesPerView: 2,
    },
    950: {
      slidesPerView: 3,
    },
  },
});
