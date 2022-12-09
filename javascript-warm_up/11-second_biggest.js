#!/usr/bin/node
// define variable
const size = process.argv.length;
// condition
if (size <= 3) {
  console.log('0');
} else {
// does not change the original array.
  const args = process.argv.map(Number)
  // method returns selected elements in an array
    .slice(2, size)
  // sort() function compares values
    .sort((a, b) => a - b);
  console.log(args[args.length - 2]);
}
