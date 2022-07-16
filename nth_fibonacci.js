/*
I love Fibonacci numbers in general, but I must admit I love some more than others.

I would like for you to write me a function that when given a number (n) returns the n-th number in the Fibonacci Sequence.
*/

function nthFibo(n) {
  var fib = [0,1], x=2;
  while(fib.length <=n){ fib[x]= fib[x-1] + fib[x-2]; x++; }
  return fib[n-1];
}

nthFibo(13)
// 144
