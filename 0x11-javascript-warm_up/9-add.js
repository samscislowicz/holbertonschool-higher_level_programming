#!/usr/bin/node
let a = parseInt(process.argv[2]);
let b = parseInt(process.argv[3]);
const x = add(a, b);
function add (a, b) {
  return a + b;
}
console.log(x);
