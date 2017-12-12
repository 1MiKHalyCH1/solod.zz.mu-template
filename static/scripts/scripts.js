function scrollTop() {
	$('#scroll-area').fadeOut();	
	$('#scroll-arrow').fadeOut();	
	$(window).scroll(function() {
		// console.log($(this).scrollTop());
		if($(this).scrollTop() > 50) { 
			$('#scroll-area').fadeIn(); 
			$('#scroll-arrow').fadeIn();
		} 
		else { 
			$('#scroll-area').fadeOut();
			$('#scroll-arrow').fadeOut();
	 }
   	});
   	$('#scroll-area').click(function() {
		   $('body,html').animate({scrollTop:0},400);
   	});
};


function scroll(){
	$('.panel-heading').click(function() {
		$('body,html').animate({ scrollTop: $(this).offset().top - 10 }, 500);
	});
}

// function scroll(){
// 	$("label div").fadeIn(500);
// 	$(':checkbox').change(function() {
//   		if ($(this).attr("checked")=="checked")
//   		{
// 	   		$(":checkbox").removeAttr("checked");
// 	   		$(this).attr("checked", "checked");
// 	   	}
// 	   	var label = $("label[for='"+$(this).attr('id')+"']");
// 	   	$('body,html').animate({ scrollTop: $(label).offset().top }, 500);
// 	});
	
// }



// function rotateArrow(){
// 	$('.panel-heading').click(function() {
		//   $(this .arrow).attr("rotate", "rotate(90deg)");
		// $(this).style.background = "red";
		// $(this).style.cssText = "background-color: red;";
		// console.log($(this).attr("checked"));
		//   $('.panel-heading').style.background = 'red';
		  
		//   var dynamicSize = document.getElementById('.panel-heading')[0].style.background; 
		//   if (document.getElementById(block_4_close).style.disp lay='none') {dynamicSize = size;}
	   	// var label = $("label[for='"+$(this).attr('id')+"']");
		   // $('body,html').animate({ scrollTop: $(label).offset().top }, 500);
	   	// $('body,html').animate({ scrollTop: $(this).offset().top }, 500);
	// });
// }


