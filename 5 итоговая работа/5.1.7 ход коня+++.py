# put your python code here
c1, r1, c2, r2 = int(input()), int(input()), int(input()), int(input())
cc = c1 - c2
rr = r1 - r2
if (((cc == 1 or cc == -1) and (rr == 2 or rr == -2)) or
        ((cc == 2 or cc == -2) and (rr == 1 or rr == -1))):
    print('YES')
else:
    print('NO')
