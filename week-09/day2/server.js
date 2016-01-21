'use strict'

var express = require('express');
var bodyParser = require('body-parser');
var database = require('./database_requests.js');

var app = express();

app.use(logRequest);
app.use(express.static('public'));
app.use(bodyParser.json());

app.get('/todos', function (req, res) {
  database.getItems(function (allItems) {
    res.status(200).json(allItems);
  });
});

app.get('/todos/:id', function (req, res) {
  findItem(req, res, function (item) { res.json(item); });
});

app.post('/todos', function (req, res) {
  var attributes = req.body;
  database.addItem(attributes, function (newItem) {
    res.status(200).json(newItem);
  });
});

app.put('/todos/:id', function (req, res) {
  var attributes = req.body;
  findItem(req, res, function (item) {
    database.updateItem(item.id, attributes, function (updatedItem) {
      res.status(200).json(updatedItem);
    });
  });
});

app.delete('/todos/:id', function (req, res) {
  findItem(req, res, function (item) {
    database.removeItem(item.id, function () {
      res.status(200).json(item);
    });
  });
});

app.listen(3000, function () {
  console.log('Listening on port 3000...');
});

function findItem(req, res, callback) {
  var id = parseInt(req.params.id);
  database.getOneItem(id, function (item) {
    if (item) {
      callback(item);
    } else {
      res.status(401).json({error: 'Item not found'})
    }
  });
}

function logRequest(req, res, next) {
  var parts = [
    new Date(),
    req.method,
    req.originalUrl,
  ];
  console.log(parts.join(' '));
  next();
}
