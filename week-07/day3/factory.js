'use strict';

function CreateCar(color, type, km) {
  return {
    color: color,
    type: type,
    km: km,
    ride: function(km) {
      this.km += km;
    }
  };
}

var volvo = CreateCar('yelloww', 'Volvo Truck', 1e3);

volvo.ride(32);
console.log(volvo.km);
// 1032
