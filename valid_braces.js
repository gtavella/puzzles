function validBraces(braces){
  var stack = [],
      pairs = { '(': ')', '[': ']', '{': '}' }, b;
  for(b = 0; b < braces.length; b++) {
     let curr = braces[b];
      if(pairs[curr]) stack.unshift(pairs[curr]);
      else if(stack[0] === curr) stack.shift();
      else return false;
  }
  return stack.length === 0;
}



validBraces("(){}[]")
// true

validBraces("([{}])")
// true

validBraces("[({})](]")
// false
