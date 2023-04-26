#!/usr/bin/node

exports.esrever = function (list) {
  const reversed = [];
  let reversedLength = list.length;
  let counter = 0;

  for (counter; counter <= list.length; counter++) {
    if (list[counter] !== undefined) {
      reversed[reversedLength] = list[counter];
      reversedLength--;
    }
  }

  return (reversed);
};
