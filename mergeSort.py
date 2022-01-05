import os
import random
import time

def merge(lista, inicio, meio, fim):
    left = lista[inicio:meio]
    right = lista[meio:fim]
    i, j = 0,0
    for k in range(inicio,fim):
        if i >= len(left):
            lista[k]= right[j]
            j+=1
        elif j >= len(right):
            lista[k] = left[i]
            i+=1    
        elif left[i] < right[j]:
            lista[k] = left[i]
            i+=1
        else:
            lista[k]= right[j]
            j+=1

def MergeSort(lista, inicio, fim):
    if (fim - inicio) > 1:                
        meio = (fim + inicio)//2
        MergeSort(lista, inicio, meio)    
        MergeSort(lista, meio, fim)
        merge(lista, inicio, meio, fim)
    return lista

os.system("cls")
A = []
for i in range(0,1000):
    A.append(random.randint(0,5))

start = time.time()
print(MergeSort(A,0,len(A)))
end = time.time()
print("Time - Insertion Sort: ", round(end-start,8))
