'use strict';

var timeout = setTimeout(function() {
  console.log('Jey');
}, 10000)

console.log('end')

clearTimeout(timeout);
// end
// 0sec later...
// 
