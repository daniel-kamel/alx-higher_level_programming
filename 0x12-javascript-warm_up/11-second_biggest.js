#!/usr/bin/node
const { argv } = require('node:process');
if (argv.length < 4) {
  console.log('0');
} else {
  const list = argv.sort();
  console.log(list.reverse()[2]);
}
