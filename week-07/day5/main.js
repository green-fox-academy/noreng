'use strict';

var imageSources = [
  'http://lorempixel.com/400/200/technics/1',
  'http://lorempixel.com/400/200/technics/2',
  'http://lorempixel.com/400/200/technics/3',
  'http://lorempixel.com/400/200/technics/4',
  'http://lorempixel.com/400/200/technics/1',
  'http://lorempixel.com/400/200/technics/2',
];

var currentIndex, image, buttons, thumbnails;

init();

function init() {
  currentIndex = 0;
  initDomElements();
  initEvents();
  displayCurrentImage();
  generateThumbnails();
  setCurrentThumbnailActive();
}

function initDomElements() {
  image = document.querySelector('.image-wrapper');
  buttons = document.querySelector('.buttons');
  thumbnails = document.querySelector('.thumbnails');
}

function initEvents() {
  buttons.addEventListener('click', buttonClickEvent);
  thumbnails.addEventListener('mouseover', thumbnailsMouseOverEvent);
  document.addEventListener('keydown', keyDownEvent, false);
}

function buttonClickEvent(event) {
  setIndexByDirection(event.target.id);
  changeCurrentImage();
}

function thumbnailsMouseOverEvent(event) {
  if (event.target.src) {
    setIndexBySelectedThumbnail(event.target);
    changeCurrentImage();
  }
}

function keyDownEvent(event) {
  setIndexByDirection(getKeyDirection(event.keyCode));
  changeCurrentImage();
}

function setIndexByDirection(direction) {
  if (direction === 'next') {
    currentIndex++;
  } else if (direction === 'prev') {
    currentIndex--;
  }
  handleIndexOnEnds();
}

function setIndexBySelectedThumbnail(thumbnail) {
  currentIndex = getIndexOfDomElement(thumbnail);
}

function handleIndexOnEnds() {
  var end = imageSources.length - 1;
  if (currentIndex < 0) {
    currentIndex = end;
  } else if (end < currentIndex) {
    currentIndex = 0;
  }
}

function changeCurrentImage() {
  removeActiveClassFromThumbnails();
  setCurrentThumbnailActive();
  displayCurrentImage();
}

function displayCurrentImage() {
  image.setAttribute('src', imageSources[currentIndex]);
}

function removeActiveClassFromThumbnails() {
  var active = thumbnails.querySelector(".active");
  active.classList.remove('active');
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

function getIndexOfDomElement(element) {
  var siblings = element.parentNode.childNodes;
  for (var i = 0; i < siblings.length; i++) {
    if (siblings[i] === element) {
      return i
    }
  }
}

function getKeyDirection(keyCode) {
  if (keyCode === 37) {
    return 'prev'
  } else if (keyCode=== 39) {
    return 'next'
  }
}
