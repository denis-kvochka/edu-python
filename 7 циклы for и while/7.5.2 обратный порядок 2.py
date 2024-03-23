n = int(input())
new_n = ''
while n != 0:
    last_digit = n % 10
    new_n = new_n + str(last_digit)
    n //= 10
print(int(new_n))

# n = int(input())
# while n != 0:
#     print(n % 10, end = '')
#     n = n // 10