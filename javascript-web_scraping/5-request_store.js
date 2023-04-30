#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const dest = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }

  if (response.statusCode === 200) {
    fs.writeFile(dest, body, function (err) {
      if (err) throw err;
    });
  }
});
