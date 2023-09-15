import pandas as pd

# DATA STRUCTURES: Reference Scale, Data
# The reference scale maps a,b..n variables/features/keys/components to their min and max values
# The data has as column name a variable in reference scale


reference_scale_dict = {
    'variable': ['a',   'b',   'c',   'd',   'e',  'f'],
    'min':      [10,    150,    30,   2200,  100,  20],
    'max':      [100,   200,    40,   3000,  170,  30]
}

data_dict = {
    'a': [5,    60,   20,   100],
    'b': [160,  210,  220,  200],
    'c': [34,   31,   42,   39],
    'd': [2000, 2600, 2900, 3000],
    'e': [100,  170,  125,  127]
}



# reference scale is a pandas dataframe
reference_scale = pd.DataFrame(reference_scale_dict)
data            = pd.DataFrame(data_dict)



# all variables in <data> must be present in reference scale, but the opposite is not necessary
def check_variables(data):
  data_variables = list(data.columns)
  # get all values in variables column in reference scale
  all_variables = list(reference_scale['variable'])
  for data_var in data_variables:
     if data_var not in all_variables:
        print('ERROR - variable not in ref scale.')
        return 



# scale x from x range to y range
# it answers this question: given a range from x_min to x_max that x can have, 
# how much is x in another range y_min, y_max? This gives us y
def get_scaled(x, x_range, y_range=(0,1), round_to=5):
    x_min, x_max = x_range
    y_min, y_max = y_range
    x_coeff = (x_max - x_min) / (y_max - y_min)
    y_diff = (x - x_min) / x_coeff 
    y = y_min + y_diff
    return round(y, round_to)



# pass the variables/column names that you want to scale 
def get_scaled_data(data, variables, scale_to=(0,1)):    
    data_scaled = pd.DataFrame({})
    # remember that a column is also called variable/feature

    for variable in variables:
        variable_info = reference_scale[reference_scale['variable'] == variable]
        x_min = variable_info['min'].values[0]
        x_max = variable_info['max'].values[0]        
        # apply a function for each column
        variable_scaled = data[variable].apply(lambda x: get_scaled(x, x_range=(x_min, x_max), y_range=scale_to))
        # set the computed column in the new dataframe
        data_scaled[variable] = variable_scaled

    return data_scaled




# do something with this result or edit function to your needs
check_variables(data)

# scale all columns/variables 
data_scaled = get_scaled_data( data=data, variables=list(data.columns) )

print(reference_scale)
print(data)
print(data_scaled)
