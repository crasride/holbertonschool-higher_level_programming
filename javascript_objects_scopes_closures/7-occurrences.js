#!/usr/bin/node
// Returns the number of occurrences list
exports.nbOccurences = function (list, searchElement) {
  return (list.filter(elem => elem === searchElement).length);
};
