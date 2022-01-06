import random
import os
import time

def selectionSort(lista):
    print("Size: ", len(lista))
    for i in range(len(lista)-1):
        min = i
        for j in range(i+1,len(lista)):
            if lista[j] < lista[min]:
                min = j
        if i != min:
            aux = lista[i]
            lista[i]=lista[min]
            lista[min]=aux
    return lista

"Este algoritmo é muito lento para vetores muito grande, por outro lado é o mais rapido para vetores pequenos, e ocupa menos memoria"
os.system("cls")
A = []
for i in range(0,100):
    A.append(random.randint(0,50))

#print(A)
"time.time() Função para calcular o tempo de excução do algoritmo"
start = time.time()
print(selectionSort(A))
end = time.time()
print("Time - Insertion Sort: ", round(end-start,8))