'use strict';

var imageSources = [
  'http://lorempixel.com/400/200/technics/1',
  'http://lorempixel.com/400/200/technics/2',
  'http://lorempixel.com/400/200/technics/3',
  'http://lorempixel.com/400/200/technics/4',
  'http://lorempixel.com/400/200/technics/1',
];

var currentIndex, image, buttons, thumbnails;

var keyCodes = {
  left: 37,
  right: 39
}

init();

function init() {
  currentIndex = 0;
  initDomElements();
  initEvents();
  displayCurrentImage();
  generateThumbnails();
  setActiveClassToThumbnail();
}

function initDomElements() {
  image = document.querySelector('.image-wrapper');
  buttons = document.querySelector('.buttons');
  thumbnails = document.querySelector('.thumbnails');
}

function initEvents() {
  buttons.addEventListener('click', changeImageWithButtons);
  thumbnails.addEventListener('mouseover', changeImageWithThumbnails);
  document.addEventListener('keydown', changeImageWithKeys, false);
}

function generateThumbnails() {
  imageSources.forEach(function(src) {
    var thumbnail = document.createElement('img');
    thumbnail.setAttribute('src', src );
    thumbnails.appendChild(thumbnail);
  });
}

function changeImageWithButtons(event) {
  setIndexByDirection(event.target.id);
  changeCurrentImage();
}

function changeImageWithThumbnails(event) {
  if (event.target.src) {
    setIndexBySelectedThumbnail(event.target);
    changeCurrentImage();
  }
}

function changeImageWithKeys(event) {
  var keyDirection = getDirectionOfKey(event.keyCode);
  setIndexByDirection(keyDirection);
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

function getDirectionOfKey(keyCode) {
  if (keyCode === keyCodes.left) {
    return 'prev'
  } else if (keyCode === keyCodes.right) {
    return 'next'
  }
}

function changeCurrentImage() {
  removeActiveClassFromThumbnail();
  setActiveClassToThumbnail();
  displayCurrentImage();
}

function displayCurrentImage() {
  image.setAttribute('src', imageSources[currentIndex]);
}

function removeActiveClassFromThumbnail() {
  var active = thumbnails.querySelector(".active");
  active.classList.remove('active');
}

function setActiveClassToThumbnail() {
  var current = thumbnails.children[currentIndex];
  current.classList.add('active');
}

function getIndexOfDomElement(element) {
  var siblings = element.parentNode.childNodes;
  for (var i = 0; i < siblings.length; i++) {
    if (siblings[i] === element) {
      return i
    }
  }
}
