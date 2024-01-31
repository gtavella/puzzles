
import math

# Recursive algorithm to compute the sum, sequence values and series values from a fixed start to a fixed end of any series. Here's how:
# STEP 1: Define the generic term of the sequence. Examples below
# STEP 2: Call the series_sum function, specify start, end and the sequence you want to compute the sum of
# See results.

# i: mobile index
# generic sequence term
def sequenceA(start,end):
    return lambda i: 10+(1/i**2)


def sequenceB(start,end):
    return lambda i: (start+i)/(i**2)


def sequenceC(start,end):
    return lambda i: (1/2)**i

def sequenceD(start,end):
    return lambda i: math.log(i,math.e)/(i**2)


# compute sum from start to end of any series
# just create the generic term of the sequence (a function) and then pass it as an argument to the series_sum function
# This implementation minimizes the number of arguments passed in recursive calls.
# Because we pre-compute the sequence function with the start and end values, for each recursive call you effectively use
# only the arguments (and thus memory) you need, because only the mobile index i needs to be updated
def series_sum(start,end,sequence_target,s,sequence_values,series_values):
    # negative numbers not allowed, only non negative integers (>=0)
    if start<0:
        raise Exception('Domain must be x>=0, x natural.')
    # pre-compute sequence function and returns another function where you'll have to pass only the mobile index i to it
    # because the start and end values of the series, as well as the sequence function will always be the same at each point
    # during the computation / recursion, there's no point passing them for each recursive call
    # thus it makes much more sense to pre-compute a function that already knows what the start,end values and sequence function is,
    # so that you'll only have to pass it the updated mobile index i
    sequence=sequence_target(start,end)

    def compute_sum(i):
        # if the mobile index has reached the end
        # simply compute the current term of the sequence
        y_sequence=sequence(i)
        # add current sequence and series values
        sequence_values.append(y_sequence)

        # update sum of series
        s[0]=s[0]+y_sequence
        series_values.append(s[0])

        if i==end:
            return y_sequence
        # if you are at any generic point except the last term of the sequence
        # compute the current term of the sequence and add it to the rest of the sum of the sequence terms
        return y_sequence + compute_sum(i+1)

    # the first value of i (mobile index) is the value of start
    # i=start
    return compute_sum(start)


# IMPORTANT: be careful about the domain
# for example: cannot divide by 0, logarithm argument must be >0, argument of even root must be >=0, etc.
# I use a list because a list gets passed by reference, whereas if I were to pass an integer, it would be pased by value/copy
# instead of initializing an integer sum to 0, for example s=0, I initialize a list with one element s=[0]
s=[0]
sequence_values=[]
series_values=[]
series_sum(1,
             100,
             sequenceA,
             s,
             sequence_values,
             series_values)

print('Sum of series:')
print(s[0])
print()
print('Sequence values:')
print(sequence_values)
print()
print('Series values:')
print(series_values)



# Model the concept of "after a certain point, the function is decreasing"
def is_definitely_decreasing(L):
    i=len(L)-1
    while i>=1:
        curr=L[i]
        prev=L[i-1]
        if prev<=curr:
            return False
        i-=1
    return True




res=is_definitely_decreasing(sequence_values)
print(res)




