// Submit post on submit
$(document).ready(function () {
        //$.get("/book/ajax/search", function (data) {
        //    alert(data);
        //});
        $('#searchButton').click(function(event){
        var q = $("#place").val();
        console.log(q);
        $.ajax({
                type: "GET",
                data: {'place':q},
                url: '/book/ajax/search',
                success: function(data) {
                    $("#results").html(data);
                }
            });
        return  false;
});
    });
/*$( document ).ajaxStart( function() {
$( ‘#spinner’ ).show();
}).ajaxStop( function() {
$( ‘#spinner’ ).hide();
});*/
