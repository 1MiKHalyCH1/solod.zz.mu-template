function scrollTop() {
	$('#scroll-area').fadeOut();	
	$(window).scroll(function() {
		if($(this).scrollTop() > 50) { 
			$('#scroll-area').fadeIn(); 
		} 
		else { 
			$('#scroll-area').fadeOut();
	 	}
   	});
   	$('#scroll-area').click(function() {
			$('html').animate({scrollTop:0},400);
	   });
};

function changePanel(){
	$('.ref-panel').click(function() {
		console.log($(this).attr("aria-expanded"))
  		if ($(this).attr("aria-expanded")=="true") {
			$(this).find(".panel-heading").css({"background":"#fff", "padding":"10px 15px"});
			$(this).find(".arrow").css("transform", "rotate(90deg)");			
		} 
		else { 
			$('html').animate({ scrollTop: $(this).offset().top - 5 }, 500);
			$(this).find(".panel-heading").css({"background":"#EDE6CE", "padding":"10px 2em"});
			$(this).find(".arrow").css("transform", "rotate(-90deg)");			
	 	}
	});
}
