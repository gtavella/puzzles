function dirReduc(arr){
 var str = arr.join('-'), after;
  while(after !== str) {
     after = str;
     str = str.replace(/(NORTH-SOUTH)|(SOUTH-NORTH)|(WEST-EAST)|(EAST-WEST)|^-|-$/g, '').replace(/--/g, '-');     
  }
  return !str ? [] : str.split(/-/);
}


console.log(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
// [ 'WEST' ]

console.log(dirReduc( ["NORTH", "WEST", "SOUTH", "EAST"] ))
// [ 'NORTH', 'WEST', 'SOUTH', 'EAST' ]

console.log(dirReduc( ["NORTH", "SOUTH", "NORTH", "EAST"] ))
// [ 'NORTH', 'EAST' ]
