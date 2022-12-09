#!/usr/bin/node
// variable defined
const args = process.argv;
const parseValue = parseInt(process.argv[2], 10);
// variable initialize
let i = 0;
// conditional , isNaN() method returns true if a value is NaN
if (isNaN(parseValue)) {
  console.log('Missing size');
} else {
  while (i < args[2]) {
    console.log('X'.repeat(args[2]));
    i++;
  }
}
