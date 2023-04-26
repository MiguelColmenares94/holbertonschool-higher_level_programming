#!/usr/bin/node
const filenames = ['./100-data', './data_0', './data_1', './data_2', './data_3'];

for (const filename of filenames) {
  const { list } = require(filename);
  console.log(list);
  console.log(list.map((value, index) => value * index));
}

