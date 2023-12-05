#!/usr/bin/node
const args = process.argv;
args.splice(0, 2)
const request = require('request')
const url = args[0]

request(url, function (error, response, body) {
    let parsedJson = JSON.parse(body);
    let the_dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    for (let entry of parsedJson) {
        if (!(entry.userId in the_dict) && (entry.completed === true)) {
            the_dict[entry.userId] = 0
        }
        if (entry.completed === true) {
            the_dict[entry.userId] += 1
        }   
    }
    console.log(the_dict);
})
