#!/usr/bin/node
exports.Rectangle = function Rectangle (w, h) {
  if (w <= 0) {
    var w = {};
  }
  if (h <= 0) {
    var h = {};
  } else {
    this.width = w;
    this.height = h;
  }
};
