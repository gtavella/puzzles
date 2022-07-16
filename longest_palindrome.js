/*
Longest Palindrome
Find the length of the longest substring in the given string s that is the same in reverse.

As an example, if the input was “I like racecars that go fast”, the substring (racecar) length would be 7.

If the length of the input string is 0, the return value must be 0.
*/




Array.prototype.max = function() {
  return Math.max.apply(null, this);
};

var longestPalindrome = function(s){
 var pal = [];
  for (var l = 0; l < s.length; l++) {
    for (var n = l; n < s.length; n++) {
      var sub = s.substring(l, n +1);
       if (sub === sub.split('').reverse().join('')) { pal.push(sub); }
     }
  }
  return pal.length === 0 ? 0 : pal.map(function(e) {return e.length}).max();
} 


longestPalindrome("zzbaabcd")
// 4
