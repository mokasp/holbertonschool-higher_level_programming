#!/usr/bin/node
function recursiveFactorial (x) {
  if (isNaN(x)) {
    return 1;
  } else if (x === 0) {
    return 1;
  } else {
    return x * recursiveFactorial(x - 1);
  }
}

const x = parseInt(process.argv[2]);
console.log(recursiveFactorial(x));
