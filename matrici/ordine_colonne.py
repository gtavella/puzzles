def scambia(L,i1,i2):
    t=L[i1]
    L[i1]=L[i2]
    L[i2]=t


# Riordina le colonne di una matrice in base all'ordinamento di una riga.
def ordina_colonne_matrice(M,ix):
    riga=M[ix]
    for i in range(len(riga)-1):
        for j in range(len(riga)-1-i):
            if riga[j]>riga[j+1]:
                for ik in range(len(M)):
                    scambia(M[ik],j,j+1)


M=[
  [ 3,   1,   4,   2],
  ['c', 'a', 'd', 'b'],
  ['z', 'x', 't', 'y'],
  [30,  10,  40,  20]
]
ordina_colonne_matrice(M,0)
