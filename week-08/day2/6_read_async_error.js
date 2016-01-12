'use strict';

var fs = require('fs');

// we can't use try-catch here
fs.readFile('korte.txt', function(err, content) {
  if (err) console.log(err);
  console.log(String(content));
});
