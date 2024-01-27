
# Given a list, write a program to get adjacent sublists of k length using recursion.
def get_sublists(L,k,res):
    if len(L)<=k:
        res.append(L)
    else:
        curr=L[:k]
        rest=L[1:]
        res.append(curr)
        get_sublists(rest,k,res)

# res=[]
# get_sublists([1,2,3,4,5,6,7],2,res)
# print(res)



# observation - with recursion, you pass the "collector variable" that is the variable that collects the result,
# as a parameter. In this example, the list res "collects" the computations of the recursive function.
# In fact not always do you have a case where the recursive function returns a specific value such as a number or string.
# In cases where the recursive function computes values like those that go in a list, you need to pass the list you want
# these values to be collected in, as a parameter.

def swap(L,i1,i2):
    t=L[i1]
    L[i1]=L[i2]
    L[i2]=t


# Order a list in ascending order using recursion.
def order_list(L,last_i):

    next_elements=L[last_i:]

    if len(next_elements)!=0:

        # build a list of the smallest elements to the left
        smallest=min(next_elements)

        # add last_i because I want the relative index found in the next_elements sublist, but I also want to absolute index of the list L,
        # that's why I add last_i, so I also get the absolute index. I do this because I don't want my index to depend on the values I'm not interested in,
        # that is those that come before the next_elements sublist. I want to find the index of an element in a sublist without being influenced by
        # elements that come before that sublist, but I want the absolute index so that when I swap elements I can swap them in the initial list L
        # in fact this code..
        # i_smallest = next_elements.index(smallest)
        # ..would only give you the relative index, that is, the index of that element in the sublist

        # get absolute index of next smallest element
        i_smallest=last_i+next_elements.index(smallest)

        # I swap the element at the last index, the smallest element
        swap(L,last_i,i_smallest)

        # get the index of the smallest element to the right
        # increment step by 1
        order_list(L,last_i+1)




# L=[1,6,23,4,2,5,7,1,0,9]
# print('initial list', L)
# order_list(L,0)
# print('final list',L)



# Write a program that checks if a number is smaller than any number in a given list, using recursion.
def smaller(x,L):
    # an element is always smaller or greater than all elements of an empty list, that is no element
    if len(L)==0:
        return True
    # the current element does not verify the condition at least once, return False
    if x>=L[0]:
        return False
    # keep on recursing with the next elements
    # the code that comes before the recursive call is to be considered like the body of a loop
    # likewise, if I keep recursing and I never return, it means the initial condition has been met
    smaller(x,L[1:])
    # in fact, if you haven't returned before, it means the element verifies the condition
    return True

# L=[4,7,5,8,7,9]
# x=3
# print(smaller(x,L))




# Reverse a string using recursion.
def reverse_string(s,res):
    if len(s)==0:
        return res
    res+=s[-1]
    return reverse_string(s[:-1],res)


# print(reverse_string('hello',''))


# Add numbers of a list using recursion.
def add_numbers(L,s):
    if len(L)==0:
        return s
    s+=L[0]
    return add_numbers(L[1:],s)

# L=[2,5,2,3,6,1]
# print(add_numbers(L,0))


# Calculate the power of a number using recursion.

def compute_power(base,exp,res):
    if exp==1:
        return res
    res=res*base
    return compute_power(base,exp-1,res)

# base=2
# exp=5
# print(compute_power(base,exp,base))
