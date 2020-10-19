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
    cloned.appendTo('#ingridients');

});

/**
 * This function will remove unwanted ingridient fields
 */
$('body').on('click', '.removeIngridient', function() {
    $(this).closest('.ingridient').remove();
});

/**
 * This function will add another step
 */
let stepCount = 1;
$(".appendStep").click(function() {

    if ($('.step')[0]) {

        let clonedSteps = $('#steps').children('.step').first().clone();

        stepCount++;
        let countLabel = ("<label class='step-label'>Step " + stepCount + "</label>");
        clonedSteps.appendTo('#steps');
        clonedSteps.find('label').replaceWith(countLabel);
        console.log(countLabel);

    }
    else {
        
    }
});

/**
 * This function will remove unwanted step fields
 */
$('body').on('click', '.removeStep', function() {
    $(this).closest('.step').remove();
    stepCount--;
});

/**
 * This function will add another tip
 */
let tipCount = 1;
$(".appendTip").click(function() {

    let clonedTips = $('#tips').children('.tip').first().clone();

    tipCount++;
    let countTipLabel = ("<label class='tip-label'>Tip " + tipCount + "</label>");
    clonedTips.appendTo('#tips');
    clonedTips.find('label').replaceWith(countTipLabel);
    console.log(countTipLabel);
});

/**
 * This function will remove unwanted tip fields
 */
$('body').on('click', '.removeTip', function() {
    $(this).closest('.tip').remove();
    tipCount--;
});
