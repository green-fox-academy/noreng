'use-strict'

var TodoItem = function () {
  this.id = nextId();
  this.text = '';
  this.completed = false;
}

TodoItem.prototype.update = function(attributes) {
  this.text = attributes.text || '';
  this.completed = !!attributes.completed;
};

var currId = 0;
function nextId() {
  return ++currId;
}


function getItem(id) {
  return items[id];
}

function addItem(attributes) {
  var item = new TodoItem();
  item.update(attributes);
  items[item.id] = item;
  return item;
}

function removeItem(id) {
  delete items[id];
}

function allItems() {
  var values = [];
  for (id in items) {
    values.push(items[id]);
  }
  return values;
}

module.exports = {
  get: getItem,
  add: addItem,
  remove: removeItem,
  all: allItems,
};


// how it works
var items = {};
//
// addItem({text: 'Buy milk'});
// addItem({text: 'Make dinner'});
// addItem({text: 'Save the world'});
//
//
// console.log(items);
