#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  let occurences = 0;

  for (counter; counter <= list.length; counter++) {
    if (list[counter] === searchElement) {
      occurences++;
    }
  }
  return (occurences);
};
