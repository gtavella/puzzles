/*
Pig latin is created by taking all the consonants before the first vowel of a word and moving them to the back of the word followed by the letters "ay".
*/



function translate(str) {
  return str.replace(/\b([^aeiou\?\s,!]*)(\w+)/gi, (m, $1, $2) => {  
    if ($1 !== '') { var p = '', x = $1; }
    else { p = 'w'; x = $2; }  
    $2 = /[A-Z]/.test(x) ? $2.replace(/(\w)/, $1a => $1a.toUpperCase()) : $2;
   return $2 + $1.toLowerCase() + p + 'ay';
  });
}



translate("hello")
// "ellohay"

translate("creating")
// "eatingcray"

console.log(translate("Pizza? Yes please!"))
// "Izzapay? Esyay easeplay!"
