#!/usr/bin/node
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
};
