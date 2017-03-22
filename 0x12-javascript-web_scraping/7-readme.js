#!/usr/bin/node
var fs = require('fs');
let path = process.argv[2];
fs.readFile(path, 'utf8', (err, data) => {
  if (err) throw err;
  console.log(data);
});
