const isTriangleNumber = n => {
  var count = 1,
      last = 0,
      left = 0;
      
  if (isNaN(n) || !(n % 1) == 0) return false;
  
  for (let x = 1; x <= n; x++) {
     if (x - last == count) {
       left = 0;
       last = x;
       count++;
     } else 
         left++;
  }
  
  return left == 0;
}



console.log(isTriangleNumber(325))
// true
