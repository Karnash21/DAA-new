from random import randint
from math import log2
import timeit
import matplotlib.pyplot as plt

def merge(arr, l, m, r):
	n1 = m - l + 1
	n2 = r - m
	L = [0] * (n1)
	R = [0] * (n2)

	for i in range(0, n1):
		L[i] = arr[l + i]
	for j in range(0, n2):
		R[j] = arr[m + 1 + j]
	i = 0
	j = 0
	k = l
	while i < n1 and j < n2:
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1
	while i < n1:
		arr[k] = L[i]
		i += 1
		k += 1
	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1
def mergeSort(arr, l, r):
	if l < r:
		m = l+int((r-l)/2)
		mergeSort(arr, l, m)
		mergeSort(arr, m+1, r)
		merge(arr, l, m, r)
arr = []
x = []
y = []
n = []
for i in range(1, 5000, 200):
    for j in range(i):
        temp = randint(1, 5000000)
        arr.append(temp)
    x.append(i)
    initial = timeit.default_timer()
    mergeSort(arr, 0, i-1)
    final = timeit.default_timer()
    y.append(final - initial)
    n.append(i*log2(i)*0.00000125)
plt.plot(x, y, label = 'Merge Sort')
plt.plot(x, n, label = 'nlogn')
plt.legend()
plt.xlabel('Array size ')
plt.ylabel('Time ')
plt.title('Merge Sort')
plt.show()
