n = int(input())
counter = 0
for i in range(1, n + 1):
    for j in range(i):
        counter += 1
        print(counter, end=' ')
    print()

# # ver 2
#
# for y in range(1, int(input())+1):
#     for x in range(y):
#         print(y * (y - 1) // 2 + x + 1, end=' ')
#     print()