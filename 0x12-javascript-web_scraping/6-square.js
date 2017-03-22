#!/usr/bin/node
function Rectangle (w, h) {
  if (w <= 0) {
    var w = {};
  }
  if (h <= 0) {
    var h = {};
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
Square.prototype.charPrint = function (c) {
  if (c === undefined) {
    for (let i = 0; i < this.height; i++) {
      console.log(('X').repeat(this.width));
    }
  } else {
    for (let i = 0; i < this.height; i++) {
      console.log((c).repeat(this.width));
    }
  }
};
exports.Square = Square;
exports.Rectangle = Rectangle;
