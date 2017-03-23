#!/usr/bin/node
let request = require('request');
let fs = require('fs');
let url = process.argv[2];
let path = process.argv[3];
request(url, (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  fs.writeFile(path, body, 'utf8', (err) => {
    if (err) {
      return console.log(err);
    }
  });
});
