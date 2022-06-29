# Python program for time complexity graph of mergesort

from random import randint
from math import log2
import timeit
import matplotlib.pyplot as plt

def merge(arr, l, m, r):#merge function to merge the arrays
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
def mergeSort(arr, l, r):#mergesort function to perform mergesort
	if l < r:
		m = l+(r-l)//2
		mergeSort(arr, l, m)
		mergeSort(arr, m+1, r)
		merge(arr, l, m, r)
arr = []
x = []
y = []
n = []
for i in range(1, 5000, 50):
    for j in range(i):
        temp = randint(0, 100000)
        arr.append(temp)
    x.append(i)
    start = timeit.default_timer()#starts timer
    mergeSort(arr, 0, i-1)
    end = timeit.default_timer()#stops timer
    y.append(end - start)
    n.append(i*log2(i)*0.00000103)
plt.plot(x, y, label = 'MergeSort', color = 'blue')
plt.plot(x, n, label = 'nlogn', color = 'red')
plt.legend()
plt.xlabel('Array size ------>')
plt.ylabel('Time taken (s) ------>')
plt.title('Merge Sort')
plt.show()