from array import array
list=[]
numar_elemente=input("introd nr de elemente al sirului ")
numar_elemente=int(numar_elemente)
for i in range (0, int(numar_elemente)):
    print ("introduceti elementul V[",i+1,"]=", end="")
    element=input()
    list.append(int(element))   
print("Lista este: ", list)

# cautarea elementului
list.sort() #sortarea vectorului
def cautare_binara(list, element, numar_elemente):
    left  = 0
    right = numar_elemente - 1
    while left <= right:
        middle = (left + right) // 2
        if list[middle] == element:
            return middle
        elif list[middle] < element:
            left = middle + 1
        else:
            right = middle - 1
    return -1
    element=input("introduceti elementul cautat ")
    print("elementul cautat este pe pozitia: ", cautare_binara(list, element, numar_elemente)+1)

    cautare_numar=input("Introdu numarul pe care vrei sa il cauti: ")
    print("Numarul pe care il cauti se gaseste pe pozitia ",cautare_binara(list, element, numar_elemente)+1)

    
        