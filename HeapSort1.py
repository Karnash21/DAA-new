from random import randint


arr = []
for i in range(1, 10, 1):
    # arr.append(randint())
    for j in range(i):
        rndm = randint(1, 5000)
        arr.append(rndm)
        # print(rndm)
    # for k in range(i):
        # print(arr)
print(arr)




# arr = [ 93, 55, 45, 98]
# heapSort(arr)
# n = len(arr)
# print("Sorted array is")
# for i in range(n):
#     print(arr[i])