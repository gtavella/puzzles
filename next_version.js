function nextVersion(version){
  var nums = version.split('.'),
     res = nums.slice(),
     n = nums.length;
  
  if(n === 1) return +nums[0]+1+'';
  
  while(n--) {
      if(+nums[n] >= 9) 
        { 
           if(n >= 1) 
              { 
                res[n-1] = +res[n-1] + 1;
                res[n] = 0;
                 if(+res[n-1] < 9) break; 
              }
        } 
      else 
        {
           res[n] = +res[n]+1;
           break;
        }
  }
  
  return res.join('.');
}


nextVersion("1.2.3")
// "1.2.4"
nextVersion("0.9.9")
// "1.0.0"
nextVersion("1")
// "2"
nextVersion("1.2.3.4.5.6.7.8")
// "1.2.3.4.5.6.7.9"
nextVersion("9.9")
// "10.0"
