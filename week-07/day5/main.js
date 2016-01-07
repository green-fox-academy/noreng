'use strict';

var imageIndex = 0;

var images = [
  'http://lorempixel.com/400/200/technics/1',
  'http://lorempixel.com/400/200/technics/2',
  'http://lorempixel.com/400/200/technics/3',
  'http://lorempixel.com/400/200/technics/4'
];

var bigPicture = document.querySelector('.gallery');
var leftButton = document.querySelector('.left');
var rightButton = document.querySelector('.right');
var thumbnails = document.querySelector('.thumbnails');

leftButton.addEventListener('click', function() {
  if (imageIndex > 0) {
    imageIndex--;
  } else {
    imageIndex = images.length - 1;
  }
  displayCurrentImage();
});

rightButton.addEventListener('click', function() {
  if (imageIndex < images.length - 1) {
    imageIndex++;
  } else {
    imageIndex = 0;
  }
  displayCurrentImage();
});

thumbnails.addEventListener('mouseover', function(event) {
  if (event.target.src) {
    var src = event.target.src;
    imageIndex = getIndexOfElement(event.target);
    displayCurrentImage();
  }
});

(function generateThumbnails(src) {
  var thumbnail;
  for (var i = 0; i < images.length; i++) {
    thumbnail = document.createElement('img');
    thumbnail.setAttribute('src', images[i] );
    thumbnails.appendChild(thumbnail);
  }
  setCurrentThumbnailActive()
})()

function displayCurrentImage() {
  setCurrentThumbnailActive();
  bigPicture.setAttribute('src', images[imageIndex]);
}

function setCurrentThumbnailActive() {
  removeActiveClassFromThumbnails();
  var current = thumbnails.children[imageIndex];
  current.classList.add('active');
}

function removeActiveClassFromThumbnails() {
  var active = thumbnails.querySelector(".active");
  if (active) active.classList.remove('active');
}

function getIndexOfElement(element) {
  var siblings = element.parentNode.childNodes;
  for (var i = 0; i < siblings.length; i++) {
    if (siblings[i] === element) {
      return i
    }
  }
}
