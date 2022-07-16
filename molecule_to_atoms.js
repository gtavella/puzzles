function parseMolecule ( f ) {
  var obj = {},     
  
      rxElCoef = /([A-Z][a-z]*)(\d*)/g,
      
      rxAll =  /(\([^()[\]{}]+\))(\d*)|(\[[^[\](){}]+\])(\d*)|({[^{}()[\]]+})(\d*)/g;
 
      f = f.replace(rxElCoef, (_, el, coef) => `${el}${coef || 1}`);

      while ( rxAll.exec(f) ) {
          f = f.replace(rxAll, (_, ...g) => {
              let paren = g[0] || g[2] || g[4],
                  parenMult = paren.replace(/(\d+)/g, (_, coef) => +coef * (g[1] || g[3] || g[5] || 1));
              return parenMult.substring(1, parenMult.length - 1)
          })
      }
    
     f.replace(rxElCoef, (_, el, coef) => obj[el] ? obj[el] += +coef : obj[el] = +coef )   
 
   return obj 
}



console.log( parseMolecule('K4[ON(SO3)2]2') )
// { K: 4, O: 14, N: 2, S: 4 }

console.log( parseMolecule('Mg(OH)2') )
// { Mg: 1, O: 2, H: 2 }
