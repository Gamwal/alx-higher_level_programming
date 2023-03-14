#!/usr/bin/node
const arr = process.argv.slice(2);
const sortedArr = arr.sort();
console.log(sortedArr);
if (arr.length === 0) {
  console.log(0);
} else if (arr.length === 1) {
  console.log(0);
} else {
  console.log(sortedArr[arr.length - 2]);
}
