/* Define $ */
const $ = window.$;
/* The $.get() method loads data from the server using a HTTP GET request */
// Data - contains the resulting data from the request
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  // Define variable list for movie
  const list = data.results;
  // Scroll down the list of results and returns the length of a string
  for (let i = 0; i < list.length; i++) {
    // Recover the value and create a list with the titles one by one
    $('UL#list_movies').append('<li>' + list[i].title + '</li>');
  }
});
