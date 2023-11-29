#!/usr/bin/node
const args = process.argv;
args.splice(0, 2);
const length = args.length;
if (length === 0) {
  console.log(0);
} else if (length === 1) {
  console.log(0);
} else {
  args.sort();
  console.log(args[length - 2]);
}
