/* Define $ */
const $ = window.$;
/* The click() method triggers the click event, or attaches a function to run when a click event occurs */
$('DIV#toggle_header').click(function () {
  /* The toggleClass() method toggles between adding and removing one or more class names from the selected elements. <header> */
  $('header').toggleClass('red green');
});

/* the second click() method
  The hasClass() method checks if any of the selected elements have a specified class name
  if ($('header').hasClass('red')) {
    The removeClass() method removes one or more class names from the selected elements.
    $('header').removeClass('red');
    $('header').addClass('green');
  } else {
    $('header').removeClass('green');
    $('header').addClass('red');
  }
  */
