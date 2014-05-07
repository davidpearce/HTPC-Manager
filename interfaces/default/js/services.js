// Document ready



// Set timeintercal to refresh stats
setInterval(function () {
    //get_diskinfo();
    if ($('#iotop').is(':visible')) {
        get_iotop();
    }
}, 1000);




$(document).ready(function () {
    $('.spinner').show();
});

function get_watchedshows() {
    $('#watcheddata').html("<br />");
    $('.spinner').show();
    $.get(WEBDIR + 'services/outputwatchedplex', function (response) {
        $('#watcheddata').html(response);
    });
    $('.spinner').hide();
}

function get_iotop() {
    $.get(WEBDIR + 'services/getiotop', function (response) {
        $('#iotopdata').html(response);
    });
    $('.spinner').hide();
}

function reloadtab() {
    if ($('#watched').is(':visible')) {
        get_watchedshows();
    } else if ($('#iotop').is(':visible')) {
        get_iotop();
    }
}

$('#watchedl').click(function () {
    get_watchedshows();
});
$('#iotopl').click(function () {
    get_iotop();
});
