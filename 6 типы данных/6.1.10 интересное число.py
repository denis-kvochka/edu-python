# put your python code here
n = int(input())
a = n // 100
b = n % 100 // 10
c = n % 10
min, max = min(a, b, c), max(a, b, c)
if max - min == (a + b + c) - max - min:
    print('Число интересное')
else:
    print('Число неинтересное')