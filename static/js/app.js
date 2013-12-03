window.onload = function(){
	document.getElementById('ac_number').focus();
}

$( document ).ready(function() {

	function getjson(number){
	if (isNaN(number)) return false;
	$.get("/antichain/"+number, function( data ) {
  		return data;
	});
}
 });

