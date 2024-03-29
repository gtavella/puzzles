

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


def fib1(n):
    if n<=1:
        return n
    return fib1(n-1)+fib1(n-2)

def fib2(n):
    a=0
    b=1
    for i in range(n):
        # print(a)
        c=a+b
        a=b
        b=c



# print(fib2(10))


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


def greater(x,L):
    if len(L)==0:
        return True
    if x<=L[0]:
        return False
    greater(x,L[1:])
    return True




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



# Sum all nonnegative numbers up to n.
def sum_until1(n,s):
    if n==0:
        return s
    return sum_until1(n-1,s+n)

# print(sum_until1(5,0))


def sum_until2(n):
    if n==0:
        return 0
    return n+sum_until2(n-1)

# print(sum_until2(5))



# Compute the whole division of an integer x divided by d which returns the total quotient q
# Equivalent to // operator
def whole_division(x,d,q):
    # if x-d returns a negative number, it means we've finished counting the quotient
    if x-d<0:
        return q
    # else decrease x by d
    return whole_division(x-d,d,q+1)


# print(whole_division(16,2,0))


# Get remainder of a division
# Equivalent to % operator
def mod_division(x,d):
    if x-d<0:
        return x
    return mod_division(x-d,d)




def find_max(L):
    first = L[0]
    if len(L) == 1:
        return first
    second = find_max(L[1:])
    if first > second:
        return first
    return second

# L = [5, 10, 361, 90, 7]
# print(find_max(L))






# Write a program that checks if a list is in ascending order - using recursion.
# Get first element (current)
# Get second element (next) (which is first in next recursive call)
# if current element >= next element, return False
# else return



def check_ascending1(L):
    n=len(L)
    # a list with no elements or one element is always sorted
    if n==0 or n==1:
        return True
    curr=L[0]
    next=L[1]
    # if list has only two elements
    # if list has more than 2 elements
    return curr<next and check_ascending1(L[1:])


# L=[1,2,3,4,5,6,7]
# print(check_ascending1(L))




# A list is said to be sorted in ascending order if and only if,
# chosen a random pivot in the list, every element to its left is less than the pivot,
# and every element to the right of the pivot is greater than the pivot.
# Base case: If the sublist is made of two elements
# A list is in ascending order if and only if the current element is smaller than the next.

# I choose the pivot with the index = middle
# Using partition algorithm
def check_ascending2(L):
    n=len(L)
    if n==0:
        return True
    mid=n//2
    pivot=L[mid]
    left=L[:mid]
    right=L[mid+1:]
    are_sorted=greater(pivot,left) and smaller(pivot,right)
    if are_sorted:
        return check_ascending2(left) and check_ascending2(right)
    return False

# L=[1,2,3,4,5,6,7,10,16,30]
# print(check_ascending2(L))



#  Write a Python program to sum recursion lists using recursion.
def sum_recurse(L,s):
    # if L is not a list, then it's a number
    if not isinstance(L,list):
        return s+L
    # if L is a list
    # if the length of the list is 0, it means there are no elements and the sum is whatever is the current sum (because s+0=s)
    if len(L)==0:
        return s
    # recurse on first element, the recursive sum of the first element will be added to s
    s1=sum_recurse(L[0],s)
    # recurse on all other elements, the recursive sum of all the other elements will be added to the recursive sum of the first element
    return sum_recurse(L[1:],s1)


# LL=[1, 2, [3,[2,[4]],4], [5,6],[[2,[1]]]]
# print(sum_recurse(LL,0))

