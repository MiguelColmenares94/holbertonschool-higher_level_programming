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

  print () {
    let counterLine;
    let counterSize;

    if (this.width && this.height) {
      for (counterSize = 0; counterSize < this.height; counterSize++) {
        for (counterLine = 0; counterLine < this.width; counterLine++) {
          process.stdout.write('X');
        }
        console.log();
      }
    }
  }

  rotate () {
    const temp = this.width;

    this.width = this.height;
    this.height = temp;
  }

  double () {
    const mulw = this.width * 2;
    const mulh = this.height * 2;

    this.width = mulw;
    this.height = mulh;
  }
}

module.exports = Rectangle;
