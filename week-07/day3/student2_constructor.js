'use strict';

var dezso = new Student();

dezso.addGrade('math', 5);
dezso.addGrade('math', 4);
dezso.addGrade('math', 4);
dezso.addGrade('arts', 1);
dezso.addGrade('arts', 3);
dezso.getCount()  // {'maths': 3, 'arts' : 2}
dezso.getAverage() // 3.4

dezso.getAverageBySubject() // {'maths': 4.3, 'arts' : 2}
