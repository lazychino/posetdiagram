$(document).ready(function() {
		
	$('#home-link').on('click', function() {		
		$.get("/home.html", function(data) {
			$('#view').empty().append(data);
			
			$('#ac_number').focus();
			$('#generate').on('click', function() {
				var number = Number($('#ac_number').val());
				if(isNaN(number)) 
					return;
				$('#poset').empty().append('<img class="loading" src="/assets/loading.gif" alt="loading">');
				$.get("/antichain/"+number, function( data ) {
					$('#poset').empty();
					drawPoset(data, number);
				});
			});
		});
	}).click();
	
	$('#team-link').on('click', function() {
		$.get("/team.html", function( data ) {
			$('#view').empty().append(data);
		});
	});
	$('#about-link').on('click', function() {
		$.get("/about.html", function( data ) {
			$('#view').empty().append(data);
		});
	});
});
