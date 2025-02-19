/*
Using jQuery to change header color to red
When the user clicks on the tag DIV#red_header
*/
$(document).ready(() => {
  $('#red_header').click(() => {
    $('header').css('color', '#FF0000');
  });
});
