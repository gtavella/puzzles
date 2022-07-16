function hexStringToRGB(hexString) {
  var a = hexString.substr(1).match(/.{2}/g).map(e => parseInt(e, 16)); 
   return {
      r: a[0],
      g: a[1],
      b: a[2]
    };
}


hexStringToRGB("#FF9933")
// {r: 255, g: 153, b: 51}

