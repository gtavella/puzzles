function letterFrequency ( text ) {
  var arr = [], 
      lts = text.toLowerCase().replace(/[^a-z]/g,'').split(''),
      u = lts.filter((e,i) => lts.indexOf(e) === i);
      
    u.forEach((_, l) => arr[l] = [u[l], text.match(new RegExp(u[l], 'gi')).length])  
    
  return arr.sort((a, b) => (a[1] == b[1]) ?  a[0] > b[0] ? 1 : -1 :  a[1] < b[1] ? 1 : -1 );
  
}


console.log(letterFrequency('aaAabb dddDD hhcc'))
//  [['d',5], ['a',4], ['b',2], ['c',2], ['h',2]]
