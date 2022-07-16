function LCS( x, y ) {

  var lcs = '';
  var last = 0;
  
    if( x.length < y.length ) {
       var short = x;
       var long = y;
    } else {
       short = y;
       long = x;
    }
    
  short.split('').forEach( l => {
    let match = long.indexOf( l, last );
    if( match !== -1 ) {
      last = match;
      lcs += l;
    }
  });

 return lcs;
  
}


console.log(LCS( "abcdef" , "abc" ))
// "abc"

console.log(LCS( "abcdef" , "acf" ))
// "acf"

console.log(LCS( "132535365" , "123456789" ))
// "12356"
