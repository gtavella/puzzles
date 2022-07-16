/*
In this kata you have to extend the dictionary with a method, that returns a list of words matching a pattern. 
This pattern may contain letters (lowercase) and placeholders ("?"). A placeholder stands for exactly one arbitrary letter.
*/


function Dictionary(words) {
  this.words = words;
}

Dictionary.prototype.getMatchingWords = function(pattern) {
 var rx = /\?/g, matches = [], pattern_orig = pattern;
  
  for (let w = 0; w < this.words.length; w++) {
     while (rx.exec(pattern)) {
       pattern = pattern.replace(/\?/, this.words[w][rx.lastIndex-1]);
     }
     if (pattern === this.words[w]) { matches.push(pattern); }    
    pattern = pattern_orig;
  }
 return matches;
}



var fruits = new Dictionary(['banana', 'apple', 'papaya', 'cherry']);

fruits.getMatchingWords('lemon');     
// []
fruits.getMatchingWords('cherr??');   
// []
fruits.getMatchingWords('?a?a?a');    
// ['banana', 'papaya']
fruits.getMatchingWords('??????');    
// ['banana', 'papaya', 'cherry']
