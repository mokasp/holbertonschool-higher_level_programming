#!/usr/bin/node
const args = process.argv;
args.splice(0, 2)
const request = require('request')
const url = `https://swapi-api.hbtn.io/api/films`

request(url, function (error, response, body) {
    let parsedJson = JSON.parse(body);
    let filmList = []
    for (let film of parsedJson.results) {
        if (film.characters.includes("https://swapi-api.hbtn.io/api/people/18/")) {
            filmList.push(film.title)
        }
    }
    console.log(filmList.length);
})
