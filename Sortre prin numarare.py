from array import array
from itertools import count

# Sortare prin numarare
def sortare_numarare(array):
    numar_elemente = len(array)
    output = [0] * numar_elemente
    count = [0] * 10
    for i in range(0, numar_elemente):
        count[array[i]] += 1
    for i in range(1, 10):
        count[i]=count[i] + count[i - 1]
    i = numar_elemente - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] = count[array[i]] - 1
        i-=1
    for i in range(0, numar_elemente):
        array[i]=output[i]

lista = [1,7,2,3,9,5,4]
sortare_numarare(lista)
print("Stiva sortata este:")
print(lista)