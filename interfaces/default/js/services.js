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
    $.get(WEBDIR + 'services/outputwatchedplex', function (response) {
        $('#watched').html(response);
    });
}

function get_iotop() {
    $.get(WEBDIR + 'services/getiotop', function (response) {
        $('#iotop').html(response);
    });
}

function reloadtab() {
    if ($('#watched').is(':visible')) {
        get_watchedshows();
    } else if ($('#iotop').is(':visible')) {
        get_iotop();
    }
}

$('#watched').click(function () {
    get_watchedshows();
});
$('#iotop').click(function () {
    get_iotop();
});
