# Mini-Parser based off of Formula Analyzer

import re, json



class Parser:

    def __init__(self, target):

        self.target_original = target

        self.target_simplified = self.target_original

        self.suggestion = None

        self.is_valid_formula = None

        self.intervals_indexes = []
        
        self.elements_map = {}

        self.tree = { 'name': 'root', 'range': (0, len(self.target_original) ), 'data': self.target_original, 'children': {} }

        self.last_parent = self.tree

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

        self.simplify_formula()

        for match_formula in self.patterns['element_coeff'].finditer(self.target_simplified):

            element = match_formula['element']
            # if coeff_formula is null, set to 1
            coeff_element = int(match_formula['coeff_element'] or 1)
            
            if element in self.elements_map:
                self.elements_map[element] += coeff_element

            else:
                self.elements_map[element] = coeff_element
    



    # return sorted list of lists of interval indexes
    def get_intervals_indexes(self):

        self.intervals_indexes = []

        def recurse(target_copy):

            # print(target_copy)
            match_inner_interval = re.search(self.patterns['innermost_interval'], target_copy)

            if match_inner_interval is None: 

                # print('DONE with intervals')

                self.intervals_indexes.sort(key=lambda x: x[0])

                return 

            start, end = match_inner_interval.span()

            self.intervals_indexes.append([start, end])

            symbol_repeat = '_' * (end - start)

            target_copy = target_copy[:start] + symbol_repeat + target_copy[end:]

            recurse(target_copy)
        
        recurse(self.target_original[:])

    
    def tree_to_json(self): self.tree_json = json.dumps(self.tree)

    
    def new_id(self, start, end): return f'{start}-{end}'


    def new_child(self, start, end, id):  return { 'name': '', 'range': (start, end), 'data': self.target_original[start:end], 'children': {} }




    def search_children(self, last_parent, start, end):

        if 'children' not in last_parent:  return
        
        start_last_parent, end_last_parent = last_parent['range']
        
        children_keys = last_parent['children'].keys()

        if start >= start_last_parent and end <= end_last_parent:

            if len(children_keys) == 0:

                id_child = self.new_id(start, end)
        
                last_parent['children'][id_child] = self.new_child(start, end, id_child)


            else: 

                recurse = True

                ranges_children_sorted = []

                # you need to check them ALL before moving on
                for child_key in children_keys:

                    start_child, end_child = last_parent['children'][child_key]['range']

                    ranges_children_sorted.append([start_child, end_child])
                
                # sort list by first number, which is the range start
                ranges_children_sorted.sort(key=lambda x: x[0])

                
                end_last_child = start_last_parent
                
                for i, range_child in enumerate(ranges_children_sorted):

                    start_child, end_child = range_child
                    
                    # check for the beginning
                    # check in between
                    if start >= end_last_child and end <= start_child:
                        # print('found new range in the middle or start')
                        
                        id_child = self.new_id(start, end)
                            
                        last_parent['children'][id_child] = self.new_child(start, end, id_child)

                        recurse = False
                    
                    # # check for the end, calculate again
                    if i == len(ranges_children_sorted)-1:

                        if start >= end_child and end <= end_last_parent:
                            # print('found new range at the end')
                            
                            id_child = self.new_id(start, end)
                            
                            last_parent['children'][id_child] = self.new_child(start, end, id_child)

                            recurse = False

                    end_last_child = end_child
                    

                if recurse:
                    # if the last parent didn't meet the conditions above, it means you need to recurse for each child
                    for child_key in children_keys:

                        child = last_parent['children'][child_key]

                        self.search_children(child, start, end)
            
        else:
            # STILL WORKING HERE
            # get the last_parent
            # get all the children with lower values than start end
            # assign these children to a 
        
            # print('CAUGHT unprocessed interval')
            # print('start interval', start)
            # print('end interval', end)
            # print(self.target_original[start:end])
            # print(self.tree)

            # print('start last parent', start_last_parent)
            # print('end last parent', end_last_parent)
            # print('\n\n')


            # print(start > start_last_parent and end < end_last_parent)

            pass





    def create_tree(self):
           
        for interval_indexes in self.intervals_indexes:

            start, end = interval_indexes

            self.search_children(self.tree, start, end)


        
text = """

(A)
[B]
(
(C) - ((D + G))
)[
(E) + [F]
]

"""


parser = Parser(text)
parser.validate_intervals()
if not parser.is_valid_formula:
    raise Exception(f'Text is not valid. Suggestion: {parser.suggestion}')


parser.get_intervals_indexes()
print(parser.intervals_indexes)

parser.create_tree()
parser.tree_to_json()
print(parser.tree_json)



    




