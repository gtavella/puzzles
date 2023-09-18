import re



class FormulaAnalyzer:

    def __init__(self, target):

        self.target_original = target

        self.target_simplified = self.target_original

        self.suggestion = None

        self.is_valid_formula = None
        
        self.elements_map = {}

        self.patterns = {
            
            'innermost_interval': re.compile(r"""(?:(?#)(?P<parenth>\([^()[\]{}]+\))|(?#)(?P<square>\[[^[\](){}]+\])|(?#)(?P<curly>{[^{}()[\]]+}))(?#)(?P<coeff_interval>\d*)"""),
            
            'element_coeff': re.compile(r"""(?P<element>[A-Z][a-z]*)(?#)(?P<coeff_element>\d*)""")
        
        }
                                                

    # check for valid intervals () [] {}
    def validate_intervals(self):

        stack_open = []
        nomatch = []
        pairs = { '(': ')', '[': ']', '{': '}' }
        opening = pairs.keys()
        closing = pairs.values()

        self.suggestion = self.target_original

        for i, c in enumerate(self.target_original):

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

                        self.suggestion = self.suggestion[:i] + '_' + self.suggestion[i+1:]
                        nomatch.append([c,i])

                # close parenthesis when there's still no parenthesis in stack open
                else:
                    self.suggestion = self.suggestion[:i] + '_' + self.suggestion[i+1:]
                    nomatch.append([c,i])

        # reverse stack_open 
        nomatch =  nomatch + stack_open

        # open parenthesis left
        for c, i in stack_open:    
            self.suggestion = self.suggestion[:i] + '_' + self.suggestion[i+1:]
        
        self.is_valid_formula = (self.target_original == self.suggestion)

        self.suggestion = self.suggestion if self.target_original != self.suggestion else None

        self.nomatch = nomatch
        
        



    def simplify_formula(self):

        str_formula = ''
        
        match_inner_interval = re.search(self.patterns['innermost_interval'], self.target_simplified)

        if match_inner_interval is None:
            return 

        start, end = match_inner_interval.span()

        formula_parenth = match_inner_interval['parenth'] or match_inner_interval['square'] or match_inner_interval['curly']
    
        coeff_interval = int(match_inner_interval['coeff_interval'] or 1)
        
        for match_formula in self.patterns['element_coeff'].finditer(formula_parenth):

            element = match_formula['element']

            coeff_element = int(match_formula['coeff_element'] or 1)

            coeff_element_new = coeff_element * coeff_interval

            formula_new_str = f'{element}{coeff_element_new}'

            str_formula += formula_new_str

        self.target_simplified = self.target_simplified[:start] + str_formula + self.target_simplified[end:]

        return self.simplify_formula()



    

        # pass a simplified or non-simplified formula
    def map_elements(self):   

        self.validate_intervals() 

        if not self.is_valid_formula:
            raise Exception(f'Formula is not valid. Suggestion: {self.suggestion}')

        self.simplify_formula()

        for match_formula in self.patterns['element_coeff'].finditer(self.target_simplified):

            element = match_formula['element']
            # if coeff_formula is null, set to 1
            coeff_element = int(match_formula['coeff_element'] or 1)
            
            if element in self.elements_map:
                self.elements_map[element] += coeff_element

            else:
                self.elements_map[element] = coeff_element
    




        

formula = FormulaAnalyzer('([(CH3)2]2)2[{[NaCa]2}3[BVi3MaC4]2{(K3)3}2]2')
formula.map_elements() 

print(formula.target_simplified)
print(formula.elements_map)




# test, expected
# tests = [
#     ['(AA{)d[A]())))[])aa(({)2)2]]A){[}]]]BA[A](A)}([)[]]', False],
#     ['([(CH3)2]2)2[{[NaCa]2}3[BVi3MaC4]2{(K3)3}2]2', True],
#     ['([(CH3)2]2)2[{[NaCa]2}3[BVi3MaC4]2{(K3))3}2]2', False],
#     ['([(CH3)2]2)2([{[NaCa]2})3[BVi3MaC4]2{(K3))3}2]2', False],
#     ['([(CH3)2]]2)2[[{[NaCa]2})3[BVi3MaC4]2{(K3))3}2]2', False],
#     ['((((((([A]([B](((({A2}(((((C))))[D]))))[E]))[F])))(G)))))', True],
#     ['(((()({)}))()[(]))(())()', False],
#     ['[(()([))(()[])][[{][[](]]', False]
# ]



# TESTS 
# for test_data in tests:
    
#     test, expected = test_data
#     result = validate_parenth(test)
#     valid = result['valid']
#     if valid:
#         target_simplified = simplify_formula(test)
#         elements_map = map_formula(target_simplified)
#         print('VALID\noriginal target')
#         print(test)
#         print('target simplified')
#         print(target_simplified)
#         print('elements map')
#         print(elements_map)
#         print('\n')
#     else:
#         suggestion = result['suggestion']
#         print('INVALID\noriginal target')
#         print(test)
#         print('suggestion')
#         print(suggestion)
#         print('\n')
    




