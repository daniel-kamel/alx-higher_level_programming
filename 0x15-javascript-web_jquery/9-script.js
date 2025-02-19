/**
 * Fetches and prints how to say “Hello” depending on the language
 */
$(document).ready(() => {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', (data) => {
    $('#hello').text(data.hello);
  });
});
