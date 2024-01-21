
# Ottieni una sottomatrice da una generica matrice, partendo dalla posizione (i,j), con ampiezza k.
# in input si assume una matrice ben formata le cui colonne sono della stessa lunghezza

# ix: indice di riga da cui partire
# jx: indice di colonna da cui partire
# k: ampiezza/distanza/passo
def sottomatrice(M,ix,jx,k):
    ret=[]

    # casi generali
    start_row=ix-k
    end_row=ix+k
    start_col=jx-k
    end_col=jx+k

    # casi limite
    # parti sempre da un vero inizio e una vera fine
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

# significa: ottieni una sottomatrice di ampiezza 1, con al centro l'elemento in posizione (2,2)
print(sottomatrice(M,2,2,1))
# output: [[6,  7,   8],
#          [11, 12, 13],
#          [16, 17, 18]]
