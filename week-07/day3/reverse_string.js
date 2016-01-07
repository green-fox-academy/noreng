'use strict'

function reverse(s) {
  s = s.split('');
  var len = s.length,
      halfIndex = Math.floor(len / 2) - 1,
      tmp;
  for (var i = 0; i <= halfIndex; i++) {
    tmp = s[len - i - 1];
    s[len - i - 1] = s[i];
    s[i] = tmp;
  }
  return s.join('');
}

console.log(reverse('kacsamajom'));
// mojamascak

function reverseRecursive(string) {
  var index = string.length - 1;
  return reverse(string, index);

  function reverse(str, i) {
    if (i < 0) {
      return ''
    } else {
      return str[i] + reverse(str, i - 1)
    }
  }
}

console.log(reverseRecursive('kacsa'));
// ascak

function reverseRecursive2(s) {
  return (s === '') ? '' : reverse(s.substr(1)) + s.charAt(0);
}

console.log(reverseRecursive2('kacsa'));
// ascak
