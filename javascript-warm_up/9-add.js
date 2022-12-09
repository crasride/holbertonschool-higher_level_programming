#!/usr/bin/node
// function addition and sum
function add (a, b) {
  return a + b;
}
// defined variable
const a = parseInt(process.argv[2], 10);
const b = parseInt(process.argv[3], 10);
// print result
console.log(add(a, b));
