m, n = int(input()), int(input())
if m < n:
    k = 1
else:
    k = -1
for i in range(m, n + k, k):
    print(i)
