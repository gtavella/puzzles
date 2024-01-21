
# Verifica se 2 specifiche colonne di una matrice ha elementi sovrapposti
# utile per verificare che date e giorni non siano sovrapposti,
# o in generale che qualsiasi valore numerico puo' o non puo' avere valori compresi tra valori gia' esistenti
# modifica la matrice iniziale (la ordina in senso crescente)
# ritorna True se e solo se i valori nella colonna jx1 e jx2 hanno almeno un sovrapposto
# alternativamente puoi lavorare su una copia della matrice, basta che crei una copia della matrice e lavori su di essa
def matrice_ha_sovrapposti(M,jx1,jx2):
    for i in range(len(M)-1):
        for j in range(len(M)-1-i):
            if M[j][jx1]>M[j+1][jx1]:
                t=M[j]
                M[j]=M[j+1]
                M[j+1]=t

    end_prev=M[0][jx2]
    for row in M[1:]:
        start_curr=row[jx1]
        end_curr=row[jx2]
        if end_prev>=start_curr:
            return True
        else:
            end_prev=end_curr
    return False



M=[
    [0, 31,  90],
    [1, 121, 215],
    [2, 11,  30],
    [0, 216, 250],
    [3, 301, 350],
    [3, 361, 370],
    [0, 351, 360],
    [0, 91,  120],
    [3, 401, 420],
    [2, 431, 450],
    [0, 421, 430]
]

# significa: verifica se le colonne con indice 1 e 2 hanno sovrapposti
print(matrice_ha_sovrapposti(M,1,2))
# ritorna False, perche' non esiste nessun valore sovrapposto nelle due colonne
# infatti la nuovo matrice ordinata e' composta da queste righe
# [2, 11, 30]
# [0, 31, 90]
# [0, 91, 120]
# [1, 121, 215]
# [0, 216, 250]
# [3, 301, 350]
# [0, 351, 360]
# [3, 361, 370]
# [3, 401, 420]
# [0, 421, 430]
# [2, 431, 450]
