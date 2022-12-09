#!/usr/bin/node
function factorial (arg) {
  if (arg > 0) {
    return arg * factorial(arg - 1);
  } else { return 1}
}

const arg = parseInt(process.argv[2], 10);
console.log(factorial(arg));
