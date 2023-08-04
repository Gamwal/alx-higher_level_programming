#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const options = {
  url: url,
  json: true
};

request.get(options, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    if (response.statusCode === 200) {
      const completedTasksByUser = {};
      body.forEach((todo) => {
        if (todo.completed) {
          if (completedTasksByUser[todo.userId]) {
            completedTasksByUser[todo.userId]++;
          } else {
            completedTasksByUser[todo.userId] = 1;
          }
        }
      });
      console.log(completedTasksByUser);
    }
  }
});
