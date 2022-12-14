/* Define $ */
const $ = window.$;
/* The $.get() method loads data from the server using a HTTP GET request */
// data - contains the resulting data from the request
$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
  // The text() method sets or returns the text content of the selected elements */
  // Selected data type element
  $('DIV#character').text(data.name);
});
