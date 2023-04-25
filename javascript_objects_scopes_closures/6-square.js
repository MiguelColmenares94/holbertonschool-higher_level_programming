#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let counterLine;
    let counterSize;

    if (this.width && this.height) {
      for (counterSize = 0; counterSize < this.height; counterSize++) {
        for (counterLine = 0; counterLine < this.width; counterLine++) {
          if (c === 'c' || c === 'C') {
            process.stdout.write(c);
          } else {
            process.stdout.write('X');
          }
        }
        console.log();
      }
    }
  }
}
module.exports = Square;
