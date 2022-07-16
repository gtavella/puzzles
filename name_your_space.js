function namespace(root, path, value){
    var result
    var props = path.split('.')
    
    if(value) {
        let lastProp = props.pop()
        props.forEach(prop => {
            if(!root[prop]) root[prop] = {}
            root = root[prop]
        })
        root[lastProp] = value
        result = root
    }
    else {
        props.forEach(prop => {
            if(!root[prop]) return 
            root = root[prop]
        })
    }
    
    return result
}



let stuff = {}

namespace(stuff, 'moreStuff.name', 'the stuff')
namespace(stuff, 'moreStuff.name') 
namespace(stuff, 'moreStuff.response', 'yes')  
namespace(stuff, 'info.name', 'Universe') 
namespace(stuff, 'info.quality', 'sweet') 

console.log(stuff)

/* {
  moreStuff: { name: 'the stuff', response: 'yes' },
  info: { name: 'Universe', quality: 'sweet' }
}
*/
