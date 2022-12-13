#!/usr/bin/node
const request = require('request');
// url API starts wars + arg is = id of episode
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  // print error || print title
  console.log(error || JSON.parse(body).title);
});
