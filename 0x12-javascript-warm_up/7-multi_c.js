#!/usr/bin/node
const x = Math.floor(Number(process.argv[2]));
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let g = 0; g < x; g++) {
    console.log('C is fun');
  }
}
