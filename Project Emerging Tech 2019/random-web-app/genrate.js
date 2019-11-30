$(document).ready(function(g){
	
	$("submitButton").click(function(g){
		
		g.preventDefault();
		
		noofros = $("noofros").val();
		
		$.postp("/random",{"noofros": noofros}, function(data){
			
			$("#randomNumbers").text(data.randomNos.join("\n"));
		});
	});
	
});