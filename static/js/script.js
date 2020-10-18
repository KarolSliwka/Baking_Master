/* global $ */

/**
 * This functions is taking current full year and passing it into copyrights section
 */
$('#copyright').html(new Date().getFullYear());

/**
 * This function will clear contact form
 */
$('#clear-contact-form').click(function() {
    $('#contact-name').val('');
    $('#contact-email').val('');
    $('#contact-message').val('');
});

/**
 * This function will hide flash messages after few seconds
 */
$(document).ready(function() {
    setTimeout(function() {
        $('#flash-message').animate({ height: 0, opacity: 0 }, 'fast');
    }, 3500);
});


/**
 * This function will execut code to collapse info section in about page
 */
$('#myCollapsible').collapse({
    toggle: false
})

/** 
 * This function will add another ingridient 
 */
$(".appendIngridient").click(function() {
    $("#ingridients").append('<div class="ingridient"><input type="text" class="form-control" id="preparing-time" name="preparing-time" placeholder="Ingridient name"required><input type="text" class="form-control" id="preparing-time" name="preparing-time" placeholder="" required></div>').insertBefore('.appendIngridient');
});