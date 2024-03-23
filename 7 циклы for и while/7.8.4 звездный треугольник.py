n = int(input())
# ver 1
for i in range(1, n + 1):
    if i  > (n + 1) / 2:
        print('*' * (n - i + 1), end = '')
    else:
        print('*' * i, end = '')
    print()

# ver 2
# for i in range(n):
#     cur_cnt = (n // 2 + 1) - abs(n // 2 - i)
#     for j in range(cur_cnt):
#         print("*", end="")
#     print()