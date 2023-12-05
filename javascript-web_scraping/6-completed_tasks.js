#!/usr/bin/node
const args = process.argv;
args.splice(0, 2)
const request = require('request')
const url = args[0]

request(url, function (error, response, body) {
    let parsedJson = JSON.parse(body);
    let the_dict = {}
    for (let entry of parsedJson) {
        if (entry.completed === true) {
            if (!(entry.userId in the_dict)) {
                the_dict[entry.userId] = 0
            }
            the_dict[entry.userId] += 1
        }   
    }
    console.log(the_dict);
})
