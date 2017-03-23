#!/usr/bin/node
var concat = require('concat-files');
let firstfile = process.argv[2];
let secondfile = process.argv[3];
let destination = process.argv[4];
concat([
  firstfile,
  secondfile
], destination, function (err) {
  if (err) throw err;
  console.log('done');
});
