'use strict';

var numbers = [1, 2, 3, 4];

var sum = numbers.reduce(function(acc, curr) {
  return acc + curr
});

console.log(sum);
// 10
