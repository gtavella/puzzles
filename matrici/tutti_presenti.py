
# Verifica che tutti gli elementi di una lista L siano tutti contenuti in almeno una di alcune liste generiche.
# Ogni lista generica puo' contenere tutti gli elementi di L, ma puo' anche contenere altri elementi.

# versione con FOR
def tutti_presenti1(L,liste):
    for lista in liste:
        tutti_in_lista=True
        for x in L:
            if x not in lista:
                tutti_in_lista=False
        if tutti_in_lista:
            return lista
    return False


# versione con WHILE
def tutti_presenti2(L,liste):
    for lista in liste:
        tutti_in_lista=True
        i=0
        while tutti_in_lista and i<len(L):
            x=L[i]
            if x not in lista:
                tutti_in_lista=False
            else:
                i+=1
        if tutti_in_lista:
            return lista
    return False



L=[1,2,3]
liste=[
    [1, 2],      # non tutti gli elementi di L sono presenti in questa lista
    [2,3],       # non tutti gli elementi di L sono presenti in questa lista
    [1, 2, 3, 4, 5]  # tutti gli elementi di L sono presenti in questa lista
]
print(tutti_presenti1(L,liste))
