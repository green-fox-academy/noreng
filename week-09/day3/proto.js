'use strict';

function PowerRanger(color) {
  this.color = color;
}

var proto = {isPowerfull: true};

PowerRanger.prototype = proto;

var yellowRanger = new PowerRanger('yellow');

console.log(yellowRanger.color);
console.log(yellowRanger.isPowerfull);
// yellow
// true
