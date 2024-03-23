n = int(input())
flag = 'YES'
while n > 9:
    if n % 10 != (n // 10) % 10:
        flag = 'NO'
    n //= 10
print(flag)

# # --- 1
#
# n = int(input())
# while n % 10 == n // 10 % 10:
#     n //= 10
# print('YES' if n < 10 else 'NO')


# # --- 2
#
# num = str(input())
# max, min = max(num), min(num)
# if max == min:
#     print('YES')
# else:
#     print('NO')

# # --- 3
#
# x = input()
# print('YES' if max(x) == min(x) else 'NO')

