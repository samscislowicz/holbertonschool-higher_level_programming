#!/usr/bin/node
exports.Rectangle = function Rectangle (w, h) {
  if (w <= 0) {
    return;
  }
  if (h <= 0) {

  } else {
    this.width = w;
    this.height = h;
  }
};
