import re


pattern_inner_parenth = re.compile(r"(\([^()[\]{}]+\))(\d*)|(\[[^[\](){}]+\])(\d*)|({[^{}()[\]]+})(\d*)")
pattern_formula = re.compile(r"([A-Z][a-z]*)(\d*)")
pattern_not_parenth = re.compile(r'([^()[\]{}]+)')


tree = {}


def parenth_to_tree(target):     

    other_matches = []

    # IMPORTANT ASSUMPTION that determines outcome 
    # since this recursion matches the very first match (innermost parenthesis)
    # we can count on this fact: given n recursion, the next recursion (n+1) will either be a parent of the previous one, 
    # or not connected to the previous one

    def recurse_match(target_copy, last_start, last_end):

        print(target_copy)

        match_inner_parenth = re.search(pattern_inner_parenth, target_copy)

        if match_inner_parenth is None:
            print(other_matches)
            return

        start, end = match_inner_parenth.span()

        # for very first match
        if last_start is None:
            last_start = start
        if last_end is None:
            last_end = end

        # if this start < last_start and end < last_end, it means it's the parent
        # remember we are relying on the fundamental assumption that the next match is the FIRST inner parenthesis match possible in the entire string 
        if start < last_start and end > last_end:
            print(f'[{start}, {end}] is parent of [{last_start}, {last_end}]')
        else:
            other_matches.append([start, end])

        # match within (), [] or {}
        # formula_parenth = match_inner_parenth.group(1) or match_inner_parenth.group(3) or match_inner_parenth.group(5)
        # if this is null, set to 1
        # coeff_parenth = int(match_inner_parenth.group(2) or match_inner_parenth.group(4) or match_inner_parenth.group(6) or 1)

        # replace entire match with _ to allow continue recursive match with next innermost parenthesis
        symbol_repeat = '_' * (end - start)
        target_copy = target_copy[:start] + symbol_repeat + target_copy[end:]

        return recurse_match(target_copy, start, end)
    
    # pass a copy to avoid unwanted string behavior
    return recurse_match(target[:], None, None)




# target = '(((A)2)(B2)(C2(D2)))'
target = '((((((([A]([B](((({A2}(((((C))))[D]))))[E]))[F])))(G)))))'
tree = parenth_to_tree(target)
