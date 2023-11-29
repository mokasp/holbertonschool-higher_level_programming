#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const row = [];
    for (let i = 0; i < this.height; i++) {
      if (i < this.height) {
        for (let j = 0; j < this.width; j++) { row.push('X'); }
        if (i < this.width) {
          row.push('\n');
        }
      }
    }
    console.log(row.join(''));
  }
}
module.exports = Rectangle;
