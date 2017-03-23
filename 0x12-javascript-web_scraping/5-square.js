#!/usr/bin/node
function Rectangle (w, h) {
  if (w <= 0) {
      return;
  }
  if (h <= 0) {
      return;
  } else {
    this.width = w;
    this.height = h;
  }
  this.print = function () {
    for (let i = 0; i < this.height; i++) {
      console.log(('X').repeat(this.width));
    }
  };
  this.rotate = function () {
    this.height = w;
    this.width = h;
  };
  this.double = function () {
    this.height = h += h;
    this.width = w += w;
  };
}
function Square (size) {
  Rectangle.call(this, size, size);
}
exports.Square = Square;
exports.Rectangle = Rectangle;
