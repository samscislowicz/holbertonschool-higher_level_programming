#!/usr/bin/node
const param1 = parseInt(process.argv[2]);
if (isNaN(param1) === true) {
  console.log('Not a number');
} else {
  console.log('My number: ' + param1);
}
