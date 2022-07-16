/*
Your task, is to create NxN multiplication table, of size provided in parameter.

for example, when given size is 3:

1 2 3
2 4 6
3 6 9

for given example, the return value should be: [[1,2,3],[2,4,6],[3,6,9]]

*/


multiplicationTable = function(size) {
var x, arr = [], arrFinal = [], copyArr;

 for (x = 1; x <= size; x++) {
  arr.push(x);
 }
 copyArr = arr.slice(0), arr = [];
 arr.push(copyArr, copyArr);

 for (x = 0; x < arr[0].length; x++) {
  for (y = 0; y < arr[1].length; y++) {
  arrFinal.push(arr[0][x] * arr[1][y]);
  }
 }
arr = [];
 for (x = 0; x < arrFinal.length; x += size) {
  arr.push(arrFinal.slice(x, x + size));
 }

return arr;
}


multiplicationTable(5)
/*
[
  [ 1, 2, 3, 4, 5 ],
  [ 2, 4, 6, 8, 10 ],
  [ 3, 6, 9, 12, 15 ],
  [ 4, 8, 12, 16, 20 ],
  [ 5, 10, 15, 20, 25 ]
]
*/
