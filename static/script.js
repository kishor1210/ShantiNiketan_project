// Shanti Niketan - Custom JavaScript utilities

// Utility function to log messages
function log(message) {
  console.log(`[Shanti Niketan] ${message}`);
}

// Check if element is in viewport
function isInViewport(element) {
  const rect = element.getBoundingClientRect();
  return (
    rect.top >= 0 &&
    rect.left >= 0 &&
    rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
    rect.right <= (window.innerWidth || document.documentElement.clientWidth)
  );
}

// Lazy load images
function lazyLoadImages() {
  const images = document.querySelectorAll('img[data-src]');
  images.forEach(img => {
    if (isInViewport(img)) {
      img.src = img.dataset.src;
      img.removeAttribute('data-src');
    }
  });
}

// Smooth scroll to element
function smoothScrollTo(selector) {
  const element = document.querySelector(selector);
  if (element) {
    element.scrollIntoView({ behavior: 'smooth' });
  }
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
  log('Page loaded successfully');
  lazyLoadImages();
});

// Lazy load on scroll
window.addEventListener('scroll', lazyLoadImages);

// Export functions
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { log, isInViewport, lazyLoadImages, smoothScrollTo };
}
