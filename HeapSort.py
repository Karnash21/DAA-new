from cmath import log
import random
import matplotlib.pyplot as plt
import time
from math import log2
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l
    else:
        largest = i

    if r < n and arr[r] > arr[largest]:
        largest = r
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n , largest)

def heapsort(arr):

    #Buld max heap
    n = len(arr)

    #Index of the last non-leaf node
    start_index = n//2 - 1

    # Perform reverse level order traversal
    # from last non-leaf node and heapify each node
    for i in range(start_index, 0-1, -1):
        heapify(arr, n, i)

    # One by one extract elements 
    for i in range(n-1, 0, -1):
          # Swap
          arr[i], arr[0] = arr[0], arr[i]

          # Heapify root element
          heapify(arr, i, 0)
    
array = []
t = []
s = []
time_complexity = []
for size in range(1, 20000, 500):

    s.append(size)
    array = [x for x in range(1, size+1)]
    random.shuffle(array)

    start = time.time_ns()
    heapsort(array)
    end = time.time_ns()

    total_time = end - start
    t.append(total_time)

    #nlog
    tc = size * (log2(size))*1400
    time_complexity.append(tc)

    # print('Sorted array: {}'.format(array))

#plot
plt.plot(s, t, label = "Heapsort")
plt.plot(s, time_complexity, label = "nlogn")
plt.xlabel("size")
plt.ylabel("time")
plt.title("Heapsort")
plt.legend()
plt.show()
#On comparison with nlogn we get the graph similar to nlogn 
#because it has the time complexity of O(nlogn)