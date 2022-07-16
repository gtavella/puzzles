function SubstitutionCipher(abc1, abc2) {
  
  this.encode = function ( str ) {
    this.str = str;
    return this.whichAlpha( abc1, abc2 );
  }
  
  this.decode = function (str) {
    this.str = str;
    return this.whichAlpha( abc2, abc1 );
  }
  
  this.whichAlpha = function( arrX, arrY ) {
    return this.str.split('').map( l => {
        let i = arrX.indexOf(l);
        return i === -1 ? l : arrY[i];
      }).join('');
  }
  
}



var abc1 = "abcdefghijklmnopqrstuvwxyz";
var abc2 = "etaoinshrdlucmfwypvbgkjqxz";
   
var sub = new SubstitutionCipher(abc1, abc2);
sub.encode("abc") // => "eta"
sub.encode("xyz") // => "qxz"
sub.encode("aeiou") // => "eirfg"
   
sub.decode("eta") // => "abc"
sub.decode("qxz") // => "xyz"
sub.decode("eirfg") // => "aeiou"


