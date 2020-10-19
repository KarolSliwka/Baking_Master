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

    if ($('.ingridient')[0]) {

        let cloned = $('#ingridients').children('.ingridient').first().clone();
        cloned.appendTo('#ingridients');
    }
    else {
         $('#ingridients').append('<div class="ingridient"><input type="text" class="form-control" id="ingridient-name" name="ingridient-name" placeholder="Ingridient name" required><input type="text" class="form-control" id="ingridient-scale" name="ingridient-scale" placeholder="g,kg,l,ml etc." required><button class="removeIngridient btn main-button-small" type="button">x</button></div>');
    }
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
        stepCount++;
        let countLabel = ("<label class='step-label'>Step " + stepCount + "</label>");
        $('#steps').append('<div class="step"><div class="top-step"><label class="step-label">' + countLabel + '</label><button class="removeStep btn main-button-small" type="button">x</button></div><textarea class="form-control" rows="2" id="preparation-step" placeholder="Step explanation" required></textarea></div>');
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

    if ($('.tips')[0]) {

        let clonedTips = $('#tips').children('.tip').first().clone();

        tipCount++;
        let countTipLabel = ("<label class='tip-label'>Tip " + tipCount + "</label>");
        clonedTips.appendTo('#tips');
        clonedTips.find('label').replaceWith(countTipLabel);
        console.log(countTipLabel);

    }
    else {
        tipCount++;
        let countTipLabel = ("<label class='tip-label'>Tip " + tipCount + "</label>");
        $('#tips').append('<div class="tip"><div class="top-tip"><label class="tip-label">' + countTipLabel + '</label><button class="removeTip btn main-button-small" type="button">x</button></div><textarea class="form-control" rows="2" id="preparation-tip" placeholder="Tip explanation" required></textarea></div>');
    }
});

/**
 * This function will remove unwanted tip fields
 */
$('body').on('click', '.removeTip', function() {
    $(this).closest('.tip').remove();
    tipCount--;
});