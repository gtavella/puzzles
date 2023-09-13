# capture the innermost parenthesis (..) [..] {..}
# {{{{A}}{A}}{A}}{(A)}{{{}{A}}[A]}{{{{A}}}}{}{{{A}}{A}{{{A}}}}

import re


pattern_inner_parenth = re.compile(r"(\([^()[\]{}]+\))(\d*)|(\[[^[\](){}]+\])(\d*)|({[^{}()[\]]+})(\d*)")
pattern_formula = re.compile(r"([A-Z][a-z]*)(\d*)")

target = '(A(K4C(A(PPr2)3)3)5)2(B3[FeDe]2Gh2(He2D4))3(Ga2HHe4Hi)2'
elements_map = {}

match_indexes = []



# slices a string given a list of list of start, end indexes
# def slice_str(target, indexes_list):
#     # get elements index that are not requested in indexes_list
#     count = 0
#     indexes_wanted = []
#     # if next start is bigger than current last, it means there's a gap of wanted indexes
#     for i, indexes in enumerate(indexes_list):
#         start, end = indexes
#         last_end = end
#         diff = start - last_end
#         # add indexes count for
#         for _ in range(0,diff):
#             if diff > 0:
#                 count += 1
#                 indexes_wanted.append(count)
        

# slice_str('GiuseppeTavellaAtUnical', [[1,2], [4,8], [10,13], [16,19]])

 
    # return a target string with innermost parenthesis removed
    
    # target = target[:start] + target[end:]






def simplify_formula(target):
    print(target)
    # search for innermost parenthesis
    for match_inner_parenth in pattern_inner_parenth.finditer(target):
        start, end = match_inner_parenth.span()
        match_indexes.append([start, end])
        # match within (), [] or {}
        formula_parenth = match_inner_parenth.group(1) or match_inner_parenth.group(3) or match_inner_parenth.group(5)
        # if this is null, set to 1
        coeff_parenth = int(match_inner_parenth.group(2) or match_inner_parenth.group(4) or match_inner_parenth.group(6) or 1)
        print('current parenthesis: ', target[start:end])

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
            # print(element, coeff_element_new)
    

    # slices innermost parenthesis
    # target = slice_str(target, match_indexes)
    # return simplify_formula(target)


simplify_formula(target)

        
