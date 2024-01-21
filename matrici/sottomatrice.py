

# ix: row index to start from
# jx: column index to start from
# k: distance/step
def submatrix(M,ix,jx,k):
    ret=[]

    start_row=ix-k
    end_row=ix+k
    start_col=jx-k
    end_col=jx+k

    # always start from real beginning end real end
    # assuming a matrix with same-length columns
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




M=[
   [0,    1,   2,   3,   4],
   [5,    6,   7,   8,   9],
   [10,  11,  12,  13,  14],
   [15,  16,  17,  18,  19],
   [20,  21,  22,  23,  24]
]
print(submatrix(M,1,0,2))
