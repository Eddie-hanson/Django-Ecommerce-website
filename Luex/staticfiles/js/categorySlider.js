document.addEventListener("DOMContentLoaded", function () {
  var swiper = new Swiper(".swiper", {
    // Optional parameters
    direction: "horizontal",
    loop: true,
    slidesPerView: 5,
    spaceBetween: 5,
    centerSlide: "true",
    fade: "true",
    grabCursor: "true",

    // If we need pagination
    pagination: {
      el: ".swiper-pagination",
    },

    // Navigation arrows
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  });
});
