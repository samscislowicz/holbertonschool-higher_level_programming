#!/usr/bin/node
let x = parseInt(process.argv[2]);
let c = 'C is fun\n'.repeat(x);
while (isNaN(x) === true) {
  console.log('Missing number of occurrences');
}
if (isNaN(x) === false) {
  console.log(c.replace(/\n$/, ''));
}
