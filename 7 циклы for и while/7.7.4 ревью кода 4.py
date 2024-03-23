# n = int(input())
# if n == 0:
#     print(0)
# else:
#     max_digit = -1
#     while n > 0:
#         digit = n % 10
#         if digit % 3 == 0:
#             if digit > max_digit:
#                 max_digit = digit
#         n = n // 10
#     if max_digit == -1:
#         print('NO')
#     else:
#         print(max_digit)

n = int(input())
max_digit = -1
while n > 0:
    digit = n % 10
    if digit % 3 == 0:
        if digit > max_digit:
            max_digit = digit
    n = n // 10
if max_digit == -1:
    print('NO')
else:
    print(max_digit)