function stripUrlParams( url, paramsToStrip = [] ) {
  
  if(!/\?/.test( url )) return url;
  
    var [domain, params] = url.split('?');
    params = params.split('&')
                   .concat( paramsToStrip );
                   
    var newUrl = `${domain}?`;
    var collect = {};
    
    params.forEach( piece => {
      let [par, val] = piece.split('=');
      
      if( paramsToStrip.includes(par) ) return;
      if( !collect[par] ) {
         collect[par] = val;
         newUrl += `${par}=${val}&`;
      }
  });
  
  
  return newUrl.substr(0, newUrl.length-1);

}


console.log(stripUrlParams('www.codewars.com?a=1&b=2&a=2'))
// 'www.codewars.com?a=1&b=2'

console.log(stripUrlParams('www.codewars.com?a=1&b=2&a=2', ['b']))
// 'www.codewars.com?a=1'

console.log(stripUrlParams('www.codewars.com', ['b']))
// 'www.codewars.com'
