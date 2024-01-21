
# la lista L2 e' sequenziale con L1
# ritorna L1 e L2 ordinati in senso crescente
# ovvero, ordinando la lista L1, si ottieni un ordinamento corretto anche in L2?
# esempio (sono sequenziali):
"""
    L1: [2  1  6  3]
         |  |  |  |
    L2: [20 10 60 30]
    perche', quando ordinati in base a L1, mantengono l'ordinamento corretto:
    L1: [1  2  3  6]
         |  |  |  |
    L2: [10 20 30 60]
esempio (non sono sequenziali):
    L1: [2  1  6  3]
         |  |  |  |
    L2: [10 20 60 30]
    perche', quando ordinati in base a L1, non mantengono l'ordinamento corretto:
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




# L1=[2,1,4]
# L2=[100,80,110]
L1= [6, 7, 1, 2, 8, 9, 3, 4, 5]
L2= [60,70,10,20,80,90,30,40,50]
print(sono_sequenziali(L1,L2))
print(L1,L2)

