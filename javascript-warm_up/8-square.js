#!/usr/bin/node
const x = process.argv[2];
if (Number.isInteger(x)) {
  const row = [];
  for (let i = 0; i < x; i++) {
    for (let j = 0; j < x; j++) { row.push('X'); }
    if (i < x - 1) {
      row.push('\n');
    }
  }
  if (x > 0) {
    console.log(row.join(''));
  }
} else {
  console.log('Missing size');
}
