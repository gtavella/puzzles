Object.prototype.hash = function ( query ) {
     var last = this,
         props = query.split('.'),
         l = props.length;
         
    for (let p = 0; p < l; p++) {
        last = last[ props[p] ];
        if (!last) return undefined;
    }
    
   return last;
}



var obj = {
  person: {
    name: 'joe',
    history: {
      hometown: 'bratislava',
      bio: {
        funFact: 'I like fishing.'
      }
    }
  }
};


console.log(obj.hash('person.name')) 
// 'joe'

console.log(obj.hash('person.history.bio'))
// { funFact: 'I like fishing.' }

console.log(obj.hash('person.history.hometown'))
// bratislava


