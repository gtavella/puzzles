# STILL WORKING ON IT
# transform a string with parenthesis into tree and viceversa

import re


pattern_inner_parenth = re.compile(r"(\([^()[\]{}]+\))(\d*)|(\[[^[\](){}]+\])(\d*)|({[^{}()[\]]+})(\d*)")
pattern_formula = re.compile(r"([A-Z][a-z]*)(\d*)")
pattern_not_parenth = re.compile(r'([^()[\]{}]+)')


tree = {}


def parenth_to_tree(target):     

    parenth_list = []

    def create_tree(matches_list, target):
        # initialize a dict for every loop round
        # lowest start and biggest end is the root tree
        root = { 'start': 0, 'end': len(target)-1 }
        for match_list in matches_list:
            start, end = match_list
            
        print(matches_list)





    def recurse_match(target_copy):
        print(target_copy)
        match_inner_parenth = re.search(pattern_inner_parenth, target_copy)

        if match_inner_parenth is None:
            return create_tree

        start, end = match_inner_parenth.span()
        # match within (), [] or {}
        formula_parenth = match_inner_parenth.group(1) or match_inner_parenth.group(3) or match_inner_parenth.group(5)
        # if this is null, set to 1
        coeff_parenth = int(match_inner_parenth.group(2) or match_inner_parenth.group(4) or match_inner_parenth.group(6) or 1)

        # replace entire match with _ to allow continue recursive match with next innermost parenthesis
        symbol_repeat = '_' * (end - start)
        target_copy = target_copy[:start] + symbol_repeat + target_copy[end:]
        parenth_list.append([start, end])

        return recurse_match(target_copy)
    
    # pass a copy to avoid unwanted string behavior
    return recurse_match(target[:])(parenth_list, target)




# target = '(((A)2)(B2)(C2(D2)))'
target = '((((((([A]([B](((({A2}(((((C))))[D]))))[E]))[F])))(G)))))'
tree = parenth_to_tree(target)
