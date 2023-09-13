import re

pattern_inner_parenth = re.compile(r"(\([^()[\]{}]+\))(\d*)|(\[[^[\](){}]+\])(\d*)|({[^{}()[\]]+})(\d*)")
pattern_formula = re.compile(r"([A-Z][a-z]*)(\d*)")



def simplify_formula(target):     

    str_formula = ''
    match_inner_parenth = re.search(pattern_inner_parenth, target)
    if match_inner_parenth is None:
         return target

    start, end = match_inner_parenth.span()
        # match within (), [] or {}
    formula_parenth = match_inner_parenth.group(1) or match_inner_parenth.group(3) or match_inner_parenth.group(5)
    # if this is null, set to 1
    coeff_parenth = int(match_inner_parenth.group(2) or match_inner_parenth.group(4) or match_inner_parenth.group(6) or 1)
    
    for match_formula in pattern_formula.finditer(formula_parenth):
        element = match_formula.group(1)
        # if coeff_formula is null, set to 1
        coeff_element = int(match_formula.group(2) or 1)
        coeff_element_new = coeff_element * coeff_parenth
        formula_new_str = f'{element}{coeff_element_new}'
        str_formula += formula_new_str

    target = target[:start] + str_formula + target[end:]
    return simplify_formula(target)



# pass a simplified or non-simplified formula
def map_formula(target):    
    # simplified target
    elements_map = {}
    target_plain = simplify_formula(target)
    for match_formula in pattern_formula.finditer(target_plain):
        element = match_formula.group(1)
        # if coeff_formula is null, set to 1
        coeff_element = int(match_formula.group(2) or 1)
        
        if element in elements_map:
            elements_map[element] += coeff_element
        else:
            elements_map[element] = coeff_element
    return elements_map




target = '([(CH3)2]2)2[{[NaCa]2}3[BVi3Ma4]2{(K3)3}2]2'

target_simplified = simplify_formula(target)
print(target_simplified)
# with simplify_formula, the result is:
# C8H24Na12Ca12B4Vi12Ma16K36


elements_map = map_formula(target)
print(elements_map)
# with map_formula, the result is:
# {'C': 8, 'H': 24, 'Na': 12, 'Ca': 12, 'B': 4, 'Vi': 12, 'Ma': 16, 'K': 36}


