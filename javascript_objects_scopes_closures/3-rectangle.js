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
}

module.exports = Rectangle;
