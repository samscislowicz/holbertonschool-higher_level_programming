#!/usr/bin/node
let fs = require('fs');
let file = process.argv[2];
let string = process.argv[3];
fs.writeFile(file, string, 'utf8', (err) => {
  if (err) {
    return console.log(err);
  }
});
