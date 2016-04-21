$(document).ready(function() {
    $('#upcoming').click(function() {
        console.log('upcoming');
        $('.upcoming_exhibition').show();
        $('.previous_exhibition').hide();
        $('.current_exhibition').hide();
        $('.street_art_festival').hide();
        $('.walloffame_panel').hide();
    });

    $('#previous').click(function() {
        console.log('previous');
        $('.upcoming_exhibition').hide();
        $('.previous_exhibition').show();
        $('.current_exhibition').hide();
        $('.street_art_festival').hide();
        $('.walloffame_panel').hide();
    });

    $('#current').click(function() {
        console.log('current');
        $('.upcoming_exhibition').hide();
        $('.previous_exhibition').hide();
        $('.current_exhibition').show();
        $('.street_art_festival').hide();
        $('.walloffame_panel').hide();
    });

    $('#street_art').click(function() {
        console.log('street art');
        $('.upcoming_exhibition').hide();
        $('.previous_exhibition').hide();
        $('.current_exhibition').hide();
        $('.street_art_festival').show();
        $('.walloffame_panel').hide();
    });

    $('#wall_of_fame').click(function() {
        console.log('wall of fame');
        $('.upcoming_exhibition').hide();
        $('.previous_exhibition').hide();
        $('.current_exhibition').hide();
        $('.street_art_festival').hide();
        $('.walloffame_panel').show();
    });

    $('#print').click(function() {
        console.log('print');
        $('.shop_print').show();
        $('.shop_clothing').hide();
        $('.shop_art').hide();
        $('.burning_man').hide();
    });

    $('#clothing').click(function() {
        console.log('clothing');
        $('.shop_print').hide();
        $('.shop_clothing').show();
        $('.shop_art').hide();
        $('.burning_man').hide();
    });

    $('#art').click(function() {
        console.log('art');
        $('.shop_print').hide();
        $('.shop_clothing').hide();
        $('.shop_art').show();
        $('.burning_man').hide();
    });

    // $('.home_slider').slick({
    //     // accesibility: true,
    //     autoplay: true,
    //     adaptiveHeight: true,
    //     // dots: true,
    // });
    $('.home_slider').slick();

    $('#home_street_art').click(function() {
        window.location = '/general/gallery?home=art'
    });

    $('#home_wall_of_fame').click(function() {
        window.location = '/general/gallery?home=fame'
    });

    $('#art7').click(function() {
        $('.shop_print').hide();
        $('.shop_clothing').hide();
        $('.shop_art').hide();
        $('.burning_man').show();
    });

    var query = window.location.search.substring(1)
    if (query.split('=')[1] == 'art') {
        $('.upcoming_exhibition').hide();
        $('.previous_exhibition').hide();
        $('.current_exhibition').hide();
        $('.street_art_festival').show();
        $('.walloffame_panel').hide();
    } else if (query.split('=')[1] == 'fame') {
        $('.upcoming_exhibition').hide();
        $('.previous_exhibition').hide();
        $('.current_exhibition').hide();
        $('.street_art_festival').hide();
        $('.walloffame_panel').show();
    }
});
