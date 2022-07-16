function getPINs(observed) {
  var possible = [
      ['0', '8'],
      ['1','2', '4'],
      ['2', '1', '3', '5'],
      ['3', '2', '6'],
      ['4', '1', '5', '7'],
      ['5', '2', '4', '6', '8'],
      ['6', '3', '5', '9'],
      ['7', '4', '8'],
      ['8','5', '7', '9', '0'],
      ['9', '6', '8']
  ];
  
  var allComb = observed.split('').map( x => possible[+x] );
  
  return (function calcComb(arr2D) {
  
     if (arr2D.length == 1) return arr2D[0];
    
      var rest = calcComb(arr2D.slice(1));
      var res = [];
  
     for (var i = 0; i < rest.length; i++) {
        for (var j = 0; j < arr2D[0].length; j++) {
          res.push(arr2D[0][j] + rest[i]);
        }
      }
      
      return res;    
    
  })(allComb);
  
}



console.log(getPINs('12'))
/*
[
  '12', '22', '42',
  '11', '21', '41',
  '13', '23', '43',
  '15', '25', '45'
]
*/


console.log(getPINs('507'))

/*
[
  '507', '207', '407', '607',
  '807', '587', '287', '487',
  '687', '887', '504', '204',
  '404', '604', '804', '584',
  '284', '484', '684', '884',
  '508', '208', '408', '608',
  '808', '588', '288', '488',
  '688', '888'
]
*/
