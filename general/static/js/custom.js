$(document).ready(function() {
    $('#upcoming').click(function() {
        console.log('upcoming');
        $('.upcoming_exhibition').show();
        $('.previous_exhibition').hide();
        $('.current_exhibition').hide();
    });

    $('#previous').click(function() {
        console.log('previous');
        $('.upcoming_exhibition').hide();
        $('.previous_exhibition').show();
        $('.current_exhibition').hide();
    });

    $('#current').click(function() {
        console.log('current');
        $('.upcoming_exhibition').hide();
        $('.previous_exhibition').hide();
        $('.current_exhibition').show();
    });
});
