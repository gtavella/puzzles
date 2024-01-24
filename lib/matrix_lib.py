"""
A library for working with matrixes and lists.
Giuseppe Tavella
"""



# Given a list, create adjacents sublists of k length.
def create_adj_sublists(L,k):
    ret=[]
    for i in range(0,len(L)-k+1):
        ret.append(L[i:i+k])
    return ret
# L=[1,2,3,4,5,6,7,8,9]
# print(create_adj_sublists(L,2))
# [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]



# Given a list, creates contiguous sublists of k length.
# If the last sublist is not of k lenght, it will be the maximum minimum length given the list length.
def create_cont_sublists(L,k):
    ret=[]
    i=0
    while i<len(L):
        ret.append(L[i:i+k])
        i+=k
    return ret
# L=[1,2,3,4,5,6,7,8,9]
# print(create_cont_sublists(L,2))
# [[1, 2], [3, 4], [5, 6], [7, 8], [9]]



# Get upper triangle of a squared matrix
def get_upper_triangle_matrix(M):
    ret=[]
    n=len(M)
    for i in range(n):
        for j in range(n):
            # upper triangle
            if i<n-1-j:
                ret.append(M[i][j])
    return ret
# M=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print(get_upper_triangle_matrix(M))
# [1, 2, 4]



def get_lower_triangle_matrix(M):
    ret=[]
    n=len(M)
    for i in range(n):
        for j in range(n):
            # lower triangle
            if i>n-1-j:
                ret.append(M[i][j])
    return ret
# M=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print(get_lower_triangle_matrix(M))
# [6, 8, 9]





# Checks that all elements of a list L are present in some lists (it will stop when it finds one).
# Every generic list can contain the elements of L, but it can contain other elements as well.
def all_present_in(L_source,LL_target):
    for L_target in LL_target:
        all_in_list=True
        i=0
        while all_in_list and i<len(L_source):
            x=L_source[i]
            if x not in L_target:
                all_in_list=False
            else:
                i+=1
        if all_in_list:
            # you can return the specific list or index you found the match at
            return True
    return False

# L=[1,2,3,4,5]
# lists_target=[
#     [1,5,6,3,4],  # not all elements of L are present in this list
#     [2,3,6,1,1],  # not all elements of L are present in this list
#     [4,5,2,1,3]   # all elements of L are present in this list, and the list can contain other elements as well
# ]
# print(all_present_in(L,lists_target))



def swap(L,i1,i2):
    t=L[i1]
    L[i1]=L[i2]
    L[i2]=t



# Verifies that the values in a list source L1 and the values in a list target L2,
# when ordered based on the values of L1, this results in a correct order of values in L2.

#  example (are sequential):
#     L1: [2  1  6  3]
#          |  |  |  |
#     L2: [20 10 60 30]

#     because, when the elements are ordered based on L1, the elements of L2 keep the correct order in the same direction (ascending or descending).

#     L1: [1  2  3  6]
#          |  |  |  |
#     L2: [10 20 30 60]

#  example (not sequential):
#     L1: [2  1  6  3]
#          |  |  |  |
#     L2: [10 20 60 30]

#     because, when the elements are ordered based on L1, the elements of L2 do not keep the correct order in the same direction (ascending or descending).

#     L1: [1  2  3  6]
#          |  |  |  |
#     L2: [20 10 30 60]
def lists_are_sequential(L1,L2):
    if len(L1)!=len(L2): return False
    n=len(L1)
    # make copies and work on the copies
    L1_c=L1[:]
    L2_c=L2[:]

    for i in range(n-1):
        for j in range(n-1-i):
            if L1_c[j]>L1_c[j+1]:
                # if there's an element to be swapped, and at the same index in the other list, you don't have the same order,
                # it means the two lists are not sequential
                if L2_c[j]<L2_c[j+1]:
                    return False
                swap(L1_c,j,j+1)
                swap(L2_c,j,j+1)
    return True

# L1=[ 4,  5,  6,  3,  1,  2]
# L2=['d','e','f','c','a','b']
# print(lists_are_sequential(L1,L2))
# True




# Sort the columns of a matrix based on the ordering of a row.
# ix is the row index
def sort_matrix_columns(M,ix):
    row=M[ix]
    n=len(row)
    for i in range(n-1):
        for j in range(n-1-i):
            if row[j]>row[j+1]:
                # swap every element of every row at that index where you must swap (so every column)
                for ik in range(len(M)):
                    swap(M[ik],j,j+1)

# M=[
#   [ 3,   1,   4,   2],
#   ['c', 'a', 'd', 'b'],
#   ['z', 'x', 't', 'y'],
#   [30,  10,  40,  20],
#   ['g', 'e', 'h', 'f']
# ]
# print(sort_matrix_columns(M,0))
# print(M)
# [[1, 2, 3, 4], ['a', 'b', 'c', 'd'], ['x', 'y', 'z', 't'], [10, 20, 30, 40], ['e', 'f', 'g', 'h']]




