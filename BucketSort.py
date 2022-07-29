import random
import matplotlib.pyplot as plt
import timeit
import math

def insertion_sort(A):
    for i in range(0, len(A), 1):
        if A[i] < A[i-1]:
            for j in range(i, 0, -1):
                if A[j] < A[j-1]:
                    A[j], A[j-1] = A[j-1], A[j]
                else:
                    break
    return A

def bucket_sort(A):
    # buckets = (math.floor(max(A) * 10)) + 1
    buckets = len(A) + 1
    B = [[] for i in range(buckets)]
    for i in range(len(A)):
        index = math.floor(A[i] * buckets)
        B[index].append(A[i])
    C = []
    for i in range(len(B)):
        B[i] = insertion_sort(B[i])
        for j in range(len(B[i])):
            C.append(B[i][j])
    return C

A = []
x = []
n = []
bs = []
for i in range(1, 10002, 1000):
    for j in range(len(A), i, 1):
        A.append(random.random())
    random.shuffle(A)
    x.append(len(A))
    n.append(len(A) * 0.000005)
    start = timeit.default_timer()
    A = bucket_sort(A)
    end = timeit.default_timer()
    bs.append((end - start))
plt.plot(x, n, label = 'n')
plt.plot(x, bs, label = 'Bucket Sort')
plt.xlabel("Array size ------>")
plt.ylabel("Time taken ------>")
plt.title("Bucket Sort")
plt.legend()
plt.show()

#The given program on bucket sort runs on linear time for inputs from uniform distribution. We can see it through graph.