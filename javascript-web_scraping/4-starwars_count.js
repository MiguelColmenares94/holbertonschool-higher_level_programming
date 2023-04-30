#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
let count = 0;
let characterId = 18;

request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);

    /*  Another way to do it: 
    *const count = data.results.characters.filter(url => url.includes('/18/')).length;
    */

    data.results.forEach(function (movie) {
     if (movie.characters.includes(`https://swapi-api.hbtn.io/api/people/${characterId}/`)) {
        count++;
       }
     });
     

    console.log(count);
  } else {
    console.log('Usage: scriptName URL');
  }
});
