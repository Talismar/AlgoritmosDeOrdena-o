import os
import time
import random

"Caso queira ordenar em ordem inversa so troca o A[i] < A[i-1] por A[i] > A[i-1] "
def insertionSort(A,n):
    if n >= 1:
        insertionSort(A,n-1)
        i = n
        while (i >= 1 and A[i] < A[i-1]):
            troca = A[i]
            A[i]=A[i-1]
            A[i-1]=troca
            i-=1
    return A


A = []
for i in range(0,100):
    A.append(random.randint(0,50))

"Função para limpa o terminal do windows os.system('cls')"
os.system('cls')

"time.time() Função para calcular o tempo de excução do algoritmo"
start = time.time()
print(insertionSort(A,len(A)-1))
end = time.time()
print("Time - Insertion Sort: ", round(end-start,8))
