function simplify( poly ) {
    var monoms = {}, 
        arr_monoms = [],
        finalStr = '';
    
    poly.replace(/([+-]?)(\d*)([a-z]+)/g, (_, sign, coef, monom) => {
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
    })
    
    
    arr_monoms = Object.keys( monoms ).sort((a, b) => {
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
    })
    
    
    arr_monoms.forEach(monom => {
        var coef = monoms[monom], sign;
        
        if (coef == 0) return;
        else if (coef > 0)
            sign = '+'
        else 
         { 
           coef = -(coef)
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
// 5x+5ab-c
