/*
Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. 
The function should return true if the string is valid, and false if it's invalid.
*/


function validParentheses(parens){
  var str = parens;
  while (str.replace('()', '') !== '') { 
      str = str.replace('()', ''); 
     if (!/\(\)/g.test(str)) return false; 
   }
  return true;
}


validParentheses("(())((()())())")
// true
