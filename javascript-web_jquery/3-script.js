/* Define $ */
const $ = window.$;
/* The click() method triggers the click event, or attaches a function to run when a click event occurs */
$('DIV#red_header').click(function () {
  /* The addClass() method adds one or more class names to the selected elements <header> */
  $('header').addClass('red');
});
