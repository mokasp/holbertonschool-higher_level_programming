#!/usr/bin/node
function recursive_factorial (x) {
  if (x == 0) {
    return 1;
  } else {
    return x * recursive_factorial(x - 1);
  }
}

const x = parseInt(process.argv[2]);
console.log(recursive_factorial(x));
