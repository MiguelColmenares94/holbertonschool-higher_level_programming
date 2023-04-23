#!/usr/bin/node

let counter;

if (Number.isNaN(Number(process.argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  for (counter = 0; counter < process.argv[2]; counter++) {
    console.log('C is fun');
  }
}
