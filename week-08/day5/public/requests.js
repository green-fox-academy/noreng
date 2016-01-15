'use strict';

function Request() {
  this.url = 'http://localhost:3000/todos';

  this.getAllTodoItems = function (callback) {
    return this.create('GET', this.url, null, callback);
  }

  this.postItemToServer = function (text, callback) {
    var data = JSON.stringify({ text: text });
    return this.create('POST', this.url, data , callback);
  }

  this.deleteItemFromServer = function (id, callback) {
    var url = this.url + '/' + id;
    return this.create('DELETE', url, null, callback);
  }

  this.updateItemOnServer = function (id, text, completed, callback) {
    var url = this.url + '/' + id;
    var data = JSON.stringify({ 'text': text, 'completed': completed });
    return this.create('PUT', url, data , callback);
  }

  this.create = function (method, url, data, callback) {
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
