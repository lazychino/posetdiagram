window.onload = function(){
	document.getElementById('ac_number').focus();
}

$( document ).ready(function() {

 });

function getjson(number){
	if (isNaN(number)) return false;
	else console.log('correct')
	$.get("/antichain/"+number, function( data ) {
  		return data;
	});
}