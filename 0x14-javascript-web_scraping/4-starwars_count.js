#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const charId = 18;
const options = {
  url: url,
  json: true
};

request.get(options, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    if (response.statusCode === 200) {
      const moviesWithWedgeAntilles = body.results.filter((film) =>
        film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${charId}/`)
      );
      console.log(moviesWithWedgeAntilles.length);
    }
  }
});
