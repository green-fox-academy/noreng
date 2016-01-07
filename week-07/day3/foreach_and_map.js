'use strict';

var weirdWords = [
  'kuty',
  'macsk',
  'alm',
  'kacs'
];

// foreach
var coolWords = [];
weirdWords.forEach(function(word) {coolWords.push(word + 'a')});

// map
var coolWords2 = weirdWords.map(function(word) {return word + 'a'});

console.log(coolWords);
console.log(coolWords2);
// [ 'kutya', 'macska', 'alma', 'kacsa' ]
// [ 'kutya', 'macska', 'alma', 'kacsa' ]
