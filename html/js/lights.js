$(document).ready(function() {
    $('.light-switch').click(function(event) {
        event.preventDefault();

        var newStatus;

        if($(this).data('status') === true) {
            $(this).html('<i class="fa fa-toggle-off fa-3x"></i>').animate(3000);
            $(this).data('status', false);
            newStatus = false;
        } else {
            $(this).html('<i class="fa fa-toggle-on fa-3x"></i>').animate(3000)
            $(this).data('status', true)
            newStatus = true;
        }

        // AJAX request
        $.ajax({
            url: '/lights/update',
            data: {
                lightName : $(this).data('light'),
                status : newStatus
            },
            method : 'POST'
        }).done(function(returnData) {
            console.log(returnData);
        })
    });

    $('.light-delete').click(function() {
        alert("Weet je zeker dat je lamp naam wilt verwijderen?");
    });
});