import random
import timeit
import random
import numpy as np
import matplotlib.pyplot as plt

def QuickSort(A, start, end):
    if(start < end):
        pIndex = Partition(A, start, end)
        QuickSort(A, start, pIndex - 1)
        QuickSort(A, pIndex + 1, end)

def Partition(A, start, end):
    pivot = A[end]
    pIndex = start
    for i in range(start, end, 1):
        if A[i] <= pivot:
            A[i], A[pIndex] = A[pIndex], A[i]
            pIndex += 1
    A[pIndex], A[end] = A[end], A[pIndex]#swap A[pIndex] and A[end]
    return pIndex

A = []
x = []
nlgn = []
qs = []
for i in range(1, 31000, 1000):
    for j in range(len(A), i, 1):
        A.append(random.randint(1, 50000))
    x.append(i)
    nlgn.append(i*np.log2(i)*0.00000065)
    random.shuffle(A)
    start = timeit.default_timer()
    QuickSort(A, 0, len(A) - 1)
    end = timeit.default_timer()
    qs.append((end - start))
plt.plot(x, qs, label = 'Quick Sort')
plt.plot(x, nlgn, label = 'nlogn')
plt.title('Quick Sort analysis')
plt.xlabel('No. of inputs')
plt.ylabel('Total time taken')
plt.legend()
plt.show()
#On comparing with nlogn we get the graph similar to nlogn
#because its characteristic is of nlogn