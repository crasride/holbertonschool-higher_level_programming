#!/usr/bin/node
// that returns the reversed version of a list:
exports.esrever = function (list) {
  if (list === undefined) return [];
  const reversed = [];
  for (let R = list.length - 1; R >= 0; R--) {
    reversed.push(list[R]);
  }
  return reversed;
};
