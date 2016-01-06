'use strict';

function Car(color, type, km) {
  this.color = color;
  this.type = type;
  this.km = km;
  this.ride = function(km) {
    this.km += km;
  }
}

var golf = new Car('grey', 'III', 123000);

golf.ride(400);
console.log(golf.km);
// 123400
