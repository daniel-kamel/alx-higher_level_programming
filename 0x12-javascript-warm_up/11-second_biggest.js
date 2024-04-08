#!/usr/bin/node
const { argv } = require('node:process');
let largest = Number(argv[2]);
let secondLargest = Number(argv[3]);

if (argv.length < 4) {
  console.log('0');
}

for (let i = 3; i < argv.length; i++) {
  if (i > 2 && Number(argv[i]) > largest) {
    secondLargest = largest;
    largest = Number(argv[i]);
  } else if (i > 2 && Number(argv[i]) > secondLargest && Number(argv[i]) < largest) {
    secondLargest = Number(argv[i]);
  }
}

console.log(secondLargest);
