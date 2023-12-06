#!/usr/bin/node
const args = process.argv;
args.splice(0, 2);
const request = require('request');
const url = args[0];

request(url, function (error, body) {
  if (error) {
    console.log(error.stack);
  }
  const parsedJson = JSON.parse(body);
  const filmList = [];
  const peopleUrl = url.slice(0, -5);
  for (const film of parsedJson.results) {
    if (film.characters.includes(`${peopleUrl}people/18/`)) {
      filmList.push(film.title);
    }
  }
  console.log(filmList.length);
});
