function domainName(url){
  if (url.indexOf('www.') !== -1) { var k = 'www.'; }
  else if (/^https?:\/\//.test(url)) { k = '://'; }
  else { return url.split('.')[0]; }
 return  url.split(k)[1].split('.')[0];
}


console.log(domainName("http://github.com/carbonfive/raygun"))
// github
