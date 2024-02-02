
import math

# Recursive algorithm to compute the sum, sequence values and series values from a fixed start to a fixed end of any series. Here's how:
# STEP 1: Define the generic term of the sequence. Examples below
# STEP 2: Call the series_sum function, specify start, end and the sequence you want to compute the sum of
# See results.

# i: mobile index
# generic sequence term
def sequenceA(start,end):
    return lambda i: 1/(i**2)


def sequenceB(start,end):
    return lambda i: (1/2)**i


def sequenceC(start,end):
    return lambda i: math.log(i,math.e)/(i**2)

def sequenceD(start,end):
    return lambda i: (i**2)/(math.e**i)

def sequenceE(start,end):
    return lambda i: i




# compute sum from start to end of any series
# just create the generic term of the sequence (a function) and then pass it as an argument to the series_sum function
# This implementation minimizes the number of arguments passed in recursive calls.
# Because we pre-compute the sequence function with the start and end values, for each recursive call you effectively use
# only the arguments (and thus memory) you need, because only the mobile index i needs to be updated
def series_sum(start,end,sequence_target,s,interval,sequence_values,series_values):
    # negative numbers not allowed, only non negative integers (>=0)
    if start<0 or isinstance(start,float) or isinstance(end,float):
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
        interval.append(i)
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





# Model the concept of "after a certain point, the function is decreasing"
def definitely_decreasing(sequence_values,start,interval,series_info):
    i=len(sequence_values)-1
    found=False

    while i>=1 and not found:
        y=sequence_values[i]
        y_prev=sequence_values[i-1]
        # if the previous value is less than or equal the current one, it means function is increasing
        # so starting from the end, we stop at the very last point such that from that point onward,
        # the function always decreases
        if y_prev<=y:
            # we want to get the corresponding x from the interval
            # even through i is actually x, since we start from the length of the list-1, it's best to
            # actually get the x from the interval, it makes more semantic sense
            series_info['decreases_from']=[interval[i], y]
            found=True
        i-=1

    # if you've never found a minimum, what does it mean? That the minimum is the very first (x,y)
    if not found:
        # if function doesn't return before, it means the value sought after is the very first one
        series_info['decreases_from']=[start,sequence_values[0]]






def save_to_csv(file_name,interval,sequence_values,series_values):
    with open(f'{file_name}.csv', 'w') as file:
        file.writelines("i,sequence,series\n")
        for i in range(len(sequence_values)):
            file.writelines(f'{interval[i]},{sequence_values[i]},{series_values[i]}\n')




def main():
    start=1
    end=100
    s = [0]

    interval=[]
    sequence_values = []
    series_values = []
    series_info={
        'decreases_from': [0,0], # [x,y]
    }
    file_name='series_output'


    series_sum(start,
               end,
               sequenceE,
               s,
               interval,
               sequence_values,
               series_values)

    definitely_decreasing(sequence_values,start,interval,series_info)

    print(series_info)
    print('sum:',s[0])

    save_to_csv(file_name,interval,sequence_values,series_values)


main()





