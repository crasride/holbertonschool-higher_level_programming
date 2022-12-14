/* Define $ */
const $ = window.$;
/* The $.get() method loads data from the server using a HTTP GET request */
// Data - contains the resulting data from the request
$.get('https://stefanbohacek.com/hellosalut/?lang=fr', function (data) {
  $('DIV#hello').text(data.hello);
});
