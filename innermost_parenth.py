# capture the innermost parenthesis (..) [..] {..}
# {{{{A}}{A}}{A}}{(A)}{{{}{A}}[A]}{{{{A}}}}{}{{{A}}{A}{{{A}}}}
# USAGE
# only use one parenthesis
# ({Ca}3)3 -> NO
# (Ga{Ca}3)3 -> YES

import re


pattern_inner_parenth = re.compile(r"(\([^()[\]{}]+\))(\d*)|(\[[^[\](){}]+\])(\d*)|({[^{}()[\]]+})(\d*)")
pattern_formula = re.compile(r"([A-Z][a-z]*)(\d*)")


elements_map = {}



# slices a string given a list of list of start, end indexes
def slice_str(target, indexes_list):
    result_str = ''
    n = 0
    for i, indexes in enumerate(indexes_list):
        start, end = indexes
        
        # first indexes
        if i == 0:
            start = start
            last_end = 0
            n = last_end
            while n < start:
                # print('n: ', n)
                result_str += target[n]
                n += 1
        else:
            start = start
            last_end = indexes_list[i-1][1]
            n = last_end
            while n < start:
                # print('n: ', n)
                result_str += target[n]
                n += 1
    
        # if it is the last indexes, you need to repeat the process twice
        if i == len(indexes_list)-1:
            start = len(target)-1
            last_end = end
            n = last_end
            while n <= start:
                # print('n: ', n)
                result_str += target[n]
                n += 1
            
    return result_str





target = '(Na(CH3)2)2[NaCa3(K3)]2'


def simplify_formula(target):        
    match_indexes = []
    # print(target)
    # search for innermost parenthesis
    for match_inner_parenth in pattern_inner_parenth.finditer(target):
        start, end = match_inner_parenth.span()
        match_indexes.append([start, end])
        # match within (), [] or {}
        formula_parenth = match_inner_parenth.group(1) or match_inner_parenth.group(3) or match_inner_parenth.group(5)
        # if this is null, set to 1
        coeff_parenth = int(match_inner_parenth.group(2) or match_inner_parenth.group(4) or match_inner_parenth.group(6) or 1)
        # print('group:        ', target[start:end])

        # if there's no match with parenthesis or coeff parenthesis is 1, then there's no parenthesis or nothing to multiply
        # if (not formula_parenth) or (coeff_parenth == 1):
        #     return elements_map

        # inside of innermost parenthesis, search for formula
        for match_formula in pattern_formula.finditer(formula_parenth):
            element = match_formula.group(1)
            # if coeff_formula is null, set to 1
            coeff_element = int(match_formula.group(2) or 1)
            coeff_element_new = coeff_element * coeff_parenth
            if element in elements_map:
                    elements_map[element] += coeff_element_new
            else:
                elements_map[element] = coeff_element_new
            # print(element, coeff_element_new, coeff_parenth)
    

    # slices innermost parenthesis
    target = slice_str(target, match_indexes)

    if target == '':
        return target
    else:
        return simplify_formula(target)





simplify_formula(target)
print(elements_map)
        
