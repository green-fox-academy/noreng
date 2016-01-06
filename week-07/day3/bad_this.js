'use strict'

var student = {
  age: 10,
  sayYourAge: sayYourAge
}

function sayYourAge() {
  console.log('I am ' + this.age);
}

student.sayYourAge()
// I am 10
sayYourAge()
// with 'use strict': 'Cannot read property 'age' of undefined'
// without 'use strict':  'I am undefined' - THAT IS DANGEROUS
