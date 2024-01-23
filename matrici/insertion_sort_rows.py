# sort matrix rows based on values in a column
def insertion_sort_matrix_rows(M,jx):
    for i in range(1,len(M)):
        current_x=M[i][jx]
        current_row=M[i]
        j=i-1
        while j>=0 and M[j][jx]>current_x:
            M[j+1]=M[j]
            j-=1
        M[j+1]=current_row




M1=[
  ['c',3],
  ['a',1],
  ['d',4],
  ['b',2]
]

# insertion_sort_matrix_rows(M1,1)
insertion_sort_matrix_rows(M1,0)
print(M1)
