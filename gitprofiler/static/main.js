$(document).ready(function(){
    $("form").on("submit", function(event){
        // Prevent the form from causing the page to reload
        event.preventDefault();

        // Show the modal
        $("#myModal").modal('show');

        // Hide the modal after 10 seconds
        setTimeout(function(){
            $("#myModal").modal('hide');
        }, 5000);
    });
});