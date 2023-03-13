#!/usr/bin/node
const conv = parseInt(process.argv[2], 10);
if (isNaN(conv)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < conv; i++) {
    console.log('X'.repeat(conv));
  }
}
