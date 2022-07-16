/*

Given 4 coordinates, check if X is within the area
For X to be within the area, these conditions must be met:

latitude of A & B must be > X
latitude of C & D must be < X
longitude of A & D must be < X
longitude of B & C must be > X

*/


function isInArea(X, A, B, C, D) {
  const latX = Math.abs(X[0])
  const longX = Math.abs(X[1])
  const latA = Math.abs(A[0])
  const longA = Math.abs(A[1])
  const latB = Math.abs(B[0])
  const longB = Math.abs(B[1])
  const latC = Math.abs(C[0])
  const longC = Math.abs(C[1])
  const latD = Math.abs(D[0])
  const longD = Math.abs(D[1])  
  var response = 'no';
  
  if(
     (latA && latB >= latX) &&
     (latC && latD <= latX) &&
     (longA && longD <= longX) &&
     (longB && longC >= longX)
  ) {
    response = 'yes';
  } 
  
  return response;
  
}


const resp = isInArea(
  [39.35467455454954, 16.242390165403442],
  [39.35493820852117, 16.242171687134118],
  [39.35495548888945, 16.244220232127706], 
  [39.35284230128518, 16.24463229837117],	
  [39.352850736928616, 16.242344615850733])


console.log(resp)
