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
});
