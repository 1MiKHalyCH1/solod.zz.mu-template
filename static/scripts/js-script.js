function scrollTop() {
	$(window).scroll(function() {
		if($(this).scrollTop() > 46) {
			$('#scrollTop').fadeIn();
		} 
		else {
   			$('#scrollTop').fadeOut();
   		}
   	});
   	$('#scrollTop').click(function() {
   		$('body,html').animate({scrollTop:0},400);
   	});
};
