/*
ISBN-10 identifiers are ten digits long. The first nine characters are digits 0-9. The last digit can be 0-9 or X, to indicate a value of 10.

An ISBN-10 number is valid if the sum of the digits multiplied by their position modulo 11 equals zero.
*/


function validISBN10(isbn) { 
 var sum = 0, l; 
  for(l = 0; l < isbn.length; l++) {
    let n = isbn[l];
     if(n === 'X') n = 10; 
   sum += +n * (l + 1);
  }
  return sum % 11 === 0 && /^\d{9}[\dX]$/g.test(isbn);
}


validISBN10('1112223339')
// true

validISBN10('1234512345')
// false

validISBN10('048665088X')
// true
