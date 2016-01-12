'use strict';

var count = 0;

var interval = setInterval(function() {
  count++;
  console.log('Jey');
}, 500);

setTimeout(function() {
  console.log('BOOM');
  clearInterval(interval);
}, 5000);

setTimeout(function() {
  for (var i = 0; i < 1234123412; i++) {
    // just wait
  }
}, 3000);

console.log('end')

// end
// Jey
// Jey
// Jey
// Jey
// Jey
// Jey
// BOOM
