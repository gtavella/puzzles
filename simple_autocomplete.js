function autocomplete(input, dictionary){
 var rx = new RegExp('^'+ input.replace(/[^a-z]+/g, ''), 'i');
  return dictionary.filter( w => rx.test( w )).slice(0,5);
}


var result1 = autocomplete('ai', ['airplane','airport','apple','ball'])
console.log(result1)
// ['airplane','airport']


var result2 = autocomplete('old', ['oldin','how older'])
console.log(result2)
// ['oldin']
