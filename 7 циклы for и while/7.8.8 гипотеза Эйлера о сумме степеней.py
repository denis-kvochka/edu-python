for a in range(1, 151, 4):
    print(a)
    for b in range(2, 151, 4):
        for c in range(3, 151, 4):
            for d in range(4, 151, 4):
                if ((a**5 + b**5 + c**5 + d**5)**(1/5)) % 1 == 0:
                    print('result =', a + b + c + d)