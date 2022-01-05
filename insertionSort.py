def insertionSort(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i-=1
        A[i+1]=key
    return A
import random
import os
import time
A = []
for i in range(0,1000):
    A.append(random.randint(0,5))

start = time.time()
print(insertionSort(A))
end = time.time()
print("Time - Insertion Sort: ", round(end-start,8))