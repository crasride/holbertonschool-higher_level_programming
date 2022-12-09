#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) { console.log('X'.repeat(this.width)); }
  }

  rotate () {
    // method called rotate() exchanges the width and the height of the rectangle
    const rota = this.width;
    this.width = this.height;
    this.height = rota;
  }

  double () {
  // method called double() multiples the width and the height of rectangle by 2
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
