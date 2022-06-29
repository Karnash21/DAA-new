import time
import random
from math import ceil

import matplotlib.pyplot as plt

def add_digit(nString, zeros, left = True):
    for i in range(zeros):
        if left:
            nString = '0' + nString
        else:
            nString = nString + '0'
    return nString
    
def multiply(x ,y):
    x = str(x)
    y = str(y)
    if len(x) == 1 and len(y) == 1:
        return int(x) * int(y)
    if len(x) < len(y):
        x = add_digit(x, len(y) - len(x))
    elif len(y) < len(x):
        y = add_digit(y, len(x) - len(y))
    n = len(x)
    j = ceil(n/2)
    BZeroPadding = n - j
    AZeroPadding = BZeroPadding * 2
    a = int(x[:j])
    b = int(x[j:])
    c = int(y[:j])
    d = int(y[j:])
    ac = multiply(a, c)
    bd = multiply(b, d)
    k = multiply(a + b, c + d)
    A = int(add_digit(str(ac), AZeroPadding, False))
    B = int(add_digit(str(k - ac - bd), BZeroPadding, False))
    return A + B + bd

n = []
et = []
n_z=[]
n_y = []

for i in range(100,2000,200):
    x = random.randint(1, 10**i)
    y = random.randint(1, 10**i)

    start = time.time_ns()
    z = multiply(x, y)
    end = time.time_ns()

    n.append(len(str(x)))
    et.append((end - start) * 0.000055)
   
    max_len=len(str(max(x,y)))
   
    n_y.append((max_len**(1.6)))
    n_z.append((max_len**(1.59)))
    
plt.plot(n, et, label="Integer multiplication")
plt.plot(n, n_z, label="n^1.59")
plt.plot(n, n_y, label="n^1.6")
plt.xlabel('Digits')
plt.ylabel('Time')
plt.title('Integer Multiplication')
plt.legend()
plt.show()