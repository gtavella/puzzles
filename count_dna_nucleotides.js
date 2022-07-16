/*
For a given DNA genetic code represented by a string, count the number of times the letters A (adenine), C (cytosine), G (guanine) and T (thymine) appears and return and object.

The input string may contain both upper and lower case characters.
*/

function getCountedNucleotides(genCode){
   function get(l) {
     var rx = new RegExp(l ,'gi');
     return genCode.match(rx) ? genCode.match(rx).length : 0;
   }
  return {
   A: get('A'),
   C: get('C'),
   G: get('G'),
   T: get('T')
  };
}


var genCode = 'aCCggT';
getCountedNucleotides(genCode)
// return {A: 1, C: 2, G: 2, T: 1}
