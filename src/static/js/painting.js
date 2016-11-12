$("td#left")
	.click( function(e){
		window.location.href = $("div#url-left").text();
		e.stopPropagation();
	} )
	.mouseenter( function(){
		$(this).css("background-color", "#f8f8f8");
		$(this).css("border-left-color", "#e7e7e7");
		$(this).css("border-top-color", "#e7e7e7");
		$(this).css("border-bottom-color", "#e7e7e7");
		$(this).css("cursor", "pointer");
	} )
	.mouseleave( function(){
		$(this).css("background-color", "transparent");
		$(this).css("border-color", "transparent");
		$(this).css("cursor", "default");
	} );


$("td#right")
	.click( function(e){
		window.location.href = $("div#url-right").text();
		e.stopPropagation();
	} )
	.mouseenter( function(){
		$(this).css("background-color", "#f8f8f8");
		$(this).css("border-right-color", "#e7e7e7");
		$(this).css("border-top-color", "#e7e7e7");
		$(this).css("border-bottom-color", "#e7e7e7");
		$(this).css("cursor", "pointer");
	} )
	.mouseleave( function(){
		$(this).css("background-color", "transparent");
		$(this).css("border-color", "transparent");
		$(this).css("cursor", "default");
	} );

$( document ).keydown( function(e){
	switch (e.keyCode){
		case $.ui.keyCode.LEFT:
			$("td#left").click();
			break;
		case 65: // A
			$("td#left").click();
			break;
		case 72: // H
			$("td#left").click();
			break;
		case 75: // K
			$("td#left").click();
			break;

		case $.ui.keyCode.RIGHT:
			$("td#right").click();
			break;
		case 68: // D
			$("td#right").click();
			break;
		case 76: // L
			$("td#right").click();
			break;
		case 74: // J
			$("td#right").click();
			break;
	}
} );


function fitPainting(){
	var max_Height = Math.round(window.innerHeight * 0.9);
	var img = document.getElementsByClassName("painting-image")[0];
	if ( img.height > 0 ){
		if ( img.height > max_Height ){
			img.width = Math.round(img.width / img.height * max_Height);
			img.height = max_Height;
		}
	}
}

$(window).load(fitPainting);
