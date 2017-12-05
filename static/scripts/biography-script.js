function scroll(){
	$("label div").fadeIn(500);
	$(':checkbox').change(function() {
  		if ($(this).attr("checked")=="checked")
  		{
	   		$(":checkbox").removeAttr("checked");
	   		$(this).attr("checked", "checked");
	   	}
	   	var label = $("label[for='"+$(this).attr('id')+"']");
	   	$('body,html').animate({ scrollTop: $(label).offset().top }, 500);
	});
	
}
