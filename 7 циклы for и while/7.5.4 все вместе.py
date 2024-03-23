n = int(input())
d_sum, d_count, d_mult, d_first = 0, 0, 1, 0
num = n
while n:
    last_digit = n % 10
    d_sum += last_digit
    d_count += 1
    d_mult *= last_digit
    n //= 10
# print(d_sum)
# print(d_count)
# print(d_mult)
# print(d_sum / d_count)
# print(last_digit)
# print(last_digit + num % 10)

print(d_sum, d_count, d_mult, d_sum / d_count, last_digit, last_digit + num % 10, sep = '\n')
