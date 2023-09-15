import re
import time


pattern_inner_parenth = re.compile(r"(\([^()[\]{}]+\))(\d*)|(\[[^[\](){}]+\])(\d*)|({[^{}()[\]]+})(\d*)")
pattern_formula = re.compile(r"([A-Z][a-z]*)(\d*)")
pattern_not_parenth = re.compile(r'([^()[\]{}]+)')



# test, expected
tests = [
    ['(AA{)d[A]())))[])aa(({)2)2]]A){[}]]]BA[A](A)}([)[]]', False],
    ['([(CH3)2]2)2[{[NaCa]2}3[BVi3MaC4]2{(K3)3}2]2', True],
    ['([(CH3)2]2)2[{[NaCa]2}3[BVi3MaC4]2{(K3))3}2]2', False],
    ['([(CH3)2]2)2([{[NaCa]2})3[BVi3MaC4]2{(K3))3}2]2', False],
    ['([(CH3)2]]2)2[[{[NaCa]2})3[BVi3MaC4]2{(K3))3}2]2', False],
    ['((((((([A]([B](((({A2}(((((C))))[D]))))[E]))[F])))(G)))))', True],
    ['(((()({)}))()[(]))(())()', False],
    ['[(()([))(()[])][[{][[](]]', False]
]





# check for valid parenthesis
# if invalid parenthesis match, run callback function
def validate_parenth(target):
    stack_open = []
    nomatch = []
    pairs = { '(': ')', '[': ']', '{': '}' }
    opening = pairs.keys()
    closing = pairs.values()

    suggestion = target

    for i, c in enumerate(target):

        #  open parenthesis
        if c in opening:
            # add at beginning of list
            stack_open = [[c, i]] + stack_open

        # close parenthesis
        if c in closing:
            if len(stack_open) > 0:
                last_open = stack_open[0][0]

                # close parenthesis corresponding
                if (c == pairs[last_open]):
                    # remove at the beginning of list
                    stack_open = stack_open[1:]

                # close parenthesis not corresponding
                else:
                    suggestion = suggestion[:i] + '_' + suggestion[i+1:]
                    nomatch.append([c,i])

            # close parenthesis when there's still no parenthesis in stack open
            else:
                suggestion = suggestion[:i] + '_' + suggestion[i+1:]
                nomatch.append([c,i])

    # reverse stack_open 
    nomatch =  nomatch + stack_open

    # open parenthesis left
    for c, i in stack_open:
        suggestion = suggestion[:i] + '_' + suggestion[i+1:]
    
    return {
        'valid': (target == suggestion),
        'original': target,
        'suggestion': suggestion if target != suggestion else None,
        'nomatch': nomatch
    }






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





# TESTS & SPEED

start_time = time.time()
for test_data in tests:
    
    test, expected = test_data
    result = validate_parenth(test)
    valid = result['valid']
    if valid:
        target_simplified = simplify_formula(test)
        elements_map = map_formula(target_simplified)
        print('VALID\noriginal target')
        print(test)
        print('target simplified')
        print(target_simplified)
        print('elements map')
        print(elements_map)
        print('\n')
    else:
        suggestion = result['suggestion']
        print('INVALID\noriginal target')
        print(test)
        print('suggestion')
        print(suggestion)
        print('\n')
    
time_diff = time.time() - start_time
time_diff_millisec = time_diff * 1000
print('execution time (milliseconds)')
print(time_diff_millisec)
print('\n')
