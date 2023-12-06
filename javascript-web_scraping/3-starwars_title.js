#!/usr/bin/node
const args = process.argv;
args.splice(0, 2);
const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${args[0]}`;

request(url, function (error, body) {
  if (error) {
    console.log(error.stack);
  }
  const parsedJson = JSON.parse(body);
  console.log(parsedJson.title);
});
