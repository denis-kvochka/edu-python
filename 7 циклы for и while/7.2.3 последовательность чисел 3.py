m, n = int(input()), int(input())
m = m - 1 * (not (m % 2))
n = n - 1 * (n % 2)
for i in range(m, n, -2):
    print(i)