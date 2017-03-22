#!/usr/bin/node
let x = parseInt(process.argv[2]);
let c = 'X'.repeat(x);
let d = c + '\n'
while (isNaN(x) === true) {
  console.log('Missing size');
}
if (isNaN(x) === false) {
  console.log(d.repeat(x).replace(/\n$/, ''));
}
