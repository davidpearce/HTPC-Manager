// Document ready
$(document).ready(function () {
    $('.spinner').show();
});


function get_watchedshows() {
    $.get(WEBDIR + 'services/outputwatchedplex', function (response) {
        $('#watchedshows').html(response);
    });
}