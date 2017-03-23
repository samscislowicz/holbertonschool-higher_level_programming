#!/usr/bin/node
// Style comment?
exports.Rectangle = function Rectangle (w, h) {
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
};
