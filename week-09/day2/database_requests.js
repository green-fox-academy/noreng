var mysql      = require('mysql');

var connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'test2',
  password : 'test2',
  database : 'my_todo'
});

connection.connect();

function getItems(callback) {
  var sql = 'SELECT id, text, completed FROM `todos`'
  connection.query(sql, function(err, res) {
    if (err) throw err;
    var items = res;
    callback(items);
  });
}

function addItem(attributes, callback) {
  connection.query('INSERT INTO `todos` SET ?', attributes, function(err, res) {
    if (err) throw err;
    var newItem = {
      'id': res.insertId,
      'text': attributes.text,
      'completed': false
      };
    callback(newItem);
  });
}

function updateItem(id, attributes, callback) {
  var sql = 'UPDATE `todos` SET ?? = ?, ?? = ? WHERE id=?';
  var inserts = ['text', attributes.text, 'completed', attributes.completed, id]
  connection.query(mysql.format(sql, inserts), function(err, res) {
    if (err) throw err;
    var updatedItem = {
      'id': id,
      'text': attributes.text,
      'completed': attributes.completed
      };
    callback(updatedItem);
  });
}

function removeItem(id, callback) {
  connection.query('DELETE FROM `todos` WHERE `id`= ?', id, function(err, res) {
    if (err) throw err;
    var removed = {'id': id}
    callback(removed);
  });
}

module.exports = {
  getItems: getItems,
  addItem: addItem,
  updateItem: updateItem,
  removeItem: removeItem
};
