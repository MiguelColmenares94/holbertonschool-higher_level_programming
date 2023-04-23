#!/usr/bin/node

function findSecondBiggestNumber (numbers) {
  if (numbers.length < 2) {
    return 0;
  }

  let biggest = 0;
  let secondBiggest = 0;
  let currentNumber;
  let counter;

  for (counter = 0; counter < numbers.length; counter++) {
    currentNumber = numbers[counter];

    if (currentNumber > biggest) {
      secondBiggest = biggest;
      biggest = currentNumber;
    } else if (currentNumber > secondBiggest) {
      secondBiggest = currentNumber;
    }
  }

  return secondBiggest;
}

const args = process.argv.slice(2);
const numbers = args.map(arg => parseInt(arg));
const result = findSecondBiggestNumber(numbers);

console.log(result);
