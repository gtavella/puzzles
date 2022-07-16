/*
The function 'fibonacci' should return an array of fibonacci numbers. 
The function takes a number as an argument to decide how many no. of elements to produce. 
If the argument is less than or equal to 0 then return empty array
*/


function fibonacci(n) {
  var fib = [0,1],x=2;
  while (fib.length < n) { fib[x] = fib[x-1] + fib[x-2]; x++; }
  return fib.slice(0,n);
}

fibonacci(14)
/*
[
  0,   1,  1,  2,  3,  5,
  8,  13, 21, 34, 55, 89,
  144, 233
]
*/

