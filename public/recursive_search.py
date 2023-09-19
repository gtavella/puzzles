tree = {
    'value': 'root',
    'children': {
        'a': {
            'value': 'a'
        },
        'b': {
        'value': 'b',
        'children': {
            'd': {
                'value': 'd',
                'children': {
                    'e': {
                        'value': 'e'
                    }
                }
            }
        }
        },
        'c': {
            'value': 'c',
            'children': {
                'f': {
                    'value': 'f'
                },
                'g': {
                    'value': 'g',
                    'children': {
                        'h': {
                            'value': 'h'
                        }
                    }
                }
            }
        }
    }
}




# simple tree recursive search
def search_parent(last_parent):
  
  children_keys = last_parent['children'].keys()
  
  for child_key in children_keys:
  
    search_parent(last_parent['children'][child_key])
  
search_parent(tree)




# simple recursive tree search for value
def search_value(last_parent, value_target):

    if 'children' not in last_parent: 
        return 
  
    children_keys = last_parent['children'].keys()
    
    for child_key in children_keys:

        child = last_parent['children'][child_key]

        value = child['value']
        
        if value == value_target:

            print('found value', value)
    
        search_value(child, value_target)
  

search_value(tree, 'h')
print(tree)
