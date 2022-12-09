#!/usr/bin/node
// prints the number of arguments already printed and the new argument value
exports.logMe = function (item) {
  let n = 0;
  console.log(n + ': ' + item);
  n++;
};