# Sort matrix rows based on values in a column.
def sort_matrix_rows(M,jx):
    n=len(M)
    for i in range(n-1):
        for j in range(n-1-i):
            # compare column elements
            if M[j][jx]>M[j+1][jx]:
                # swap rows
                swap(M,j,j+1)

# M=[
#     ['okay', 2],
#     ['home', 4],
#     ['food', 34],
#     ['history', 6],
#     ['tech', 12]
# ]
# sort_matrix_rows(M,1)
# print(M)
# [['okay', 2], ['home', 4], ['history', 6], ['tech', 12], ['food', 34]]





# Generate a submatrix of k width
# Note: submatrix number of rows and columns is not always the same, it depends what coordinates you want the submatrix from
# ix: row index to start from
# jx: column index to start from
# k: width
def create_submatrix(M,ix,jx,k):
    ret=[]

    # general cases
    start_row=ix-k
    end_row=ix+k
    start_col=jx-k
    end_col=jx+k

    # edge cases
    # always start from a real beginning and a real end
    if start_row<0:
        start_row=0
    if end_row>=len(M):
        end_row=len(M)-1
    if start_col<0:
        start_col=0
    if end_col>=len(M[0]):
        end_col=len(M[0])-1

    for i in range(start_row, end_row+1):
        row=[]
        for j in range(start_col, end_col+1):
            row.append(M[i][j])
        ret.append(row)

    return ret

# M=[
#   [ 3,   1,   4,   2],
#   ['c', 'a', 'd', 'b'],
#   ['z', 'x', 't', 'y'],
#   [30,  10,  40,  20],
#   ['g', 'e', 'h', 'f']
# ]
# print(create_submatrix(M,1,1,1))
# [[3, 1, 4], ['c', 'a', 'd'], ['z', 'x', 't']]





def copy_matrix(M):
    ret=[]
    for i in range(len(M)):
        row=[]
        for j in range(len(M[0])):
            row.append(M[i][j])
        ret.append(row)
    return ret



# Checks if 2 columns of a matrix have overlapping elements
# Useful to check that dates and days are not overlapping
# Or in general that any numeric value cannot have values included between already existent values
# Returns True if and only if at least one value of the two columns have an overlap

def matrix_has_overlap(M,jx1,jx2):
    M_c=copy_matrix(M)
    n=len(M)

    # sorts matrix rows in ascending order
    for i in range(n-1):
        for j in range(n-1-i):
            if M_c[j][jx1]>M_c[j+1][jx1]:
                swap(M_c,j,j+1)

    # checks for overlap between two columns
    end_prev=M_c[0][jx2]
    for row in M_c[1:]:
        start_curr=row[jx1]
        end_curr=row[jx2]
        if end_prev>=start_curr:
            return True
        else:
            end_prev=end_curr

    return False

# M=[
#     [0, 31,  90],
#     [1, 121, 215],
#     [2, 11,  30],
#     [0, 216, 250],
#     [3, 301, 350],
#     [3, 361, 370],
#     [0, 351, 360],
#     [0, 91,  120],
#     [3, 401, 420],
#     [2, 431, 450],
#     [0, 421, 430]
# ]
# print(matrix_has_overlap(M,1,2))
# True
# If you were to work with the original matrix and you want to sort it as well, this would be the output.
# As you can see, there's no overlapping value between column with index jx1 e jx2
# [
# [2, 11, 30],
# [0, 31, 90],
# [0, 91, 120],
# [1, 121, 215],
# [0, 216, 250],
# [3, 301, 350],
# [0, 351, 360],
# [3, 361, 370],
# [3, 401, 420],
# [0, 421, 430],
# [2, 431, 450]
# ]


# Move all elements of a list to the right by as many elements there are in the list to add
# Useful to update a list with most recent entries or something to that effect.
def move_right_insert_start(L,L_new):
    # for i in range(len(L_new),len(L)-len(L_new)):
    #     L[i]=L[i-len(L_new)]
        # L[i+len(L_new)]=L[i]

    # for i in range(0,len(L_new)):
    #     L[i]=L_new[i]

    return L_new+L[0:len(L)-len(L_new)]

# L=[1,2,3,4,5,6,7,8,9]
# print(move_right_insert_start(L,['x','b']))
# print(L)

def move_left_insert_end(L,L_new):
    # for i in range(len(L)-1):
    #     L[i]=L[i+1]
    # L[-1]=x
    return L[len(L_new):]+L_new

# L=[1,2,3,4,5,6,7,8,9]
# print(move_left_insert_end(L,['x']))
# print(L)





