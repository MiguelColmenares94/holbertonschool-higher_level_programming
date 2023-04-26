#!/usr/bin/node

exports.esrever = function (list) {
  const reversed = [];
  let reversedLength = list.length - 1;
  let counter = 0;

  for (counter; counter <= list.length - 1; counter++) {
    if (list[counter] !== undefined) {
      reversed[reversedLength] = list[counter];
      reversedLength--;
    }
  }

  return (reversed);
};
