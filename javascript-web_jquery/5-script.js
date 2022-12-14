/* Define $ */
const $ = window.$;
/* The click() method triggers the click event, or attaches a function to run when a click event occurs */
$('DIV#add_item').click(function () {
  /* The append() method inserts specified content at the end of the selected elements. */
  $('UL.my_list').append('<li>Item</li>');
});

/*
The prepend() method inserts specified content at the beginning of the selected elements

The append() method inserts specified content at the end of the selected elements

The appendTo() method inserts HTML elements at the end of the selected elements
*/
