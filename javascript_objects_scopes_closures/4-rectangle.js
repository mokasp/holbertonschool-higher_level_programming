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
      for (let j = 0; j < this.width; j++) {
        row.push('X');
      }
      if (i < this.height - 1) {
        row.push('\n');
      }
    }
    console.log(row.join(''));
  }

  rotate () {
    this.w = this.width;
    this.h = this.height;
    this.width = this.h;
    this.height = this.w;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
