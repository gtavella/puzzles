def sono_unici(L):
    lista=[]
    for x in L:
        if x not in lista:
            lista.append(x)
        else:
            return False
    return True


L=[1,2,5,7,9]
# L=[5,7,8,9,8,1]
print(sono_unici(L))
