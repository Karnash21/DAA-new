import random
import timeit
import matplotlib.pyplot as plt

def count_sort(A, max):
    C = [0] * (max + 1)

    for j in range(0, len(A), 1):
        C[A[j]] += 1

    for k in range(1, len(C)):
        C[k] += C[k-1]

    B = [-1] * (len(A) + 1)
    for k in range(len(A) - 1, -1, -1):
        B[C[A[k]]] = A[k]
        C[A[k]] -= 1
    B = B[1:]
    return B

A = []
n_x = []
n_y = []
count_time = []

for i in range(2, 10003, 1000):
    for j in range(len(A), i):
        A.append(random.randint(0, i))
    random.shuffle(A)
    start = timeit.default_timer()
    A = count_sort(A, i)
    end = timeit.default_timer()
    n_x.append(len(A))
    n_y.append(len(A) * 0.00000125)
    count_time.append((end - start))

plt.plot(n_x, n_y, label = 'n')
plt.plot(n_x, count_time, label = 'CountSort')
plt.title('CountSort')
plt.xlabel("Array size ------>")
plt.ylabel('Time taken ------>')
plt.legend()
plt.show()