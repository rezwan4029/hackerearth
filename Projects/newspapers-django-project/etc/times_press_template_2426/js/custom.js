jQuery(document).ready(function() {

//Notification bar
	$(".btn-slide").click(function(){
	  $("#panel").slideToggle(1000);
	  $(this).toggleClass("active");
	});


//Dropdown menu
        $('ul.sf-menu').superfish({ 
            delay:       500,                            // one second delay on mouseout 
            animation:   {opacity:'show',height:'show'},  // fade-in and slide-down animation 
            speed:       'fast',                          // faster animation speed 
            autoArrows:  true,                           // disable generation of arrow mark-up 
            dropShadows: false                            // disable drop shadows 
        }); 
		
// Tabbed widget
$(document).ready(function() {
  $("#tabs").tabs({ fx: { opacity: 'toggle'}, selected: 0 });
});
		
//Social sharing buttons fading effect
$(".social_sharing_post a").hover(function() {
	    $(this).stop().animate({  opacity: ".7",color:"#2387D9" }, 400);
},function() {
    $(this).stop().animate({ opacity: "1",color:"#333333" }, 400);
});


// Categories menu link hover effect
$(".sf-menu li a").hover(function() {
	    $(this).stop().animate({  color: "#2594EF" }, 200);
},function() {
    $(this).stop().animate({ color: "#717171" }, 200);
});


//Featured slider arrows
	jQuery('#featured').not('#featured .nav_controls').hover( 
		function () {
			jQuery('#featured .nav_controls').stop().show().animate({ opacity: 1 },200);
		}, function () {
			jQuery('#featured .nav_controls').stop().animate({ opacity: 0 },200, function() {
				jQuery(this).hide();
			});
		}
	);
	 	
// Image border Fading effect in content
    $(".entry-content img").hover(function() {
    $(this).stop().animate({ backgroundColor: "#2594EF" }, 1400);
},function() {
    $(this).stop().animate({ backgroundColor: "#fff" }, 800);
});

// INPUT BORDER
	// Input focus
	jQuery('#respond input,#respond textarea').focus( 
		function () {
			jQuery(this).css('border', '1px solid #2594EF');
			jQuery(this).css('color', '#444444');
		}
	);
	// Input blur
	jQuery('#respond input,#respond textarea').blur( 
		function () {
			jQuery(this).css({
				border: '1px solid #cccccc',
				color: '#999999'
			});
		}
	);

//Scroll to top
	$('#Scroll a').click(function(){
		$('html, body').animate({scrollTop: '0px'}, 1000);
		return false;
	});


// Categories shadow effect
$(".tab-tags a").hover(function() {
	    $(this).stop().animate({  boxShadow: "1px 1px 1px 0 #D1D1D1" }, 100);
},function() {
    $(this).stop().animate({ boxShadow: "4px 4px 0 -2px #D4D4D4" }, 100);
});

// Footer Link hover effect
    $("#footer_inner a").hover(function() {
    $(this).stop().animate({ color: "#2387D9" }, 300);
},function() {
    $(this).stop().animate({ color: "#333333" }, 300);
});

//Enable n-th childs
$("#featured .column:nth-child(6n-1)").css("margin-right", "0");

$(".post_double:nth-child(2n)").css("margin-right", "35px");


}); 