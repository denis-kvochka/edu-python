# put your python code here
c1, r1, c2, r2 = int(input()), int(input()), int(input()), int(input())
if (c1 % 2 != 0 and r1 % 2 != 0) or (c1 % 2 == 0 and r1 % 2 == 0):
    color1 = 'white'
else:
    color1 = 'black'
if (c2 % 2 != 0 and r2 % 2 != 0) or (c2 % 2 == 0 and r2 % 2 == 0):
    color2 = 'white'
else:
    color2 = 'black'
if color1 == color2:
    print('YES')
else:
    print('NO')
