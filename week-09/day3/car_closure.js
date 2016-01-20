'use strict';

function createCar(color, type, km) {
  function ride(distance) {
    km += distance;
  }

  function getKm() {
    return km;
  }

  return {
    ride: ride,
    getKm: getKm
  }
}

var opel = createCar('red', 'Astra', 4000);
opel.ride(333);

console.log(opel.getKm());
// 4333
