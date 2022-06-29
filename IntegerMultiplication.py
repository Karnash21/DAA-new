def multiply(A, B):
n = len(A)
half = n // 2

if n <= 1:
    return [A[0] * B[0]]

xl, xh = A[:half], A[half:]
yl, yh = B[:half], B[half:]

a = multiply(xh, yh)
b = multiply(xh, yl)
c = multiply(xl, yh)
d = multiply(xl, yl)

b = add(b, c)

d = shift(d, n)
b = shift(b, half)

return add_n(a, b, d)