#!/usr/bin/node
if (process.argv.length < 4) {
  console.log('0');
} else {
  console.log(process.argv.slice(2, process.argv.length).sort()[process.argv.length - 4]);
}
