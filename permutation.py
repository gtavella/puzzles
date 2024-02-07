# Permute lists in vertical order
# Input example
# [a, b, c]
# [d, e, f]
# [g, h, i]
# Output example
# adg, adh, adi, aeg, aeh, aei, afg, afh, afi..


    
# gets invoked before performing any operation
# output True means that this value will NOT be included in the permutation
# you can also skip an entire column
# this value will be skipped
# output boolean
def perm_validv(p, i_p):
    # skip values with these indexes (which corresponds to a column)
#     return p != None and i_p != 1
    return p
#   i_p must be different than values in skip columns
    
    
    

def perm_editv(p):
    return p

    

# what to do with each permutation list
# gets invoked on the whole list after permutation is done and you want to edit outcome
# input list, output list
def perm_editl(p_list):
    return ''.join(p_list)
    # if you want all permutated values in list, use:
#     return p_list




# editv = function edit value
# validv = function valid value
# editl = function edit list
def permute_all(to_permute, editv, editl, validv):
    perms = [[]]    
    size_to_perm = len(to_permute)
    def perm(i_row, row, pre_p):
        # last row
        if i_row+1 == size_to_perm:   
            for i_p, p in enumerate(row):
                if not validv(p,i_p): 
                    continue
                last_perm = pre_p+[editv(p)]
                perms[-1].append(editl(last_perm))
            perms.append([])
            return   
        else:
            # all rows except last
            for i_p, p in enumerate(row):
                if not validv(p,i_p): 
                    continue
                perm(i_row+1, to_permute[i_row+1], pre_p+[editv(p)])
            return
    perm(0, to_permute[0], [])
    perms.pop()
    return perms
             

    

list_to_permute = [
    ['a', 'b', 'c'], 
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]   

    
    
permutations_all = permute_all(to_permute=list_to_permute, 
                               editv=perm_editv, 
                               editl=perm_editl, 
                               validv=perm_validv)

print(permutations_all)
# [['adg', 'adh', 'adi'], ['aeg', 'aeh', 'aei'], ['afg', 'afh', 'afi'], 
# ['bdg', 'bdh', 'bdi'], ['beg', 'beh', 'bei'], ['bfg', 'bfh', 'bfi'], 
# ['cdg', 'cdh', 'cdi'], ['ceg', 'ceh', 'cei'], ['cfg', 'cfh', 'cfi']]
