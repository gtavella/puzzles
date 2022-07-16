function formatWords(words){
  if(!Array.isArray(words)) return '';
  return (function() {
    words = words.filter(w => w);     
     if(words.length <= 1) {
           var len = 1;
           var lastWord = '';
        } else {
            len = words.length-1;
            lastWord = ' and ' + words[words.length-1];
        }
      return words.slice(0, len).join(', ') + lastWord;
  })(); 
     
}


formatWords(['ninja', 'samurai', 'ronin'])
// "ninja, samurai and ronin"
