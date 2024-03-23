n = int(input())
while n:
    if 0 < n // 10 < 10:
        print(n % 10)
    n //= 10

# n = int(input())
# while n > 99:
#     n //= 10
# print(n % 10)