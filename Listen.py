# Listen
"""
from codecs import getreader


L = list(range(10, 120, 10))

L[1] = 15
print(L)

del L[2:6] 
print(L)
liste = list(range(0,8))

L[2:2] = liste

print(L)


L.append(1)
L.append(2)
L.append(3)
L.append(4)
L.append(5)
print(L)

liste1 = list(range(0,5))
L.extend(liste1)
print(L)



L.pop()

x = len(L) -1
del L[x]
x = len(L) -1

L.reverse()
L.remove(L[0])
L.reverse()

print(L)



Z = list(zip([1, 2, 3], [4, 5 ,6]))
print(Z)

J = list(range(0, 10))
K = list()

for x in J:
    K.append(J[x] * 10)

H = list(x * 10 for x in J)


print(J)
print(K)    
print(H)"""


def sortieren(J):
    gerade = list()
    ungerade = list()
    for x in J:
        if x % 2 == 0:
            gerade.append(x)
        else:
            ungerade.append(x)

    gerade = sorted(gerade)       
    ungerade = sorted(ungerade)
    rueckgabe = list(gerade + ungerade)
    return(rueckgabe)

unsortiert = list(range(0,10))
sortiert = sortieren(unsortiert)
print(sortiert)

'''def fun(key:int):
    return key % 2

lst = list(range(10))
print(lst)
lst.sort(key=fun)
print(lst)'''