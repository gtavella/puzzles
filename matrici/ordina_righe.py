def scambia(M,i1,i2):
    t = M[i1]
    M[i1] = M[i2]
    M[i2] = t



# Ordina le righe di una matrice in base ai valori di 1 colonna specifica
# [[valore, numero]]
def bubble_sort_matrice(M,k,ord):

    for i in range(len(M)-1):
        for j in range(len(M)-1-i):

            if ord=='asc':
                if M[j][k] > M[j+1][k]:
                    scambia(M,j,j+1)

            elif ord=='desc':
                if M[j][k] < M[j+1][k]:
                    scambia(M,j,j+1)


M=[
    ['ciao', 2],
    ['ehi', 4],
    ['casa', 34],
    ['bau', 6],
    ['ok', 12]
]

# significa: ordina in senso crescente (ascending) le righe della matrice in base ai valori della colonna con indice 1
bubble_sort_matrice(M,1,'asc')
print(M)
# output: [['ciao', 2], 
#          ['ehi',  4], 
#          ['bau',  6], 
#          ['ok',   12], 
#          ['casa', 34]] 
