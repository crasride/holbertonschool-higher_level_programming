/* Define $ */
const $ = window.$;
/* The click() method triggers the click event, or attaches a function to run when a click event occurs */
$('DIV#red_header').click(function () {
  $('header').css('color', '#FF0000');
});
