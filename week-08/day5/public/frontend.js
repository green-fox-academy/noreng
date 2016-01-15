'use strict';

var form;
var inputField;
var todoItems;

init();

function init() {
  initDomElements();
  initEvents();
  getItemsFromServer();
}

function initDomElements() {
  form = document.querySelector('form');
  inputField = document.querySelector('input');
  todoItems = document.querySelector('.todo-items');
}

function initEvents() {
  form.addEventListener('submit', submitItem, false);
  todoItems.addEventListener('click', changeItemStatus);
  todoItems.addEventListener('dblclick', removeItem);
}

// Request
function getItemsFromServer() {
  getAllTodoItems(insertItemsToDom);
}

// Dom action
function insertItemsToDom(items) {
  items.forEach(function(item) {
    addItemToDom(item.id, item.text, item.completed);
  });
}

// Event
function submitItem(event) {
  var text = inputField.value;
  if (text.length > 2) {
    postItemToServer(text, addItemToDom);
    inputField.value = '';
  }
  event.preventDefault();
};

// Dom action
function addItemToDom(id, text, completed) {
  var item = createOneItem(id, text, completed);
  todoItems.appendChild(item);
}

// Dom action
function deleteItemFromDom(id) {
  var item = document.getElementById(id);
  item.remove();
}

// Dom action
function createOneItem(id, text, completed) {
  var item = document.createElement("li");
  if (completed) item.setAttribute('class', 'done');
  item.setAttribute('id', id);
  item.innerText = text;
  return item;
}

// Event
function changeItemStatus(event) {
  var item = event.target;
  if (item.tagName === 'LI') {
    var completed = true;
    if (item.className === 'done') completed = false;
    updateItemOnServer(item.id, item.innerText, completed, toggleItemStatus);
  }
}

// Dom action
function toggleItemStatus(changedItem) {
  var item = document.getElementById(changedItem.id);
  item.classList.toggle('done');
}

// Event
function removeItem(event) {
  var item = event.target;
  if (item.tagName === 'LI') {
    deleteItemFromServer(item.id, deleteItemFromDom);
  }
}
