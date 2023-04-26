from math import log

n = int(input())
asim = 0
for i in range(1, n + 1):
    asim = asim + 1 / i
print(asim - log(n))
