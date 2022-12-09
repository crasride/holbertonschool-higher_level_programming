#!/usr/bin/node
// create class Square and inherits from Rectangle
const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
// exports class Square
module.exports = Square;
