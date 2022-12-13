#!/usr/bin/node
// that display the status code of a GET request
const request = require('request');
request(process.argv[2], function (error, response) {
  if (error == null) {
    console.log('code: ' + response.statusCode);
  }
});
