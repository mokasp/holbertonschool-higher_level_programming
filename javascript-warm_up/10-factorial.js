#!/usr/bin/node
const num = parseInt(process.argv[2]);
let rval = 1;
for (let i = 2; i <= num; i++) { rval = rval * i; }
console.log(rval);
