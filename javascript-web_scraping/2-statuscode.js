#!/usr/bin/node
const args = process.argv;
args.splice(0, 2);
const request = require('request');

request(args[0], (error, response) => {
  if (error) {
    console.log(error.stack);
  }
  console.log(`code: ${response.statusCode}`);
});
