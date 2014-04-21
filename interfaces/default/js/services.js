// Document ready
$(document).ready(function () {
    $('.spinner').show();
});


function get_watchedshows() {
    $.get(WEBDIR + 'services/outputwatchedplex', function (response) {
        $('#watchedshows').html(response);
    });
}

function get_iotop() {
    $.get(WEBDIR + 'services/getiotop', function (response) {
        $('#iotop').html(response);
    });
}