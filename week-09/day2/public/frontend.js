'use strict';

(function () {
  var form, inputField, todoItems;
  var request = new Request();

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
    todoItems.addEventListener('contextmenu', removeItem);
  }

  function getItemsFromServer() {
    request.getAllTodoItems(insertItemsToDom);
  }

  function insertItemsToDom(items) {
    items.forEach(function(item) {
      addItemToDom(item);
    });
  }

  function submitItem(event) {
    var text = inputField.value;
    if (text.length > 2) {
      request.postItemToServer(text, addItemToDom);
      inputField.value = '';
    }
    event.preventDefault();
  };

  function addItemToDom(item) {
    var element = createOneItem(item);
    todoItems.appendChild(element);
  }

  function deleteItemFromDom(item) {
    var element = document.getElementById(item.id);
    Velocity(element, 'slideUp', {duration: 500});
  }

  function createOneItem(item) {
    var element = document.createElement("li");
    if (item.completed) element.setAttribute('class', 'done');
    element.setAttribute('id', item.id);
    element.innerText = item.text;
    return element;
  }

  function changeItemStatus(event) {
    var element = event.target;
    if (element.tagName === 'LI') {
      var completed = true;
      if (element.className === 'done') completed = false;
      request.updateItemOnServer(element.id, element.innerText,
        completed, toggleItemStatus);
    }
  }

  function toggleItemStatus(changedItem) {
    var element = document.getElementById(changedItem.id);
    element.classList.toggle('done');
  }

  function removeItem(event) {
    var element = event.target;
    if (element.tagName === 'LI') {
      request.deleteItemFromServer(element.id, deleteItemFromDom);
    }
    event.preventDefault();
  }
})();
