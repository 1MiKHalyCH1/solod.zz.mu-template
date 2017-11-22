function abc(){
	$(':checkbox').change(function() {
  		if ($(this).attr("checked")=="checked")
  		{
	   		$(":checkbox").removeAttr("checked");
	   		$(this).attr("checked", "checked");
	   	}
	});
}