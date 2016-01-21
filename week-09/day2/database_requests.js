var mysql = require('mysql');

var connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'test2',
  password : 'test2',
  database : 'my_todo'
});

connection.connect();

function getItems(callback) {
  var sql = 'SELECT id, text, completed FROM `todos`';
  connection.query(sql, function(err, res) {
    if (err) throw err;
    var items = res;
    callback(items);
  });
}

function getOneItem(id, callback) {
  var sql = 'SELECT id, text, completed FROM `todos` WHERE id=?';
  connection.query(sql, id, function(err, res) {
    if (err) throw err;
    var item = res[0];
    callback(item);
  });
}

function addItem(attributes, callback) {
  var sql = 'INSERT INTO `todos` SET ?';
  connection.query(sql, attributes, function(err, res) {
    if (err) throw err;
    var newId = res.insertId;
    getOneItem(newId, callback);
  });
}

function updateItem(id, attributes, callback) {
  var sql = 'UPDATE `todos` SET ?? = ?, ?? = ? WHERE id=?';
  var inserts = ['text', attributes.text, 'completed', attributes.completed, id];
  connection.query(mysql.format(sql, inserts), function(err, res) {
    if (err) throw err;
    getOneItem(id, callback);
  });
}

function removeItem(id, callback) {
  var sql = 'DELETE FROM `todos` WHERE `id`= ?';
  connection.query(sql, id, function(err, res) {
    if (err) throw err;
    callback();
  });
}

module.exports = {
  getItems: getItems,
  getOneItem: getOneItem,
  addItem: addItem,
  updateItem: updateItem,
  removeItem: removeItem
};
