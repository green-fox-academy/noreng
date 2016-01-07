// Pascal Problem + Draw Pascal Triangle
// https://en.wikipedia.org/wiki/Pascal%27s_triangle#Combinations

function draw_pascal_triangle(n) {
  var triangle = stringify(pascal_triangle(n));
  return 5 < n ? replace_long_numbers(triangle) : triangle;
}

function pascal_triangle(depth) {
var triangle = [], temp_row = [];
  for (var row = 0; row < depth; row++) {
    for (var col = 0; col <= row; col++) {
      temp_row.push(calculate_nth_number(row, col));
    }
    triangle.push(temp_row);
    temp_row = [];
  }
  return triangle;
}

function calculate_nth_number(row, col) {
  return combination(row, col);
}

function combination(n, k) {
  var f = factorial;
  return f(n) / (f(k) * f(n - k));
}

function factorial(num) {
  if (num < 0) return -1;
  else if (num == 0) return 1;
  else return (num * factorial(num - 1));
}

function stringify(triangle) {
  var width = triangle.length;
  var indented = triangle.map(function(row, index) {
    var n = width - 1 - index;
    return add_n_whitespaces_to_start(n, row);
  });
  return replace_commas_with_whitespaces(indented.join('\n'));
}

function add_n_whitespaces_to_start(n, string) {
  return ' '.repeat(n) + string;
}

function replace_commas_with_whitespaces(string) {
  return string.replace(/,/g, ' ');
}

function replace_long_numbers(string) {
  return string.replace(/\d{2,}/g, '#');
}

console.log(pascal_triangle(5));
// [ [ 1 ], [ 1, 1 ], [ 1, 2, 1 ], [ 1, 3, 3, 1 ], [ 1, 4, 6, 4, 1 ] ]
console.log(draw_pascal_triangle(10));
//          1
//         1 1
//        1 2 1
//       1 3 3 1
//      1 4 6 4 1
//     1 5 # # 5 1
//    1 6 # # # 6 1
//   1 7 # # # # 7 1
//  1 8 # # # # # 8 1
// 1 9 # # # # # # 9 1
