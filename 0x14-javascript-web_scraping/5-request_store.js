#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];
const options = {
  url: url,
  json: true
};

request.get(options, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    if (response.statusCode === 200) {
      fs.writeFile(filePath, body, (err) => {
        if (err) {
          console.error(err);
        }
      });
    }
  }
});
