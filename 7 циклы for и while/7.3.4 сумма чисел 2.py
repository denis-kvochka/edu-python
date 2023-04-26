n = int(input())
total = 0
for i in range(1, n + 1):
    last_digit = str(i**2 % 10)
    if last_digit in '258': 
        total += i
print(total)