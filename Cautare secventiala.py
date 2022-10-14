from array import array

list=[]
numar_elemente=input("itrod nr elem: ")
numar_elemente=int(numar_elemente)
for i in range (0, int(numar_elemente)):
    element=input("introd elem: ")
    list.append(element)
print(list)
cautare_numar=input("introd nr cautat: ")
list.sort() #sortarea vectorului

def find_array(list,numar_elemente):
    for i in range (0, numar_elemente):
        if (list[i]==cautare_numar):
            print("numarul cautat se afla pe pozitia: ", i)
            break
        else:
            print("numarul cautat nu se afla in lista")

find_array(list,numar_elemente)
print("lista sortata este: ", list)