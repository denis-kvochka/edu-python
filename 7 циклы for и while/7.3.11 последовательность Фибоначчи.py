n = int(input())

prev_sum = 0
str_f = '1'

if n == 0:
    print('0')
elif n == 1:
    print('1')
else:
    n1 = 1
    n2 = 0
    for i in range(2, n + 1):
        f = n1 + n2
        str_f = str_f + ' ' + str(f)
        n2, n1 = n1, f
    print(str_f)

# n = int(input())
# a, b = 1, 1

# for i in range(n):
#     print(a, end=' ')
#     a, b = b, a + b