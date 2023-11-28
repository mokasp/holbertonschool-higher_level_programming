#!/usr/bin/node
const args = process.argv;
args.splice(0, 2);
let count = 0;

for (const i of args) { // eslint-disable-line no-unused-vars
  count++;
}
if (count === 0) {
  console.log('No argument');
} else {
  console.log(args[0]);
}
