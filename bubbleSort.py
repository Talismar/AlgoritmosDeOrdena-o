import random
import os
import time

def bubbleSort(lista):
    print("Size: ", len(lista))
    for i in range(len(lista)):
        j = i 
        for k in range(i+1,len(lista)):
            if lista[k] < lista[j]:
                x = lista[k]
                lista[k] = lista[j]
                lista[j] = x

    return lista


os.system("cls")
A = []
for i in range(0,1000):
    A.append(random.randint(0,50))

#print(A)
"time.time() Função para calcular o tempo de excução do algoritmo"
start = time.time()
print(bubbleSort(A))
end = time.time()
print("Time - Insertion Sort: ", round(end-start,8))