#!/usr/bin/node
const length = process.argv.length;
if (length === 2) {
  console.log('No argument');node -v
} else if (length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
