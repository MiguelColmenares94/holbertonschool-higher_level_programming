#!/usr/bin/node

let counterLine;
let counterSize;

if (Number.isNaN(Number(process.argv[2]))) {
  console.log('Missing size');
} else {
  for (counterSize = 0; counterSize < process.argv[2]; counterSize++) {
    for (counterLine = 0; counterLine < process.argv[2]; counterLine++) {
      process.stdout.write('X');
    }
    console.log();
  }
}
