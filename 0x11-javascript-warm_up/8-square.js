#!/usr/bin/node
let x = parseInt(process.argv[2]);
let c = 'X'.repeat(x);
if (isNaN(x) === true) {
  console.log('Missing size');
}
for (let i = 0; i < x; i++) {
  console.log(c);
}
