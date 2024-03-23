n = int(input())
for i in range(2, n + 1):
    if n % i == 0:
        print(i)
        break

# n, div = int(input()), 2
# while n % div:
#     div += 1
# print(div)