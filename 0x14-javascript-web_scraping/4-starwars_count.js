#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
let count = 0;
const regex = /\/people\/18/i;
const options = {
  url: url,
  json: true
};

request.get(options, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    if (response.statusCode === 200) {
      body.results.forEach((film) => {
        if (regex.test(film.characters)) {
          count++;
        }
      }
      );
      console.log(count);
    }
  }
});
