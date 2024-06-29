// Add sticky and animation classes to the header on scroll
window.addEventListener('scroll', function () {
  var header = document.querySelector('.sticky-header');
  var headerHeight = header.offsetHeight;
  var scrollTop = window.pageYOffset;

  if (scrollTop >= 100) {
    header.classList.add('sticky');
    header.classList.add('animate');
  } else {
    header.classList.remove('sticky');
    header.classList.remove('animate');
  }
});


// Show/hide scroll-to-top button on scroll
window.addEventListener('scroll', function () {
  var scrollToTop = document.querySelector('.scroll-to-top');
  if (window.pageYOffset > 200) {
    scrollToTop.classList.add('show');
  } else {
    scrollToTop.classList.remove('show');
  }
});

// Scroll to top on click of scroll-to-top button
document.querySelector('.scroll-to-top').addEventListener('click', function () {
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  });
});


var swiper = new Swiper(".bannerSwiper", {
  spaceBetween: 30,
  centeredSlides: true,
  autoplay: {
    delay: 2500,
    disableOnInteraction: false,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
});


var swiper = new Swiper(".campaignSwiper", {
  slidesPerView: 1,
  spaceBetween: 10,
  // autoplay: {
  //   delay: 2500,
  //   disableOnInteraction: false,
  // },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },

  breakpoints: {
    320: {
      slidesPerView: 1,
      spaceBetween: 10,
    },
    576: { 
      slidesPerView: 2,
      spaceBetween: 10,
    },
    768: { 
      slidesPerView: 2,
      spaceBetween: 20,
    },
    992: {
      slidesPerView: 3,
      spaceBetween: 20,
    },
    1200: {
      slidesPerView: 3,
      spaceBetween: 20,
    },
  },

});


var swiper = new Swiper(".testimonialsSwiper", {
  slidesPerView: 4,
  spaceBetween: 10,
  autoplay: {
    delay: 2500,
    disableOnInteraction: false,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  breakpoints: {
    320: {
      slidesPerView: 1,
      spaceBetween: 10,
    },
    450: { 
      slidesPerView: 2,
      spaceBetween: 10,
    },
    768: { 
      slidesPerView: 3,
      spaceBetween: 20,
    },
    992: {
      slidesPerView: 4,
      spaceBetween: 20,
    },
    1200: {
      slidesPerView: 4,
      spaceBetween: 20,
    },
  },

});


var swiper = new Swiper(".heavenCowSwiper", {
  slidesPerView: 3.7, 
  spaceBetween: 10,
  autoplay: {
    delay: 2500,
    disableOnInteraction: false,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  breakpoints: {
    320: {
      slidesPerView: 1,
      spaceBetween: 10,
    },
    576: { 
      slidesPerView: 1.7,
      spaceBetween: 10,
    },
    768: { 
      slidesPerView: 2,
      spaceBetween: 20,
    },
    992: {
      slidesPerView: 3.7,
      spaceBetween: 20,
    },
    1200: {
      slidesPerView: 3.7,
      spaceBetween: 20,
    },
  },
});



var swiper = new Swiper(".sustainableSwiper", {
  slidesPerView: 3.7, 
  spaceBetween: 10,
  autoplay: {
    delay: 2500,
    disableOnInteraction: false,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  breakpoints: {
    320: {
      slidesPerView: 1,
      spaceBetween: 10,
    },
    576: { 
      slidesPerView: 1.7,
      spaceBetween: 10,
    },
    768: { 
      slidesPerView: 2,
      spaceBetween: 20,
    },
    992: {
      slidesPerView: 3.7,
      spaceBetween: 20,
    },
    1200: {
      slidesPerView: 3.7,
      spaceBetween: 20,
    },
  },
});


var swiper = new Swiper(".trusteeSwiper", {
  slidesPerView: 3,
  spaceBetween: 10,
  autoplay: {
    delay: 2500,
    disableOnInteraction: false,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  breakpoints: {
    320: {
      slidesPerView: 1,
      spaceBetween: 10,
    },
    480: { 
      slidesPerView: 2,
      spaceBetween: 10,
    },
    600: { 
      slidesPerView: 3,
      spaceBetween: 10,
    },
    768: { 
      slidesPerView: 3,
      spaceBetween: 20,
    },
    992: {
      slidesPerView: 3,
      spaceBetween: 20,
    },
    1200: {
      slidesPerView: 3,
      spaceBetween: 20,
    },
  },
});


var swiper = new Swiper(".factSwiper", {
  autoplay: {
    delay: 2500,
    disableOnInteraction: false,
  },
  pagination: {
    el: ".swiper-pagination",
  },
});


var swiper = new Swiper(".objectiveCowSwiper", {
  slidesPerView: 3.7, 
  spaceBetween: 10,
  autoplay: {
    delay: 2500,
    disableOnInteraction: false,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  breakpoints: {
    320: {
      slidesPerView: 1,
      spaceBetween: 10,
    },
    576: { 
      slidesPerView: 1.7,
      spaceBetween: 10,
    },
    768: { 
      slidesPerView: 2,
      spaceBetween: 20,
    },
    992: {
      slidesPerView: 3.7,
      spaceBetween: 20,
    },
    1200: {
      slidesPerView: 3.7,
      spaceBetween: 25,
    },
  },
});


// Event Box
document.addEventListener("DOMContentLoaded", function() {
  const eventBoxes = document.querySelectorAll('.eventBox');
  eventBoxes[0].classList.add('active');
  eventBoxes[0].querySelector('.eventCheckbox').checked = true; 
});

function selectEvent(selectedElement) {
  const eventBoxes = document.querySelectorAll('.eventBox');
  
  eventBoxes.forEach(box => {
      if (box === selectedElement) {
          box.classList.add('active');
          box.querySelector('.eventCheckbox').checked = true;
      } else {
          box.classList.remove('active');
          box.querySelector('.eventCheckbox').checked = false;
      }
  });
}


document.addEventListener('DOMContentLoaded', function () {
  var swiper = new Swiper(".gallerySwiper", {
    effect: "cards",
    grabCursor: true,
    autoplay: {
      delay: 2500,
      disableOnInteraction: false,
    },
  });

  // Add click event listener to each Swiper slide
  document.querySelectorAll('.swiper-slide').forEach(function(slide) {
    slide.addEventListener('click', function() {
      if (swiper.isEnd) {
        swiper.slideTo(0);
      } else {
        swiper.slideNext();
      }
    });
  });
});




  var swiper = new Swiper(".CSRSwiper", {
    spaceBetween: 10,
    slidesPerView: 9,
    freeMode: true,
    watchSlidesProgress: true,
  });
  var swiper2 = new Swiper(".CSRSwiper2", {
    spaceBetween: 10,
      autoplay: {
      delay: 2500,
      disableOnInteraction: false,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    thumbs: {
      swiper: swiper,
    },
  });



  document.addEventListener('DOMContentLoaded', () => {
    const indianBtn = document.getElementById('indian-btn');
    const nonIndianBtn = document.getElementById('non-indian-btn');
    
    const buttons = document.querySelectorAll('.countryBtn');

    buttons.forEach(button => {
        button.addEventListener('click', () => {
            buttons.forEach(btn => btn.classList.remove('active')); // Remove active class from all buttons
            button.classList.add('active'); // Add active class to the clicked button
        });
    });

    // Set initial active button
    indianBtn.classList.add('active');
});




// Quantity

document.addEventListener('DOMContentLoaded', () => {
  const cardDonateSections = document.querySelectorAll('.card_donate');

  cardDonateSections.forEach((cardDonate) => {
      const addButton = cardDonate.querySelector('.add-button');
      const buttonContainer = cardDonate.querySelector('.add_button');
      const quantityContainer = cardDonate.querySelector('.quantity-container');
      const quantityValue = cardDonate.querySelector('.quantity-value');
      const enterButton = cardDonate.querySelector('.enter-button');
      const addedButton = cardDonate.querySelector('.added-button');

      let quantity = 0;

      addButton.addEventListener('click', () => {
          buttonContainer.style.display = 'none';
          quantityContainer.style.display = 'flex';
      });

      enterButton.addEventListener('click', () => {
          if (quantity > 0) {
              // Hide quantity container
              quantityContainer.style.display = 'none';
              // Show added button
              addedButton.style.display = 'inline-flex';
          }
      });

      const decrementBtn = cardDonate.querySelector('.decrement-btn');
      const incrementBtn = cardDonate.querySelector('.increment-btn');

      decrementBtn.addEventListener('click', () => {
          if (quantity > 0) {
              quantity--;
              quantityValue.textContent = quantity;
          }
      });

      incrementBtn.addEventListener('click', () => {
          quantity++;
          quantityValue.textContent = quantity;
      });
  });
});



