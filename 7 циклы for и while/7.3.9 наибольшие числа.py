max_number = 0
pre_max_number = 0
n = int(input())
for _ in range(n):
    i = int(input())
    if i > max_number:
        pre_max_number = max_number
        max_number = i
    elif i > pre_max_number:
        pre_max_number = i
print(max_number, pre_max_number, sep='\n')
