#!/usr/bin/node
let request = require('request');
const epId = process.argv[2];
const url = 'http://swapi.co/api/films/' + epId;
request(url, function (err, res, body) {
  if (err) {
    return console.log(err);
  }
  console.log(JSON.parse(body).title);
});
