import time
import random

import matplotlib.pyplot as plt

def zeroPad(numberString, zeros, left = True):
    """Return the string with zeros added to the left or right."""
    for i in range(zeros):
        if left:
            numberString = '0' + numberString
        else:
            numberString = numberString + '0'
    return numberString
def karatsubaMultiplication(x ,y):
    """Multiply two integers using Karatsuba's algorithm."""
    #convert to strings for easy access to digits
    x = str(x)
    y = str(y)
    #base case for recursion
    if len(x) == 1 and len(y) == 1:
        return int(x) * int(y)
    if len(x) < len(y):
        x = zeroPad(x, len(y) - len(x))
    elif len(y) < len(x):
        y = zeroPad(y, len(x) - len(y))
    n = len(x)
    j = n//2
    #for odd digit integers
    if (n % 2) != 0:
        j += 1    
    BZeroPadding = n - j
    AZeroPadding = BZeroPadding * 2
    a = int(x[:j])
    b = int(x[j:])
    c = int(y[:j])
    d = int(y[j:])
    #recursively calculate
    ac = karatsubaMultiplication(a, c)
    bd = karatsubaMultiplication(b, d)
    k = karatsubaMultiplication(a + b, c + d)
    A = int(zeroPad(str(ac), AZeroPadding, False))
    B = int(zeroPad(str(k - ac - bd), BZeroPadding, False))
    return A + B + bd

n = []
et = []
n_z=[]
n_y = []

for i in range(100,2000,200):
    x = random.randint(i, 10**i)
    y = random.randint(i, 10**i)

    start = time.time_ns()
    z = karatsubaMultiplication(x, y)
    end = time.time_ns()

    n.append(len(str(x)))
    #print("n ke value=",n)
    executionTime = end - start
    et.append(executionTime * 0.00005975)
   
    max_len=len(str(max(x,y)))
   
    n_y.append((max_len**(1.6)))
    n_z.append((max_len**(1.59)))
    
plt.plot(n, et, label="Integer multiplication",color="r")
plt.plot(n, n_z, label="n^1.59",color="g")
plt.plot(n, n_y, label="n^1.6",color="b")
plt.xlabel('No of bits ------>')
plt.ylabel('Time taken (s) ------>')
plt.title('Integer Multiplication')
plt.legend()
plt.show()