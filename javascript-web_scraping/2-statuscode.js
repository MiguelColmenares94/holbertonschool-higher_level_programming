#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (!err && response.statusCode) {
    console.log('code:', response.statusCode);
  }
});
