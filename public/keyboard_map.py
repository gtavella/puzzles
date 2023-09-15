# map the keyboard's characters to its coordinates, what it has on its left, right, up, down

import pandas as pd



# c = character
# x = row index
# y = column index
# l = left 
# r = right
# u = up
# d = down
def map_keyboard(keyboard_list):
    keyboard = pd.DataFrame(keyboard_list)
    result = []
    tot_cols = len(keyboard.columns)
    tot_rows = len(keyboard)
    
    for x, this_row in keyboard.iterrows():        
        for y in keyboard:
            c = this_row[y]
            if c == None:
                continue
    
            # no left, yes right
            if y-1 < 0:
                l = None
                r = keyboard[y+1][x]
            
            # yes left, no right
            elif y+1 >= tot_cols:
                l = keyboard[y-1][x]
                r = None
            
            # yes left, yes right
            elif y-1 >= 0 and y+1 < tot_cols:
                l = keyboard[y-1][x]
                r = keyboard[y+1][x]
            
            # other if group
            # no up, yes down
            if x-1 < 0:
                u = None
                d = keyboard[y][x+1]
            
            # yes up, no down
            elif x+1 >= tot_rows:
                u = keyboard[y][x-1]
                d = None
            
            # yes up, yes down
            elif x-1 >= 0 and x+1 < tot_rows:
                u = keyboard[y][x-1]
                d = keyboard[y][x+1]

            result.append([c, x, y, l, r, u, d])
    
    return pd.DataFrame(result, columns=['char', 'x', 'y', 'left', 'right', 'up', 'down'])





# TESTS 

keyboard_qwerty = [
    ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
    ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
    ['z', 'x', 'c', 'v', 'b', 'n', 'm']
]

keyboard_random1 = [
    ['a', 'b'],
    ['c', 'd', 'e'],
    ['f'],
    ['g', 'h', 'i', 'j']
]

keyboard_random2 = [
    ['a', 'b', 'c', 'd'],
    ['e', 'f', 'g'],
    ['h'],
    ['i', 'j']
]

keyboard_random3 = [
    ['a'],
    ['b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i', 'j']
]


qwerty_map = map_keyboard(keyboard_qwerty)
random1_map = map_keyboard(keyboard_random1)
random2_map = map_keyboard(keyboard_random2)
random3_map = map_keyboard(keyboard_random3)

print(qwerty_map, '\n----')
print(random1_map, '\n----')
print(random2_map, '\n----')
print(random3_map, '\n----')


