/* Define $ */
const $ = window.$;
/* The click() method triggers the click event, or attaches a function to run when a click event occurs */
$('DIV#update_header').click(function () {
  // The text() method sets or returns the text content of the selected elements */
  $('header').text('New Header!!!');
});
