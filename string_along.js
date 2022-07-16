const createMessage = word1 => {
   var words = [word1];
  
   return function( word2 ) {
      const fn = word3 => {
           if(word3) {
              words.push(word3);
              return fn;
           }
           return words.join(' ');
      }
      
      return fn(word2);
   }
   
}


console.log(createMessage("Hello")("World!")("how")("are")("you?")())

// Hello World! how are you?
