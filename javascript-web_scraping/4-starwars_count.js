#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (!error) {
    // Convert JSON TO Objects(for analysis string conversion)
    const restconv = JSON.parse(body).results;
    console.log(restconv.reduce((count, movie) => {
      // method returns true if a string ends with a specified string
      return (movie.characters.find((character) => character.endsWith('/18/')))
        // The conditional (ternary) operator
        ? count + 1
        : count;
    }, 0));
  }
});
