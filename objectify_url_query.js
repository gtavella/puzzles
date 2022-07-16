 function convertQueryToMap(query) {
  if(!query) return {};
   var final = {};
      
    query.split('&').map( block => {
        
      let obj = final;
           return block.split('.').forEach( piece => { 
           
               let [prop, val] = piece.split('=').map(decodeURIComponent);
               
               if(/=/.test( piece )) obj[prop] = val;
               else if(!obj[prop]) obj[prop] = {};
                
               obj = obj[prop];
           });
       });
       
  return final; 
}


console.log(convertQueryToMap("user.name.firstname=Bob&user.name.lastname=Smith&user.favoritecolor=Light%20Blue"))
/*
{
  user: {
    name: { firstname: 'Bob', lastname: 'Smith' },
    favoritecolor: 'Light Blue'
  }
}
*/
