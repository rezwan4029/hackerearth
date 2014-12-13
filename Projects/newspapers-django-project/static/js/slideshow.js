//<![CDATA[
$(window).load(function () {
    $('#slider').nivoSlider({
        effect: 'slideInLeft', // Specify sets like: 'fold,fade,sliceDown'
        slices: 10,
        boxCols: 10, // For box animations
        boxRows: 5, // For box animations
        animSpeed: 1000, // Slide transition speed
        pauseTime: 4500, // How long each slide will show
        startSlide: 0, // Set starting Slide (0 index)
        directionNav: true, // Next & Prev navigation
        directionNavHide: true, // Only show on hover
        controlNav: true, // 1,2,3... navigation
        controlNavThumbs: true, // Use thumbnails for Control Nav
        controlNavThumbsFromRel: true, // Use image rel for thumbs
        pauseOnHover: true, // Stop animation while hovering
    });
});
//]]>


//featured slider
jQuery('#featured_slider').cycle({
    fx: 'scrollHorz',
    speed: 800,
    timeout: 0,
    easing: 'easeInOutQuint',
    next: '#featured_slider_next',
    prev: '#featured_slider_prev'
});
