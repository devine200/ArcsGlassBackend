$('.carousel-item').slick({
    infinite: true,
    speed: 500,
    autoplay: true,
});

const video = document.getElementById('myVideo');
const playButton = document.getElementById('playButton');

// Function to toggle video play and pause
function togglePlay() {
  if (video.paused || video.ended) {
    video.play();
  } else {
    video.pause();
  }
}

// Show play button when the video is paused
video.addEventListener('pause', () => {
  playButton.style.display = 'block';
});

// Hide play button when the video is playing
video.addEventListener('play', () => {
  playButton.style.display = 'none';
});

// Hide play button when the video ends
video.addEventListener('ended', () => {
  playButton.style.display = 'block';
});
