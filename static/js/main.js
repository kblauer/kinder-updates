'use strict';


$(function(){

    $("button").on('click', function(){

        $("#loginPopUp").slideToggle(100);
    });
});

$(function(){

    $("#loginPopUp").hide();
});


$(function(){
	
	$('.leftCol .panel').on('click', function(){

		var clickedPanelID = $(this).attr('id');

		if(clickedPanelID === 'Updates'){

			$(this).removeClass('panel-primary');
			$(this).addClass('panel-info');

			$('#Assignments').removeClass('panel-info');
			$('#Assignments').addClass('panel-primary');

			$('#Main' + ' .panel-heading').html("Updates");

		}

		else {

			$(this).removeClass('panel-primary');
			$(this).addClass('panel-info');

			$('#Updates').removeClass('panel-info');
			$('#Updates').addClass('panel-primary');

			$('#Main' + ' .panel-heading').html("Assignments");

		}
	});
});



