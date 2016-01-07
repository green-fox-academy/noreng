'use strict';

var currentIndex = 0;

var images = [
  'http://lorempixel.com/400/200/technics/1',
  'http://lorempixel.com/400/200/technics/2',
  'http://lorempixel.com/400/200/technics/3',
  'http://lorempixel.com/400/200/technics/4'
];

var bigPicture = document.querySelector('.gallery');
var buttons = document.querySelector('.buttons');
var thumbnails = document.querySelector('.thumbnails');

buttons.addEventListener('click', function(event) {
  setIndexByDirection(event.target.id);
  displayCurrentImage();
});

function setIndexByDirection(direction) {
  if (direction === 'next') {
    currentIndex++;
  } else if (direction === 'prev') {
    currentIndex--;
  }
  handleIndexOnEnds();
}

function handleIndexOnEnds(index) {
  var end = images.length - 1;
  if (currentIndex < 0) {
    currentIndex = end;
  } else if (end < currentIndex) {
    currentIndex = 0;
  }
}

thumbnails.addEventListener('mouseover', function(event) {
  if (event.target.src) {
    var src = event.target.src;
    currentIndex = getIndexOfElement(event.target);
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
  removeActiveClassFromThumbnails();
  setCurrentThumbnailActive();
  bigPicture.setAttribute('src', images[currentIndex]);
}

function removeActiveClassFromThumbnails() {
  var active = thumbnails.querySelector(".active");
  if (active) active.classList.remove('active');
}

function setCurrentThumbnailActive() {
  var current = thumbnails.children[currentIndex];
  current.classList.add('active');
}

function getIndexOfElement(element) {
  var siblings = element.parentNode.childNodes;
  for (var i = 0; i < siblings.length; i++) {
    if (siblings[i] === element) {
      return i
    }
  }
}
