def search_parent(last_parent):
  
  children_keys = last_parent['children'].keys()
  
  for child_key in children_keys:
  
    search_parent(last_parent['children'][child_key])
  

search_parent(tree)
