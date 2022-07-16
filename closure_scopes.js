/*
We want to create a function, which returns an array of functions, which return their index in the array. 
*/

function createFunctions(n) {
  var callbacks = [];
    // note let
  for (let i=0; i<n; i++) {
    callbacks.push(function() {
      return i;
    });
  }
  
  return callbacks;
}


var callbacks = createFunctions(5); 
// create an array, containing 5 functions

callbacks[0]()
// must return 0

callbacks[3]()
// must return 3
