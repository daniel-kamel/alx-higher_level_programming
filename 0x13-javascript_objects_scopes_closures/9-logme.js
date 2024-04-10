#!/usr/bin/node
let printedNo = 0;
exports.logMe = function (item) {
  console.log(`${printedNo}: ${item}`);
  printedNo += 1;
};
