'use strict';

function Car(type, color, km) {
  this.type = type;
  this.color = color;
  this.km = km;
}

Car.prototype.ride = function (km) {
  this.km += km;
}

var uaz = new Car('UAZ', 'red', 300000);

uaz.ride(200);

console.log(uaz.km);
// 300200
