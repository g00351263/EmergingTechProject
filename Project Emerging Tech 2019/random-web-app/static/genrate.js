$(document).ready(function(g){
	
	$("submitButton").click(function(g){
		
		g.preventDefault();
		
		noofros = document.getElementById('sheet');
		
		console.log(noofros[0].toDataURL());

		});
	});
	
});