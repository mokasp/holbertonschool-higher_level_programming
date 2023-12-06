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
  const theDict = {};
  for (const entry of parsedJson) {
    if (entry.completed === true) {
      if (!(entry.userId in theDict)) {
        theDict[entry.userId] = 0;
      }
      theDict[entry.userId] += 1;
    }
  }
  console.log(theDict);
});
