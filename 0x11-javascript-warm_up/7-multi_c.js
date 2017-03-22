#!/usr/bin/node
let x = parseInt(process.argv[2]);
let c = 'C is fun';
if (isNaN(x) === true) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i < x; i++) {
  console.log(c);
}
