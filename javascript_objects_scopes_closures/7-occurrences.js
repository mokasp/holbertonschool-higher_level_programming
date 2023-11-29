#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occurance = 0;
  for (const element of list) {
    if (element === searchElement) {
      occurance++;
    }
  }
  return occurance;
};
