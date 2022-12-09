#!/usr/bin/node
// variable defined
const num = parseInt(process.argv[2]);
// isNaN() method returns true if a value is NaN.
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 1; i <= num; i++) {
    console.log('C is fun');
  }
}
