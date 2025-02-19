/**
 * Fetches and lists all movies title by using this
 * URL: https://swapi-api.alx-tools.com/api/films/?format=json
 */
$(document).ready(() => {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', (data) => {
    data.results.forEach((movie) => {
      $('#list_movies').append('<li>' + movie.title + '</li>');
    });
  });
});
