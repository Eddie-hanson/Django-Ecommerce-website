/*********** 
document.addEventListener("DOMContentLoaded", () => {
  const bigContainer = document.querySelector(".bigContainer");
  const controls = document.querySelectorAll(".control");
  const controlWidth = controls[0].offsetWidth + 40; // width + margin
  let currentPosition = 0;

  // Calculate the max position to stop at the last item before wrapping
  const maxPosition = -(controls.length - 1) * controlWidth;

  document.getElementById("left").addEventListener("click", () => {
    scrollLeft();
  });

  document.getElementById("right").addEventListener("click", () => {
    scrollRight();
  });

  function scrollLeft() {
    currentPosition += controlWidth;
    if (currentPosition > 0) {
      currentPosition = 0; // Stop at the first item
    }
    bigContainer.style.transform = `translateX(${currentPosition}px)`;
    updateButtonState();
  }

  function scrollRight() {
    currentPosition -= controlWidth;
    if (currentPosition < maxPosition) {
      currentPosition = maxPosition; // Stop at the last item
    }
    bigContainer.style.transform = `translateX(${currentPosition}px)`;
    updateButtonState();
  }

  function updateButtonState() {
    document.getElementById("left").disabled = currentPosition === 0;
    document.getElementById("right").disabled =
      currentPosition === maxPosition;
  }

  updateButtonState();
});*/

/***** 
document.addEventListener("DOMContentLoaded", () => {
  const bigContainer = document.querySelector(".bigContainer");
  const controls = document.querySelectorAll(".control");
  const controlWidth = controls[0].offsetWidth + 40; // width + margin
  const visibleCards = 4; // Number of cards to display at once
  let currentPosition = 0;

  document.getElementById("left").addEventListener("click", () => {
    scrollLeft();
  });

  document.getElementById("right").addEventListener("click", () => {
    scrollRight();
  });

  function scrollLeft() {
    currentPosition += controlWidth * visibleCards;
    if (currentPosition > 0) {
      currentPosition = -((controls.length - visibleCards) * controlWidth); // Wrap to the end
    }
    bigContainer.style.transform = `translateX(${currentPosition}px)`;
  }

  function scrollRight() {
    currentPosition -= controlWidth * visibleCards;
    if (currentPosition < -(controls.length - visibleCards) * controlWidth) {
      currentPosition = 0; // Wrap to the beginning
    }
    bigContainer.style.transform = `translateX(${currentPosition}px)`;
  }
}); */
/***** 
document.addEventListener("DOMContentLoaded", () => {
  const bigContainer = document.querySelector(".bigContainer");
  const controls = document.querySelectorAll(".control");
  const controlWidth = controls[0].offsetWidth + 40; // width + margin
  const visibleCards = getVisibleCards();
  let currentPosition = 0;

  // Set up event listeners for navigation buttons
  document.getElementById("left").addEventListener("click", scrollLeft);
  document.getElementById("right").addEventListener("click", scrollRight);

  // Update number of visible cards based on window resize
  window.addEventListener("resize", () => {
    currentPosition = 0;
    updateContainerPosition();
  });

  function scrollLeft() {
    currentPosition += controlWidth * visibleCards;
    if (currentPosition > 0) {
      currentPosition = -((controls.length - visibleCards) * controlWidth); // Loop to the end
    }
    updateContainerPosition();
  }

  function scrollRight() {
    currentPosition -= controlWidth * visibleCards;
    if (currentPosition < -(controls.length - visibleCards) * controlWidth) {
      currentPosition = 0; // Loop to the beginning
    }
    updateContainerPosition();
  }

  function getVisibleCards() {
    const screenWidth = window.innerWidth;
    if (screenWidth < 520) {
      return 1;
    } else if (screenWidth < 950) {
      return 2;
    } else {
      return 4;
    }
  }

  function updateContainerPosition() {
    bigContainer.style.transform = `translateX(${currentPosition}px)`;
  }
});*/

document.addEventListener("DOMContentLoaded", () => {
  const bigContainer = document.querySelector(".bigContainer");
  const controls = document.querySelectorAll(".control");
  let controlWidth = controls[0].offsetWidth + 40; // Card width + margin
  let visibleCards = 4; // Number of cards to display at once
  let currentPosition = 0;

  function updateControlWidth() {
    controlWidth = controls[0].offsetWidth + 40;
  }

  function scrollLeft() {
    currentPosition += controlWidth * visibleCards;
    if (currentPosition > 0) {
      currentPosition = -(controls.length - visibleCards) * controlWidth; // Loop to the end
    }
    bigContainer.style.transform = `translateX(${currentPosition}px)`;
  }

  function scrollRight() {
    currentPosition -= controlWidth * visibleCards;
    if (currentPosition < -(controls.length - visibleCards) * controlWidth) {
      currentPosition = 0; // Loop to the beginning
    }
    bigContainer.style.transform = `translateX(${currentPosition}px)`;
  }

  document.getElementById("left").addEventListener("click", scrollLeft);
  document.getElementById("right").addEventListener("click", scrollRight);

  window.addEventListener("resize", () => {
    updateControlWidth(); // Update control width on resize
    bigContainer.style.transition = "none"; // Disable transition during resize
    bigContainer.style.transform = "translateX(0px)"; // Reset position
    setTimeout(() => {
      bigContainer.style.transition = ""; // Re-enable transition
    }, 50);
  });

  // Initial setup
  updateControlWidth();
});
