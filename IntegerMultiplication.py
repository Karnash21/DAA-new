# Python program for time complexity graph of integer multiplication using divide and conquer

import time
import random

import matplotlib.pyplot as plt

def addzero(nString, zeros, left = True):#for adding zeroes
    for i in range(zeros):
        if left:#adds zeroes to left
            nString = '0' + nString
        else:#adds zeroes to right
            nString = nString + '0'
    return nString
    
def multiply(x ,y):#for integer multiplication
    x = str(x)
    y = str(y)
    if len(x) == 1 and len(y) == 1:
        return int(x) * int(y)
    if len(x) < len(y):
        x = addzero(x, len(y) - len(x))
    elif len(y) < len(x):
        y = addzero(y, len(x) - len(y))
    n = len(x)
    j = n//2
    if (n % 2) != 0:
        j += 1    
    Baddzero = n - j
    Aaddzero = Baddzero * 2
    a = int(x[:j])
    b = int(x[j:])
    c = int(y[:j])
    d = int(y[j:])
    ac = multiply(a, c)
    bd = multiply(b, d)
    k = multiply(a + b, c + d)
    A = int(addzero(str(ac), Aaddzero, False))
    B = int(addzero(str(k - ac - bd), Baddzero, False))
    return A + B + bd

n = []
et = []
n_z=[]
n_y = []

for i in range(1,2000,200):
    x = random.randint(i, 2**i)
    y = random.randint(i, 2**i)

    start = time.time_ns()#for calculating time
    z = multiply(x, y)
    end = time.time_ns()#for calculating time

    n.append(len(str(x)))
    et.append((end - start) * 0.00005975)

    max_len=len(str(max(x,y)))
    n_y.append((max_len**(1.6)))
    n_z.append((max_len**(1.59)))
    
plt.plot(n, et, label="Integer multiplication",color="r")#plots graph for integer multiplication
plt.plot(n, n_z, label="n^1.59",color="g")#plots graph for n^1.59
plt.plot(n, n_y, label="n^1.6",color="b")#plots graph for n^1.6
plt.xlabel('No of bits ------>')
plt.ylabel('Time taken (s) ------>')
plt.title('Integer Multiplication')
plt.legend()
plt.show()#shows graph
