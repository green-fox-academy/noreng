'use strict';
// https://market.mashape.com/ismaelc/yoda-speak/overview

var ACCESS_TOKEN = 'JNDzfN0Pz8mshV6DHISeFTRHJy00p1LvLoKjsnSUpz0krIeYGX';

var yodaInput = document.querySelector('.yoda-input');
var yodaButton = document.querySelector('.yoda-button');
var responseContainer = document.querySelector('.yoda-response');

function createUrl() {
  var url = 'https://yoda.p.mashape.com/yoda';
  var sentence = yodaInput.value;
  return url + '?sentence=' + encodeURIComponent(sentence);
}

yodaButton.addEventListener('click' , function() {
  responseContainer.innerText = 'loading...';
  createRequest(createUrl(), onDone);
});

function createRequest(url, callback) {
  var testRequest = new XMLHttpRequest();
  testRequest.open('GET', url);
  testRequest.setRequestHeader('X-Mashape-Key', ACCESS_TOKEN);
  testRequest.send();
  testRequest.onreadystatechange = function () {
    if (testRequest.readyState === 4) {
      callback(testRequest.response);
    }
  };
}

function onDone(response) {
  responseContainer.innerText = response;
}
