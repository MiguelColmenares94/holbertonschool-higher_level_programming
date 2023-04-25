#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w < 1 || h < 1 || w === undefined || h === undefined) {
      // Create an empty class
    } else {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
