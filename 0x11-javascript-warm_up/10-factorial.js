#!/usr/bin/node
let n = parseInt(process.argv[2]);
function factorial (n) {
  if (n === 0) {
    return 1;
  } if (isNaN(n) === true) {
    return 1;
  }
  return n * factorial(n - 1);
}
console.log(factorial(n));
