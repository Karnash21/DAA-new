import random
import timeit
import matplotlib.pyplot as plt

def count_sort(A, place):
    C = [0] * 10
    for j in range(0, len(A)):
        index = (A[j] // place) % 10
        C[index] += 1
    for k in range(1, len(C)):
        C[k] += C[k-1]
    B = [-1] * (len(A) + 1)
    for k in range(len(A) - 1, -1, -1):
        index = (A[k] // place) % 10
        B[C[index]] = A[k]
        C[index] -= 1
    B = B[1:]
    return B

def radix_sort(A, MAX):
    place = 1
    while MAX > place:
        A = count_sort(A, place)
        place *= 10
    return A

MAX = 50000
A = []
x = []
n = []
rs = []
for i in range(0, 20001, 2000):
    for j in range(len(A), i, 1):
        A.append(random.randint(0, MAX))
    random.shuffle(A)
    x.append(len(A))
    n.append(len(A) * 0.000005)
    start = timeit.default_timer()
    A = radix_sort(A, MAX)
    end = timeit.default_timer()
    rs.append(end - start)
plt.plot(x, n, label = 'n')
plt.plot(x, rs, label = 'Radix Sort')
plt.title('Radix Sort')
plt.xlabel('Array size ------>')
plt.ylabel('Time taken ------>')
plt.legend()
plt.show()