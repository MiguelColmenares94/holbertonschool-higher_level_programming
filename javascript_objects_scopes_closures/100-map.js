#!/usr/bin/node
const { list } = require('./test/100-data');
console.log(list);
console.log(list.map((value, index) => value * index));
