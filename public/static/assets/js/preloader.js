// Wait for the window to load
window.onload = function() {
    const preloader = document.getElementById('preloader');
    const content = document.getElementById('content');

    // Set a timeout to hide the preloader after 2 seconds
    setTimeout(function() {
        // Fade out the preloader
        preloader.style.opacity = 0;

        // Wait for the fade-out to complete (0.5s) and then remove it from the DOM
        setTimeout(function() {
            preloader.style.display = 'none';  // Completely remove preloader
            content.classList.remove('hidden'); // Show the content
        }, 500); // 500ms corresponds to the CSS transition time
    }, 1000); // Time to display the preloader
};
