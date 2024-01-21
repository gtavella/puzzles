
# Verifica che i valori nella lista L1 e i valori nella lista L2, quando ordinati secondo i valori di L1,
# questo produce un ordinamento corretto in L2.
# ritorna L1 e L2 ordinati in senso crescente
# esempio (sono sequenziali):
"""
    L1: [2  1  6  3]
         |  |  |  |
    L2: [20 10 60 30]
    perche', quando ordinati in base a L1, gli elementi in L2 mantengono l'ordinamento corretto nello stesso senso:
    L1: [1  2  3  6]
         |  |  |  |
    L2: [10 20 30 60]
esempio (non sono sequenziali):
    L1: [2  1  6  3]
         |  |  |  |
    L2: [10 20 60 30]
    perche', quando ordinati in base a L1, gli elementi in L2 non mantengono l'ordinamento corretto nello stesso senso:
    L1: [1  2  3  6]
         |  |  |  |
    L2: [20 10 30 60]
"""

def scambia(L,i1,i2):
    t=L[i1]
    L[i1]=L[i2]
    L[i2]=t

def sono_sequenziali(L1,L2):
    for i in range(len(L1)-1):
        for j in range(len(L1)-1-i):
            if L1[j]>L1[j+1]:
                if L2[j]<L2[j+1]:
                    return False
                scambia(L1,j,j+1)
                scambia(L2,j,j+1)
    return True



L1= [6, 7, 1, 2, 8, 9, 3, 4, 5]
L2= [60,70,10,20,80,90,30,40,50]
# significa: gli elementi in L1, se ordinati, producono un ordinamento corretto anche in L2? 
print(sono_sequenziali(L1,L2))
# output: True, perche' gli elementi nella lista L1, quando ordinati, producono un ordinamento corretto anche in L2
print(L1,L2)
# output: [1,  2,  3,  4,  5,  6,  7,  8,  9]
#         [10, 20, 30, 40, 50, 60, 70, 80, 90]


