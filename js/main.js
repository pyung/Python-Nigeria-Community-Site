/**
 * Main.js
 *
 * This is the primary js file used in our website.
 * All general / non-specific functionality should
 * go here.
 *
 * depends on: jquery
 */
$(document).load(function(){

// check if scroll event happened
$(window).scroll(function() {
	// check if user scrolled more than 550 from top of the browser window
	if ($(document).scrollTop() > 450) {
			$(".navbar-fixed-top").css("background-color", "#2aac2a")
			$(".navbar-default .navbar-nav > li > a ").css("color", "#fff")
   } else {
   // if not, change it back to transparent
		 	$(".navbar-fixed-top").css("background-color", "transparent")
		 	$(".navbar-default .navbar-nav > li > a").css("color", "#fff")
	 }
})
  
//navbar hamburger toggle
$(".navbar-toggle").on("click", function () {
	$(this).toggleClass("active")
})

});