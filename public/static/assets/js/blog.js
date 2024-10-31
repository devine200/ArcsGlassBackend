// Custom Cursor
$("a:not(.grid-img, .hero__img-wrap)").on("mouseenter", function () {
    $(".cursor__dot").addClass("cc-large");
});
$("a").on("mouseleave", function () {
    $(".cursor__dot").removeClass("cc-large");
});
$(".grid-img").on("mouseenter", function () {
    $(".cursor__dot").addClass("cc-project");
});
$(".grid-img").on("mouseleave", function () {
    $(".cursor__dot").removeClass("cc-project");
});
$(".swiper-slide").on("mouseenter", function () {
    $(".cursor__dot").addClass("cc-larger");
});
$(".swiper-slide").on("mouseleave", function () {
    $(".cursor__dot").removeClass("cc-larger");
});
$(".slider-btn").on("mouseenter", function () {
    $(".cursor").addClass("cc-slider");
});
$(".slider-btn").on("mouseleave", function () {
    $(".cursor").removeClass("cc-slider");
});
$(".swiper-next")
    .on("mouseenter", function () {
        $(".cursor__dot, .cursor__next").addClass("cc-slider");
    })
    .on("mouseleave", function () {
        $(".cursor__dot, .cursor__next").removeClass("cc-slider");
    });
$(".swiper-prev")
    .on("mouseenter", function () {
        $(".cursor__dot, .cursor__prev").addClass("cc-slider");
    })
    .on("mouseleave", function () {
        $(".cursor__dot, .cursor__prev").removeClass("cc-slider");
    });
// LENIS SMOOTH SCROLL
let lenis;
if (Webflow.env("editor") === undefined) {
    lenis = new Lenis({
        lerp: 0.1,
        wheelMultiplier: 0.9,
        gestureOrientation: "vertical",
        normalizeWheel: false,
        smoothTouch: false
    });
    function raf(time) {
        lenis.raf(time);
        requestAnimationFrame(raf);
    }
    requestAnimationFrame(raf);
}
$("[data-lenis-start]").on("click", function () {
    lenis.start();
});
$("[data-lenis-stop]").on("click", function () {
    lenis.stop();
});
$("[data-lenis-toggle]").on("click", function () {
    $(this).toggleClass("stop-scroll");
    if ($(this).hasClass("stop-scroll")) {
        lenis.stop();
    } else {
        lenis.start();
    }
});


const swiper = new Swiper(".swiper.cc-main", {
    // Optional parameters
    direction: "vertical",
    loop: true,
    mousewheel: true,
    keyboard: true,
    followfinger: false,
    speed: 800,
    parallex: true
});
function setText() {
    $(".swiper-text").css("transform", "translateY(100%)");
    $(".swiper-text").css("opacity", "0");
}
//When scrolling down
swiper.on("slideNextTransitionStart", function (e) {
    setText();
    //Text Leaving
    let outgoingText = $(".h-text_item").eq(e.previousIndex - 1);
    gsap.fromTo(
        outgoingText.find(".swiper-text"),
        { y: "0%" },
        { y: "-100%", duration: 0.4, ease: "cubic.out" }
    );
    gsap.fromTo(
        outgoingText.find(".swiper-text"),
        { opacity: 1 },
        { opacity: 0, duration: 0.4 }
    );
    //Text Entering
    let incomingText = $(" .h-text_item").eq(e.realIndex);
    gsap.fromTo(
        incomingText.find(".swiper-text"),
        { y: "100%" },
        { y: "0%", duration: 0.4, delay: 0.6, ease: "cubic.out" }
    );
    gsap.fromTo(
        incomingText.find(".swiper-text"),
        { opacity: 0 },
        { opacity: 1, duration: 0.4, delay: 0.6 }
    );
});
//When scrolling up
swiper.on("slidePrevTransitionStart", function (e) {
    setText();
    //Text Leaving
    let outgoingText = $(" .h-text_item").eq(e.activeIndex);
    gsap.fromTo(
        outgoingText.find(".swiper-text"),
        { y: "0%" },
        { y: "100%", duration: 0.4 }
    );
    gsap.fromTo(
        outgoingText.find(".swiper-text"),
        { opacity: 1 },
        { opacity: 0, duration: 0.4 }
    );
    //Text Entering
    let incomingText = $(" .h-text_item").eq(e.realIndex);
    gsap.fromTo(
        incomingText.find(".swiper-text"),
        { y: "-100%" },
        { y: "0%", duration: 0.4, delay: 0.6 }
    );
    gsap.fromTo(
        incomingText.find(".swiper-text"),
        { opacity: 0 },
        { opacity: 1, duration: 0.4, delay: 0.6 }
    );
});
// Display number for total slide count
let slideLength = swiper.slides.length - 2;
$(".total").text(("0" + slideLength).slice(-2));
// Update current slide number to display
swiper.on("transitionStart", function (e) {
    let activeNumer = +e.realIndex + 1;
    $(".current").text(("0" + activeNumer).slice(-2));
});


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


