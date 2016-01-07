'use strict';

function Student() {
  this.grades = [];

  this.addGrade = function(grade) {
    return this.grades.push(grade)
  };

  this.getAverage = function() {
    var sum = this.grades.reduce(function(a,b) {
      return a + b
    });
    return sum / this.grades.length
  };
}

var jozsi = new Student();

jozsi.addGrade(4);
jozsi.addGrade(3);
jozsi.addGrade(5);
jozsi.addGrade(5);

console.log(jozsi.getAverage());
// 4.25
