#!/usr/bin/node
const { argv } = require('node:process');
function getList (argv) {
  const list = [];
  if (argv.length < 4) {
    return 0;
  }
  for (let i = 2; i < argv.length; i++) {
    list.push(Number(argv[i]));
  }
  return list;
}

function secondBiggest (list) {
  if (list === 0) {
    return 0;
  }
  list.sort(function (a, b) { return a - b; });
  return list.reverse()[1];
}

console.log(secondBiggest(getList(argv)));
