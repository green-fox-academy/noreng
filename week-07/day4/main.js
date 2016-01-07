'use strict';

var title = document.querySelector('.mainTitle');
title.classList.add('red')

// edit existing element's attribute
var image = document.querySelector('.goat');
image.setAttribute('src', 'img/goat.jpg');

// add new element to the DOM 10 times
var body = document.querySelector('body');

for (var i = 0; i < 10; i++) {
  createNewImage('img/apple.jpg');
}

function createNewImage(src) {
  var image = document.createElement('img');
  image.setAttribute('src', src );
  body.appendChild(image);
}

// add new elements to the DOM from an array
var images = [
  'http://lorempixel.com/400/200/technics/1',
  'http://lorempixel.com/400/200/technics/2',
  'http://lorempixel.com/400/200/technics/3',
  'http://lorempixel.com/400/200/technics/4',
  'http://lorempixel.com/400/200/technics/5',
  'http://lorempixel.com/400/200/technics/6',
  'http://lorempixel.com/400/200/technics/7',
  'http://lorempixel.com/400/200/technics/8',
  'http://lorempixel.com/400/200/technics/9',
  'http://lorempixel.com/400/200/technics/10'
];

for (var i = 0; i < images.length; i++) {
  createNewImage(images[i]);
}

// button
var buttonAnimals = document.querySelector('.animals');
var buttonPeople = document.querySelector('.people');
// var button3 = document.querySelector('.people');

var gallery = document.querySelector('.gallery');

buttonAnimals.addEventListener('click', function() {
  gallery.setAttribute('src', 'http://lorempixel.com/400/200/animals')
});

buttonPeople.addEventListener('click', function() {
  gallery.setAttribute('src', 'http://lorempixel.com/400/200/people')
});



// scroll EventListener
window.addEventListener('scroll', function() {
  console.log('scroll', window.scrollY);
})
