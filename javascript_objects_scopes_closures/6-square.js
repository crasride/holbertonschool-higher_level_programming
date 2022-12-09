#!/usr/bin/node
// create class Square and inherits from Square
const Square2 = require('./5-square.js');

class Square extends Square2 {
  charPrint (c = undefined) {
    if (c === undefined) {
      // super call constructor its parent class access the parent's properties and methods
      super.print();
    } else {
      super.print(c);
    }
  }
}

// exports class Square
module.exports = Square;
