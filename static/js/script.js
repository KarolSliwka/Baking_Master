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
 * This function will add another ingredient
 */
let ingrCount = 0;
$(".appendIngredient").click(function() {
    $('#ingredients').append('<div class="ingredient"><div class="top-ingredient"><button class="removeingredient btn main-button-small" type="button">x</button><div class="ingredient-inputs"><input type="text" class="form-control" id="ingredient-name" name="ingredient-name-' + ingrCount +'" placeholder="Ingredient" required><input type="text" class="form-control" id="ingredient-scale" name="ingredient-scale- ' + ingrCount + '" placeholder="2g/5ml" required></div></div></div>');
    ingrCount++;
    console.log(ingrCount);
});

/**
 * This function will remove unwanted ingredient fields
 */
$('body').on('click', '.removeingredient', function() {
    $(this).closest('.ingredient').remove();
    ingrCount--;
});

/**
 * This function will add another step
 */
let stepCount = 0;
$(".appendStep").click(function() {

    if ($('.step')[0]) {

        stepCount++;
        let countLabel = ("<label class='step-label'>Step " + stepCount + "</label>");
        $('#steps').append('<div class="step"><div class="top-step"><label class="step-label">' + countLabel + '</label><button class="removeStep btn main-button-small" type="button">x</button></div><textarea class="form-control" name="preparation-step-' + stepCount + '"rows="2" id="preparation-step" placeholder="Step explanation" required></textarea></div>');
    }
    else {
        stepCount++;
        let countLabel = ("<label class='step-label'>Step " + stepCount + "</label>");
        $('#steps').append('<div class="step"><div class="top-step"><label class="step-label">' + countLabel + '</label><button class="removeStep btn main-button-small" type="button">x</button></div><textarea class="form-control" name="preparation-step-' + stepCount + '"rows="2" id="preparation-step" placeholder="Step explanation" required></textarea></div>');
    }
});

/**
 * This function will remove unwanted step fields
 */
$('body').on('click', '.removeStep', function() {
    $(this).closest('.step').remove();
    if ($('.steps')[0]) {
        stepCount++;
    }
    else {
        stepCount = document.querySelectorAll('.step').length;
    }
});

/**
 * This function will add another tip
 */
let tipCount = 0;
$(".appendTip").click(function() {

    if ($('.tips')[0]) {

        tipCount++;
        let countTipLabel = ("<label class='tip-label'>Tip " + tipCount + "</label>");
        $('#tips').append('<div class="tip"><div class="top-tip"><label class="tip-label">' + countTipLabel + '</label><button class="removeTip btn main-button-small" type="button">x</button></div><textarea class="form-control" name="tip-step-' + tipCount + ' "rows="2" id="preparation-tip" placeholder="Tip explanation" required></textarea></div>');
    }
    else {
        tipCount++;
        let countTipLabel = ("<label class='tip-label'>Tip " + tipCount + "</label>");
        $('#tips').append('<div class="tip"><div class="top-tip"><label class="tip-label">' + countTipLabel + '</label><button class="removeTip btn main-button-small" type="button">x</button></div><textarea class="form-control" name="tip-step-' + tipCount + ' "rows="2" id="preparation-tip" placeholder="Tip explanation" required></textarea></div>');
    }
});

/**
 * This function will remove unwanted tip fields
 */
$('body').on('click', '.removeTip', function() {
    $(this).closest('.tip').remove();
    if ($('.tips')[0]) {
        tipCount++;
    }
    else {
        tipCount = document.querySelectorAll('.tip').length;
    }
});


/**
 * This function will animate progress bar for favourites page 
 */
let timeleft = 10;
let downloadTimer = setInterval(function(){
  if(timeleft <= 0){
    clearInterval(downloadTimer);
  }
  document.getElementById("progressBar").value = 10 - timeleft;
  timeleft -= 1;
}, 1000);