#!/usr/bin/node
const x = process.argv[2];
let row = []
for (let i = 0; i < x; i++){ 
    for (let j = 0; j < x; j++)
        row.push('X')
    if (i < x - 1) {
        row.push('\n')
    }
}
if (x > 0) { 
    console.log(row.join(""))
}
