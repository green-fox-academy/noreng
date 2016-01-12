'use strict';

function Game() {
  var _this = this;
  this.candies;
  this.lollipops;
  this.lollipopPrice;
  this.currentSpeed;
  this.candiesQty;
  this.lollipopsQty;
  this.speed;
  this.btnCreateCandy;
  this.btnBuyLollipop;

  this.init = function() {
    this.candies = 0;
    this.lollipops = 0;
    this.lollipopPrice = 10;
    this.initDomElements();
    this.initEvents();
  }

  this.initDomElements = function() {
    this.candiesQty = document.querySelector('.candies');
    this.lollipopsQty = document.querySelector('.lollipops');
    this.speed = document.querySelector('.speed');
    this.btnCreateCandy = document.querySelector('.btn-create-candy');
    this.btnBuyLollipop = document.querySelector('.btn-buy-lollipop');
  }

  this.initEvents = function() {
    this.btnCreateCandy.addEventListener('click', this.createCandies);
    this.btnBuyLollipop.addEventListener('click', this.buyLollipop);
  }

  this.restart = function() {
    this.init();
    this.updateAllStats();
  }

  this.createCandies = function() {
    _this.candies++;
    _this.updateCandies();
  }

  this.buyLollipop = function() {
    if (_this.lollipopPrice <= _this.candies) {
      _this.candies -= _this.lollipopPrice;
      _this.lollipops++;
      _this.updateAllStats();
    }
    if (_this.lollipops === 10) {
      _this.autoChangeCandiesBySpeed()
    }
  }

  this.updateAllStats = function() {
    this.updateCandies();
    this.updateLollipops();
    this.updateSpeed();
  }

  this.updateCandies = function() {
    this.candiesQty.innerHTML = this.candies;
    this.checkWinnerCandiesQty();
  }

  this.updateLollipops = function() {
    this.lollipopsQty.innerHTML = this.lollipops;
  }

  this.updateSpeed = function() {
    this.speed.innerHTML = this.getSpeed();
  }

  this.getSpeed = function() {
    return Math.floor(this.lollipops / 10);
  }

  this.autoChangeCandiesBySpeed = function() {
    setInterval(this.changeCandiesBySpeed, 1000);
  }

  this.changeCandiesBySpeed = function() {
    _this.candies += _this.getSpeed();
    _this.updateCandies();
  }

  this.checkWinnerCandiesQty = function() {
    if (this.candies >= 10000) {
      alert('You won!');
      this.restart();
    }
  }
}

var game = new Game();
game.init();
