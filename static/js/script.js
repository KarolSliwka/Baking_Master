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
});

/**
 * This function will add another ingridient
 */
$(".appendIngridient").click(function() {

    let cloned = $('#ingridients').children('.ingridient').first().clone();
    if ($(".ingridient")[0] != undefined) {
        $("#ingridients").append('<div class="ingridient"><input type="text" class="form-control" id="ingridient-name" name="ingridient-name" placeholder="Ingridient name" required><input type="text" class="form-control" id="ingridient-scale" name="ingridient-scale" placeholder="g,kg,l,ml etc." required><button class="removeIngridient btn main-button-small" type="button">x</button></div>');
    }
    else {
        cloned.appendTo('#ingridients');
    }
});

/**
 * This function will remove unwanted ingridient fields
 */
$('body').on('click', '.removeIngridient', function() {
    $(this).closest('.ingridient').fadeOut();
});

/**
 * This function will add another ingridient
 */
let stepCount = 1;
$(".appendStep").click(function() {

    let clonedSteps = $('#steps').children('.step').first().clone();

    stepCount++;
    let countLabel = ("<label class='step'>Step " + stepCount + "</label>");
    clonedSteps.appendTo('#steps');
    clonedSteps.find('label').replaceWith(countLabel);
    console.log(countLabel);
});

/**
 * This function will remove unwanted ingridient fields
 */
$('body').on('click', '.removeStep', function() {
    $(this).closest('.step').fadeOut();
    stepCount--;
});
