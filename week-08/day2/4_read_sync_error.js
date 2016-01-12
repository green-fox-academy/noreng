'use strict';

var fs = require('fs');

try {
  var content = fs.readFileSync('korte.txt'); // error
}
catch (e) {
  content = 'No such file, sorry'
}

console.log(String(content));
// No such file, sorry
