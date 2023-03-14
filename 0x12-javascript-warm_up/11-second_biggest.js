#!/usr/bin/node
const arr = process.argv.slice(2).map(Number);
const sortedArr = arr.sort(function (a, b) {
  return a - b;
});
if (arr.length === 0) {
  console.log(0);
} else if (arr.length === 1) {
  console.log(0);
} else {
  console.log(sortedArr[arr.length - 2]);
}
