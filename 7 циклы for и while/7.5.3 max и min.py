n = int(input())
min_d, max_d = 9, 0
while n != 0:
    digit = n % 10
    if digit > max_d:
        max_d = digit
    if digit < min_d:
        min_d = digit
    n = n // 10
print('Максимальная цифра равна', max_d)
print('Минимальная цифра равна', min_d)

# x = input()
# print('Максимальная цифра равна', max(x))
# print('Минимальная цифра равна', min(x))

# n, x, m = int(input()), -1, 10
# while n:
#     x = max(x, n % 10)
#     m = min(m, n % 10)
#     n //= 10
# print('Максимальная цифра равна', x)
# print('Минимальная цифра равна', m)