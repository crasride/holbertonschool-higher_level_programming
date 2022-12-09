#!/usr/bin/node
// create class Square and inherits from Square
const Square2 = require('./5-square.js');

class Square extends Square2 {
  charPrint (c) {
    if (c === undefined) c = 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

// exports class Square
module.exports = Square;
