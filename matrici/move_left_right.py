def move_right_insert_start(L,x):
    i=len(L)-1
    while i>=1:
        L[i]=L[i-1]
        i-=1
    L[0]=x


def move_left_insert_end(L,x):
    for i in range(len(L)-1):
        L[i]=L[i+1]
    L[-1]=x
