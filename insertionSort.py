import random
import os
import time

def insertionSort(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i-=1
        A[i+1]=key
    return A

A = []
for i in range(0,10):
    A.append(random.randint(0,50))

os.system('cls')
"time.time() Função para calcular o tempo de excução do algoritmo"
start = time.time()
print(insertionSort(A))
end = time.time()
print("Time - Insertion Sort: ", round(end-start,8))