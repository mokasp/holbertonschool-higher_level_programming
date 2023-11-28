#!/usr/bin/node
const x = process.argv[2];
let row = []
for (var i = 0; i < x; i++){ // iterates rows
    for (var j = 0; j < x; j++) // iterates * in row
        row.push('X')
    if (i < x - 1) {
        row.push('\n')
    }
}
console.log(row.join(""))
