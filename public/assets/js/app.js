$(document).ready(function() {
	number_word = ['one','two','three','four','five','six','seven','eight'];
	$('#home-link').on('click', function() {		
		$.get("/home.html", function(data) {
			$('#view').empty().append(data);
			
			$('#ac_number').focus();
			$('#generate').on('click', function() {
				var number = Number($('#ac_number').val());
				if(isNaN(number) || number < 2 || number > 7) 
					return;
				$('#poset').empty().append('<img class="loading" src="/assets/loading.gif" alt="loading">');
				$.get("/antichain/"+number, function( data ) {
					$('#poset').empty();
					drawPoset(data, number);
					data = JSON.parse(data);
					
					data.levels = countLevels(data);
					//console.log(data.levels);
					data = nodeGrades(data);
					data.levels = data.levels.reverse();
					
					var grades = [];
					for (i = 0 ; i < number ; i++)
						grades.push([]);
						
					for (var j in data.nodes){
						if (grades[data.nodes[j].level].indexOf(data.nodes[j].grade) == -1)
							grades[data.nodes[j].level].push(data.nodes[j].grade ? data.nodes[j].grade : 0);
					}
					console.dir(grades);
					
					$("#nodeslevel").empty();
					var tmp = [];
					var word = '';
					for (i = 0 ; i < data.levels.length; i++){
						word = (data.levels[i]==1) ? ' node.':' nodes.';
						
						for ( var x in grades[i])
							console.log(grades[i][x]);
						console.log(tmp)
						tmp=[];
						$("#nodeslevel").append('<li>Level '+ number_word[i] + ' has ' + data.levels[i] + word + ' with ' + grades + ' links ' </li><br>');
					}

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
