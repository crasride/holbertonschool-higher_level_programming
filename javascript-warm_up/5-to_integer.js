#!/usr/bin/node
// parseInt Parses a string and returns an integer
const num = parseInt(process.argv[2]);

if (num) {
  console.log('My number: ' + num);
} else {
  console.log('Not a number');
}
