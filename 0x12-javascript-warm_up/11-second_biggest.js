#!/usr/bin/node
const { argv } = require('node:process');
let largest = Number(argv[2]);
let secondLargest = 0;

if (argv.length < 4) {
  console.log('0');
}

for (const i in argv) {
  if (i > 2 && Number(argv[i]) > largest) {
    secondLargest = largest;
    largest = Number(argv[i]);
  } else if (i > 2 && Number(argv[i]) > secondLargest && Number(argv[i]) < largest) {
    secondLargest = Number(argv[i]);
  }
}

console.log(secondLargest);
