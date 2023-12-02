#!/usr/bin/node
const args = process.argv;
args.splice(0, 2)
const https = require('https')

https.get(args[0], response => {

    console.log(response.statusCode)
    })
