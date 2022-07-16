/*
The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once 
in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.
*/


function duplicateEncode(word) {
 var s = '', word = word.toLowerCase(), w;
  for (w = 0; w < word.length; w++) {
    s += word.indexOf(word[w]) !== word.lastIndexOf(word[w]) ? ')' : '(' ;
  }
  return s;
}


duplicateEncode("din")
//  "((("

duplicateEncode("recede")
//  "()()()"

duplicateEncode("Success")
//  ")())())"

duplicateEncode("(( @")
// "))((" 
