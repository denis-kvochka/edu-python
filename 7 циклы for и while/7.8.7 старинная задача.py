for b in range(1, 100):
    for k in range(1, 100):
        for t in range(1, 100):
            if 10 * b + 5 * k + 0.5 * t == 100:
                print('b =', b, "\nk =", k, "\nt = ", t)

# v2
# for x in range(1, 10):
#     for y in range(1, 18):
#         for z in range(2, 99, 2):
#             if (x*10 + y*5 + z/2 == 100) and (x + y + z == 100):
#                 print(x, y, z)