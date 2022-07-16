function simplify ( poly ) {
    var monoms = {}, 
        finalStr = '',
        rxMonom = /\s*([+-]?)\s*(\d*)([a-z]+)/g,
        resMonom;
    
    while ( resMonom = rxMonom.exec(poly) ) 
     {
        let [, sign, coef, monom] = resMonom;
        
        sign = sign || '+'
        
        if (coef == '0') coef = 0;
        else if (coef == '') coef = 1
        else coef = +coef
          
        monom = monom.split('').sort().join('')
          
        if ( monoms[monom] ) 
          {
             (sign == '+') 
                ? monoms[monom] += coef 
                : monoms[monom] -= coef;
          }
        else 
          {
             monoms[monom] = (sign == '+') 
                ? coef 
                : -coef;
          }  
     }
  
    
    Object.keys( monoms ).sort((a, b) => {
        var a_len = a.length,
            b_len = b.length;
        
        if (a_len != b_len) return a_len > b_len;
        else 
         {           
           let l = 0
           while (l < a_len) 
            {
               if (a[l] > b[l]) return a[l] > b[l]
               l++
            }
           
         }
      
    }).forEach(monom => {
         var coef = monoms[monom], sign;
    
         if (coef == 0) return;
         else if (coef > 0)
            sign = '+'
         else 
          { 
            coef = - (coef)
            sign = '-'
          }
    
        if (coef == 1) 
           coef = ''
    
         finalStr += `${sign}${coef}${monom}`
         
    })
    
    
  return finalStr.replace(/^\+/, '')
    
}


var result = simplify("3x-zx-3a+2xy-x-a+5ab+3a-c-2a+2x+abc-2ac+3a+2ac+x-abc-2xy+xz")

console.log(result)
// -abc+3a+2ac
