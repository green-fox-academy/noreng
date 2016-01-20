'use strict';

function createCounter() {
  var count = 0;
  return function () {
    count++;
    return count;
  }
}

var counter = createCounter();

console.log(counter());
