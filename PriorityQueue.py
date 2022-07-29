import matplotlib.pyplot as plt
import numpy as np
import time , random

def Heapify(Arr,i,Arr_len2):
    left_child = 2 * i + 1  #leftChild child
    right_child = 2 * i + 2 #rightChild child
    if left_child < Arr_len2 and Arr[left_child] > Arr[i]:
        largest = left_child
    else:
        largest = i
    if right_child < Arr_len2 and Arr[right_child] >=Arr[largest]:
        largest = right_child
    if largest != i:
        Arr[i], Arr[largest] = Arr[largest], Arr[i]
        Heapify(Arr, largest,Arr_len2)

#Build heap
def BuildHeap(Arr):
    for i in range(int((len(Arr)/2)-1), -1, -1):
        Heapify(Arr,i,len(Arr))

#finding Maximum Element
def FindingMax(arr):
    return arr[0]

#Extracting max element
def extractMax2(Arr):
    len_Arr=len(Arr)
    if len_Arr<1:
        return -1
    elif len_Arr==1:
        return Arr[0]
    else:
        max_element=Arr[0]
        Arr[0]=Arr[len(Arr)-1]
        lst=np.delete(Arr,len(Arr)-1)
        Heapify(Arr,0,len(Arr))
        return max_element

#Incerase Key
def increaseKey(Arr,i,key):
    if Arr[i]>key:
        return -1
    Arr[i]=key
    while (i>0 and Arr[(i)//2]<Arr[i]):
        Arr[i],Arr[(i)//2]=Arr[(i)//2],Arr[i]
        i=i//2

#Insert A value
def insert(Arr,key):
    Arr=np.insert(Arr,-1,len(Arr)+1)
    increaseKey(Arr,len(Arr)-1,key)
    

#main function
time_extract_max=[]
time_increase_key=[]
time_insert_key=[]
time_finding_max=[]
randarr_len=[]
for i in range(1,50):
    randarr=np.random.randint(1,20,i*30)
    randarr_len.append(len(randarr))
    BuildHeap(randarr)

    st_timer1=time.perf_counter()
    largest=FindingMax(randarr)
    time_finding_max.append((time.perf_counter()-st_timer1))
    
    st_timer2=time.perf_counter()
    extractMax2(randarr)
    time_extract_max.append(((time.perf_counter()-st_timer2)))
    
    st_timer3=time.perf_counter()
    increaseKey(randarr,random.randint(10,20),random.randint(40,50))
    time_increase_key.append((time.perf_counter()-st_timer3))

    st_timer4=time.perf_counter()
    insert(randarr,random.randint(40,60))
    time_insert_key.append((time.perf_counter()-st_timer4))

logn=[(np.log2(i)/10**4.6) for i in randarr_len] #logn


plt.plot(randarr_len,logn,label="logn")
plt.plot(randarr_len,time_extract_max,label="Extract Max")
plt.plot(randarr_len,time_increase_key,label="Increase Key")
plt.plot(randarr_len,time_insert_key,label="Insert Key")
plt.plot(randarr_len,time_finding_max,label="Finding max")

plt.title("All heap operations")
plt.xlabel("No. of inputs")
plt.ylabel("Total time taken")
plt.legend()
plt.show()
#On comparing with logn the graph comes as expected but not always
#Priority queue is implemented