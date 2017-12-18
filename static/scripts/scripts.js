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


