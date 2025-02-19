/**
 * Fetches the translation of "Hello" in the language selected by the user
 */
$(document).ready(() => {
  $('#btn_translate').click(() => {
    const langCode = $('#language_code').val();
    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${langCode}`, (data) => {
      $('#hello').text(data.hello);
    });
  });
});
