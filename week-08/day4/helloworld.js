'use strict';

var express = require('express');
var url = require('url');
var bodyParser = require('body-parser');

var app = express();
// parse application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: false }));
 // parse application/json
app.use(bodyParser.json());

// GET/
app.get('/', function (req, res) {
  res.send('Hello World');
})

// GET/add?a=1&b=5
app.get('/add', function(req, res) {
  var urlParts = url.parse(req.url, true);
  var query = urlParts.query;

  var a = parseInt(query['a']);
  var b = parseInt(query['b']);
  var result = a + b;
  res.send(result.toString() + '\n');
});

// POST
app.post('/add', function (req, res) {
  var body = req.body;

  var a = parseInt(body['a']);
  var b = parseInt(body['b']);
  var result = a + b;
  res.send(result.toString() + '\n');
  console.log(result);

  res.status(204).end();
});

// GET/norbi
app.get('/:name', function(req, res) {
  var name = req.params['name'];
  console.log('Name: ' + name);
});

app.listen(3000);
