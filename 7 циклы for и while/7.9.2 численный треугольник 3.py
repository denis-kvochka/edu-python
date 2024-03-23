for n in range (1, int(input()) + 1):
    output = "1"

    for i in range(2, n + 1):
        output = output + str(i)
    for j in range(n - 1, 0, -1):
        output = output + str(j)
        
    print(output)

# n = int(input())

# for i in range(1, n + 1):
#     for j in range(1, i):
#         print(j, end="")

#     print(i, end="")

#     for j in range(i - 1, 0, -1):
#         print(j, end="")

#     print()
