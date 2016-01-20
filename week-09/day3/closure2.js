'use strict';

function createCounter(start) {
  return function () {
    start++;
    return start;
  }
}


var counter = createCounter(5);
console.log(counter());
console.log(counter());
