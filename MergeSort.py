# Python program for implementation of MergeSort

# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]


from random import randint
from math import log2
import timeit
import matplotlib.pyplot as plt




def merge(arr, l, m, r):
	n1 = m - l + 1
	n2 = r - m

	# create temp arrays
	L = [0] * (n1)
	R = [0] * (n2)

	# Copy data to temp arrays L[] and R[]
	for i in range(0, n1):
		L[i] = arr[l + i]

	for j in range(0, n2):
		R[j] = arr[m + 1 + j]

	# Merge the temp arrays back into arr[l..r]
	i = 0	 # Initial index of first subarray
	j = 0	 # Initial index of second subarray
	k = l	 # Initial index of merged subarray

	while i < n1 and j < n2:
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1

	# Copy the remaining elements of L[], if there
	# are any
	while i < n1:
		arr[k] = L[i]
		i += 1
		k += 1

	# Copy the remaining elements of R[], if there
	# are any
	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1

# l is for left index and r is right index of the
# sub-array of arr to be sorted


def mergeSort(arr, l, r):
	if l < r:

		# Same as (l+r)//2, but avoids overflow for
		# large l and h
		m = l+(r-l)//2

		# Sort first and second halves
		mergeSort(arr, l, m)
		mergeSort(arr, m+1, r)
		merge(arr, l, m, r)


# Driver code to test above
arr = []
x = []
y = []
n = []
for i in range(1, 20000):
    # n = len(arr)
    for j in range(i):
        temp = randint(0, 100000)
        arr.append(temp)
    # print("Given array is")
    # for k in range(i):

    x.append(i)
    start = timeit.default_timer()
    mergeSort(arr, 0, i-1)
    end = timeit.default_timer()
    y.append(end - start)
    n.append(i*log2(i)*0.00000112)
    # print(end - start)
    # print("\n\nSorted array is")
    # for l in range(i):
    #     print("%d" % arr[l],end=" ")
    # print("\n")
plt.plot(x, y, label = 'MergeSort')
plt.plot(x, n, label = 'nlogn')
plt.legend()
plt.xlabel('Array size ------>')
plt.ylabel('Time taken (s) ------>')
plt.title('Merge Sort')
plt.show()

