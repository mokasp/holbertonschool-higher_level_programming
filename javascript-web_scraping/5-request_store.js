#!/usr/bin/node
const args = process.argv;
args.splice(0, 2);
const request = require('request');
const fs = require('fs');
const url = args[0];

request(url, function (body) {
  fs.writeFile(args[1], body, 'utf-8', (err) => {
    if (err) throw err;
  });
});
