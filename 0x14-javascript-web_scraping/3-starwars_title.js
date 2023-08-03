#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
const options = {
  url: url,
  json: true
};
request.get(options, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    console.log(body.title);
  }
});
