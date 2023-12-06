#!/usr/bin/node
const args = process.argv;
args.splice(0, 2)
const request = require('request')
const url = args[0]
request(url, function (error, response, body) {
    let parsedJson = JSON.parse(body);
    let filmList = []
    let peopleUrl = url.slice(0, -5)
    for (let film of parsedJson.results) {
        if (film.characters.includes(`${peopleUrl}people/18/`)) {
            filmList.push(film.title)
        }
    }
    console.log(filmList.length);
})
