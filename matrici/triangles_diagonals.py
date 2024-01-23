

# Get upper triangle, lower triangle, main diagonal, secondary diagonal of a squared matrix
def matrix(M):
    # matrix dimension
    n=len(M)

    # upper triangle
    LU=[]
    # lower triangle
    LO=[]
    # main diagonal
    LM=[]
    # secondary diagonal
    LS=[]

    for i in range(n):
        # main diagonal
        LM.append(M[i][i])
        # secondary diagonal
        LS.append(M[i][n-1-i])

        for j in range(n):
            # upper triangle
            if i<n-1-j:
                LU.append(M[i][j])
            # lower triangle
            if i>n-1-j:
                LO.append(M[i][j])
            # if i==len(M) - 1 - j:
            #     LS.append(M[i][j])
            
    print(LM,LU,LO,LS)


M=[
    [0,  1,  2,  3],
    [4,  5,  6,  7],
    [8,  9,  10, 11],
    [12, 13, 14, 15]
]
matrix(M)



