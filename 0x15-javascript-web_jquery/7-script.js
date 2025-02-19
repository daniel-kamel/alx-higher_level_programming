/**
 * Fetches and replaces the name of this URL:
 * https://swapi-api.alx-tools.com/api/people/5/?format=json
 */
$(document).ready(() => {
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', (data) => {
    $('#character').text(data.name);
  });
});
