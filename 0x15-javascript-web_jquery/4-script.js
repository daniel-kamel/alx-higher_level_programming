/**
 * Toggles the class of the HTML tag HEADER to red (#FF0000)
 * when the user clicks on the tag DIV#toggle_header
 */
$(document).ready(() => {
  $('#toggle_header').click(() => {
    $('header').toggleClass('red green');
  });
});
