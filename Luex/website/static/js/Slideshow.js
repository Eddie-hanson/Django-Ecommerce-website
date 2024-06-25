let images = document.querySelectorAll('.slideshow img'); 
let index = 0; 

function displayImages() {
  images[index].style.opacity = 1; 
  setTimeout(() => {
    images[index].style.opacity = 0;
    index = (index + 1) % images.length; 
    displayImages(); 
  }, 2000); // Set the delay to 2 seconds
}

displayImages(); 