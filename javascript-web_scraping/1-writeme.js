#!/usr/bin/node
const args = process.argv;
args.splice(0, 2)
const fs = require('fs')


fs.writeFile(args[0], args[1], 'utf-8', (err) => {
    if (err) throw err;
})
