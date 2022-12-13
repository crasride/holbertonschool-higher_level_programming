#!/usr/bin/node
// import module AXIOS
const axios = require('axios');
// start the counter
let count = 0;
// response get from url
axios.get(process.argv[2]).then(
  res => {
    for (const movies of res.data.results) {
      for (const id of movies.characters) {
        // includes() returns true if a string contains a specified string
        if (id.includes(18)) {
          count++;
        }
      }
    }
    // print count
    console.log(count);
  });
