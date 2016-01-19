'use strict';

function Request() {
  this.url = 'http://localhost:3000/todos/';

  this.getAllTodoItems = function (callback) {
    return this.createRequest('GET', this.url, null, callback);
  }

  this.postItemToServer = function (text, callback) {
    var data = JSON.stringify({ 'text': text });
    return this.createRequest('POST', this.url, data, callback);
  }

  this.deleteItemFromServer = function (id, callback) {
    var url = this.url + id;
    return this.createRequest('DELETE', url, null, callback);
  }

  this.updateItemOnServer = function (id, text, status, callback) {
    var url = this.url + id;
    var data = JSON.stringify({ 'text': text, 'completed': status });
    return this.createRequest('PUT', url, data, callback);
  }

  this.createRequest = function (method, url, data, callback) {
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
}
