#!/usr/bin/node
const FirstSquare = require('./5-square');

class Square extends FirstSquare {
  charPrint (c) {
    const character = c || 'X';
    const row = [];
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        row.push(`${character}`);
      }
      if (i < this.height - 1) {
        row.push('\n');
      }
    }
    console.log(row.join(''));
  }
}

module.exports = Square;
