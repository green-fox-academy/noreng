'use strict';

var arabicToRoman = require('./kata');
var tape = require('tape');

tape('roman converter', function(t) {
  // t.equal(actual, expected);
  t.equal(arabicToRoman(0), '');
  t.equal(arabicToRoman(1), 'I');
  t.equal(arabicToRoman(2), 'II');
  t.equal(arabicToRoman(4), 'IV');
  t.equal(arabicToRoman(5), 'V');
  t.equal(arabicToRoman(6), 'VI');
  t.equal(arabicToRoman(7), 'VII');
  t.equal(arabicToRoman(8), 'VIII');
  t.equal(arabicToRoman(9), 'IX');
  t.equal(arabicToRoman(10), 'X');
  t.equal(arabicToRoman(100), 'C');
  t.equal(arabicToRoman(23), 'XXIII');
  t.equal(arabicToRoman(50), 'L');
  t.equal(arabicToRoman(53), 'LIII');
  t.equal(arabicToRoman(43), 'XLIII');
  t.equal(arabicToRoman(453), 'CDLIII');
  t.end();
});
