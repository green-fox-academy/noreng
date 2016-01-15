'use strict';

var basicUrl = 'http://localhost:3000/todos';

function getAllTodoItems(callback) {
  return createRequest('GET', basicUrl, null, callback);
}

function postItemToServer(text, callback) {
  var data = JSON.stringify({ text: text });
  return createRequest('POST', basicUrl, data , callback);
}

function deleteItemFromServer(id, callback) {
  var url = basicUrl + '/' + id;
  return createRequest('DELETE', url, null, callback);
}

function updateItemOnServer(id, text, completed, callback) {
  var url = basicUrl + '/' + id;
  var data = JSON.stringify({ 'text': text, 'completed': completed });
  return createRequest('PUT', url, data , callback);
}

function createRequest(method, url, data, callback) {
  var req = new XMLHttpRequest();
  req.open(method, url);
  req.setRequestHeader('Content-Type', 'application/json');
  req.send(data);
  req.onreadystatechange = function () {
    if (req.readyState === 4) {
      var res = JSON.parse(req.response);
      return callback(res);
    }
  };
}
