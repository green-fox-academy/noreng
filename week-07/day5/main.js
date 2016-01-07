'use strict';

var imageSources = [
  'http://lorempixel.com/400/200/technics/1',
  'http://lorempixel.com/400/200/technics/2',
  'http://lorempixel.com/400/200/technics/3',
  'http://lorempixel.com/400/200/technics/4'
];

var currentIndex, image, buttons, thumbnails;

init();

function init() {
  currentIndex = 0;
  initDomElements();
  generateThumbnails();
  setCurrentThumbnailActive();
}

function initDomElements() {
  image = document.querySelector('.gallery');
  buttons = document.querySelector('.buttons');
  thumbnails = document.querySelector('.thumbnails');
}

buttons.addEventListener('click', function(event) {
  setIndexByDirection(event.target.id);
  displayCurrentImage();
});

thumbnails.addEventListener('mouseover', function(event) {
  if (event.target.src) {
    setIndexBySelectedThumbnail(event.target);
    displayCurrentImage();
  }
});

function setIndexByDirection(direction) {
  if (direction === 'next') {
    currentIndex++;
  } else if (direction === 'prev') {
    currentIndex--;
  }
  handleIndexOnEnds();
}

function setIndexBySelectedThumbnail(thumbnail) {
  currentIndex = getIndexOfElement(event.target);
}

function handleIndexOnEnds(index) {
  var end = imageSources.length - 1;
  if (currentIndex < 0) {
    currentIndex = end;
  } else if (end < currentIndex) {
    currentIndex = 0;
  }
}

function displayCurrentImage() {
  removeActiveClassFromThumbnails();
  setCurrentThumbnailActive();
  image.setAttribute('src', imageSources[currentIndex]);
}

function removeActiveClassFromThumbnails() {
  var active = thumbnails.querySelector(".active");
  if (active) active.classList.remove('active');
}

function setCurrentThumbnailActive() {
  var current = thumbnails.children[currentIndex];
  current.classList.add('active');
}

function generateThumbnails() {
  var thumbnail;
  imageSources.forEach(function(src) {
    thumbnail = document.createElement('img');
    thumbnail.setAttribute('src', src );
    thumbnails.appendChild(thumbnail);
  });
}

function getIndexOfElement(element) {
  var siblings = element.parentNode.childNodes;
  for (var i = 0; i < siblings.length; i++) {
    if (siblings[i] === element) {
      return i
    }
  }
}
