#!/usr/bin/node
let fs = require('fs');
let path = process.argv[2];
fs.readFile(path, 'utf8', (err, data) => {
  if (err) {
    return console.log(err);
  }
  console.log(data);
});
