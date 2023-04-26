# put your python code here
c1, r1, c2, r2 = int(input()), int(input()), int(input()), int(input())
mc, mr = c1 - c2, r1 - r2
if mc < 0:
    mc = mc * (-1)
if mr < 0:
    mr = mr * (-1)
if mc == mr:
    print('YES')
else:
    print('NO')
