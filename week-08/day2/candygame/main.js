'use strict';

var candies, lollipops, lollipopPrice, currentSpeed;
var candiesQty, lollipopsQty, speed;
var btnCreateCandy, btnBuyLollipop;

init();

function init() {
  candies = 0;
  lollipops = 0;
  lollipopPrice = 10;
  initDomElements();
  initEvents();
}

function initDomElements() {
  candiesQty = document.querySelector('.candies');
  lollipopsQty = document.querySelector('.lollipops');
  speed = document.querySelector('.speed');
  btnCreateCandy = document.querySelector('.btn-create-candy');
  btnBuyLollipop = document.querySelector('.btn-buy-lollipop');
}

function initEvents() {
  btnCreateCandy.addEventListener('click', createCandies);
  btnBuyLollipop.addEventListener('click', buyLollipop);
}

function restart() {
  init();
  updateAllStats();
}

function createCandies() {
  candies++;
  updateCandies();
}

function buyLollipop() {
  if (lollipopPrice <= candies) {
    candies -= lollipopPrice;
    lollipops++;
    updateAllStats();
  }
  if (lollipops === 10) {
    autoChangeCandiesBySpeed()
  }
}

function updateAllStats() {
  updateCandies();
  updateLollipops();
  updateSpeed();
}

function updateCandies() {
  candiesQty.innerHTML = candies;
  checkWinnerCandiesQty();
}

function updateLollipops() {
  lollipopsQty.innerHTML = lollipops;
}

function updateSpeed() {
  speed.innerHTML = getSpeed();
}

function getSpeed() {
  return Math.floor(lollipops / 10);
}

function autoChangeCandiesBySpeed() {
  setInterval(changeCandiesBySpeed, 1000);
}

function changeCandiesBySpeed() {
  candies += getSpeed();
  updateCandies();
}

function checkWinnerCandiesQty() {
  if (candies >= 10000) {
    alert('You won!');
    restart();
  }
}
