#!/usr/bin/node
const request = require('request');
// Import the filesystem module
const fs = require('fs');

request(process.argv[2], 'utf8', function (err, response, body) {
  if (err == null) {
    // Method gets the contents of a webpage and stores it in 'loripsum file'
    fs.writeFileSync(process.argv[3], body);
  }
});
