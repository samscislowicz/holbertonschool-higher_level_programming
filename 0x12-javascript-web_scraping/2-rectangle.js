#!/usr/bin/node
exports.Rectangle = function Rectangle (w, h) {
  if (w <= 0) {
    let w = {};
  }
  if (h <= 0) {
    let h = {};
  } else {
    this.width = w;
    this.height = h;
  }
};