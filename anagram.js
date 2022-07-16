/*
What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:

'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false

'abba' & 'abca' == false
Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. For example:

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
*/


function anagrams(word, words) {
  var arr = [];
  words.forEach(function(e1){
    if ( e1.split('').sort().every(function(e2,i2){ 
      return word.split('').sort()[i2] === e2;
    }) ) { arr.push(e1); }
  });
  return arr;
}


anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])
// [ 'aabb', 'bbaa' ]
